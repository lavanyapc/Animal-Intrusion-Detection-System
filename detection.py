import cv2
import numpy as np
import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust COM port or path as needed
time.sleep(2)  # Wait for Arduino to initialize

# Load cascade classifier for human detection
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')  # Adjust path to cascade file as needed

# Initialize webcam capture (replace '0' with the appropriate webcam index if needed)
cap = cv2.VideoCapture(0)

# Initialize servo control
def open_door():
    ser.write(b'O')  # Send command to Arduino to open the door

def close_door():
    ser.write(b'C')  # Send command to Arduino to close the door

# Main loop for human detection and door control
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect humans in the frame
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(humans) > 0:
        # At least one human detected, open the door
        open_door()
        print("Human detected, door opened.")
    else:
        # No humans detected, close the door
        close_door()
        print("No humans detected, door closed.")

    cv2.imshow('Human Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
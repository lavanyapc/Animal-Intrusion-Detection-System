# Smart Automatic Door System using Human Detection

A smart door automation system that uses Computer Vision and Arduino to automatically control the opening and closing of a door based on the presence of a human. The system uses OpenCV's Haar Cascade classifier to detect human bodies through a webcam and communicates with an Arduino over serial communication to operate a servo motor.

This project demonstrates the integration of Computer Vision with Embedded Systems to create a simple, contactless, and automated door control system.

---

# Motivation

Automatic door systems have become increasingly common in homes, offices, hospitals, and commercial buildings, providing convenience, accessibility, and hands-free operation. Inspired by these systems, we developed a prototype that uses computer vision to detect the presence of a person and automatically control the movement of a door.

The primary objective of this project is to demonstrate how Computer Vision and Embedded Systems can work together to automate a simple real-world application. To validate the concept, we built a miniature door prototype using cardboard, controlled by a servo motor connected to an Arduino. The webcam continuously monitors the entrance, and the door automatically opens when a person is detected and closes when no one is present.

---

# Features

- Real-time human detection using OpenCV
- Automatic door opening and closing
- Live webcam monitoring
- Arduino and Python serial communication
- Servo motor-based door control
- Prototype implementation using a cardboard door model
- Simple and lightweight implementation

---

# Technologies Used

## Software

- Python 3
- OpenCV
- NumPy
- PySerial
- Arduino IDE

## Hardware

- Arduino Uno
- Servo Motor
- USB Webcam
- Cardboard Door Prototype
- Jumper Wires
- USB Cable

---

# Project Structure

```
Smart-Automatic-Door-System/
│
├── detection.py              # Human detection and serial communication
├── servo.cpp                 # Arduino servo motor control
├── cascadefrontalface.xml    # Haar Cascade classifier for face detection
├── cascadefullbody.xml       # Haar Cascade classifier for full body detection
└── README.md
```

---

# System Workflow

1. The webcam continuously captures live video.
2. Each frame is converted to grayscale.
3. The Haar Cascade classifier detects the presence of a human body.
4. If a human is detected:
   - Python sends the command **'O'** to the Arduino.
   - The servo motor rotates to open the door.
5. If no human is detected:
   - Python sends the command **'C'** to the Arduino.
   - The servo motor rotates back to close the door.
6. The process continues until the application is terminated.

---

# Working Principle

```
Webcam
   │
   ▼
Capture Video Frames
   │
   ▼
Convert to Grayscale
   │
   ▼
Human Detection using Haar Cascade
   │
   ├──────────────┐
   │              │
Human          No Human
Detected        Detected
   │              │
   ▼              ▼
Send 'O'      Send 'C'
to Arduino    to Arduino
   │              │
   ▼              ▼
Servo Opens   Servo Closes
the Door      the Door
```

---

# Installation

## Prerequisites

Install the required Python libraries:

```bash
pip install opencv-python numpy pyserial
```

Upload the `servo.cpp` file to the Arduino using the Arduino IDE.

Update the serial port in `detection.py` according to your operating system.

For Linux:

```python
ser = serial.Serial('/dev/ttyUSB0', 9600)
```

For Windows:

```python
ser = serial.Serial('COM3', 9600)
```

Run the Python program:

```bash
python detection.py
```

Press **Q** to exit the application.

---

# Serial Communication

The Arduino communicates with the Python application at **9600 baud rate**.

| Command | Action |
|---------|--------|
| `O` | Opens the door |
| `C` | Closes the door |

---

# Prototype Demonstration

The project was demonstrated using a miniature cardboard door prototype operated by a servo motor. The webcam continuously monitors the area in front of the door, while the Python application processes the video feed to detect human presence.

When a person is detected, the Arduino rotates the servo motor to open the cardboard door. Once the person is no longer detected, the servo returns to its original position, automatically closing the door. This prototype demonstrates the practical implementation of an automated door system using Computer Vision and Embedded Systems.

---

# Applications

- Smart homes
- Office entrances
- Laboratories
- Libraries
- Educational institutions
- Automatic access systems
- Contactless door automation

---

# Future Enhancements

- Implement face recognition for authorized access.
- Add RFID or keypad authentication.
- Integrate IoT for remote monitoring and control.
- Maintain entry and exit logs.
- Integrate with electronic door locking systems.
- Support multiple object detection.


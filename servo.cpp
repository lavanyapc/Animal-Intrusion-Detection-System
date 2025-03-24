#include <Servo.h>

Servo servoMotor;  // Create a servo object to control the motor
int servoPin = 3;  // Define the Arduino pin connected to the servo motor

void setup() {
  servoMotor.attach(servoPin);  // Attach the servo to the specified pin
  Serial.begin(9600);  // Initialize serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming command

    if (command == 'O') {
      openDoor();  // Call the openDoor function
    } else if (command == 'C') {
      closeDoor();  // Call the closeDoor function
    }
  }
}

void openDoor() {
  servoMotor.write(0);  // Rotate the servo to open the door position
}

void closeDoor() {
  servoMotor.write(90);  // Rotate the servo to close the door position
}
# Animal Intrusion Detection System

A smart door automation system designed to prevent stray dogs from entering hostel premises while allowing people to pass through without manual intervention. The system uses Computer Vision to monitor the entrance through a webcam and controls a servo motor using an Arduino to automate the opening and closing of the door.

This project was developed as a prototype to demonstrate how computer vision and embedded systems can be combined to solve a practical problem commonly faced in hostel environments.

---

# Motivation

In many hostels, room doors and entrance gates are often left open for ventilation or convenience. However, this frequently allows stray dogs to wander into hostel corridors, rooms, and common areas, causing inconvenience and discomfort to students.

To address this issue, we proposed a Smart Automatic Door System capable of distinguishing between humans and stray dogs. The objective is to allow humans to enter normally while preventing dogs from accessing restricted areas.

As a proof of concept, we developed a working prototype using a cardboard door model driven by a servo motor and controlled through an Arduino. The prototype demonstrates how an automated access system can help improve safety and hygiene in hostel environments.

---

# Features

- Real-time monitoring using a webcam
- Computer vision-based object detection
- Automatic door control using a servo motor
- Arduino and Python serial communication
- Prototype implementation using a cardboard door model
- Hands-free and automated operation

---

# Technologies Used

## Software

- Python
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
├── detection.py
├── servo.cpp
├── cascadefrontalface.xml
├── cascadefullbody.xml
└── README.md
```

---

# Working Principle

1. A webcam continuously monitors the entrance.
2. Video frames are processed using OpenCV.
3. The detection algorithm analyzes objects appearing in front of the entrance.
4. If a dog is detected, the door remains closed, preventing entry.
5. The servo motor controls the opening and closing of the prototype door.

---

# Prototype Demonstration

The proposed system was demonstrated using a miniature cardboard door prototype. A servo motor was attached to the door and controlled by an Arduino. A webcam continuously monitored the entrance, while the Python application processed the video feed and transmitted commands to the Arduino through serial communication.

The prototype successfully demonstrates the concept of automated door control and its potential application in hostel entrances to prevent stray dog entry while allowing access to people.

---

# Applications

- Hostel entrances
- Hostel room doors
- Apartment entrances
- Residential buildings
- Smart home automation
- Animal-restricted access systems

---

# Future Enhancements

- Support multiple animal classifications.
- Integrate IoT for remote monitoring.
- Add RFID or face recognition for authorized access.
- Maintain entry and exit logs.
- Integrate with electronic smart locks.

# Mini AI Home Project

This project demonstrates a smart home system that can control a light (LED), fan (motor), and buzzer (sound) using hand gestures. It uses OpenCV and MediaPipe for real-time hand gesture recognition and communicates with an Arduino Uno to control the devices.

## Features

- **Open/Closed Palm** for controlling the LED (light)
- **Thumbs Up/Down** for controlling the buzzer (sound)
- **Victory Sign/One Finger** for controlling the fan (motor)
- **Adjustable Intensity** using the thumb and index finger distance

## Requirements

- **Hardware**
  - Arduino Uno
  - LED
  - Fan (motor)
  - Buzzer (sound source)
  - Servo motors or DC motors (for fan control)
  
- **Software**
  - Python 3.x
  - OpenCV
  - MediaPipe
  - Arduino IDE
  - Serial communication (COM port)

## Libraries

- OpenCV: `pip install opencv-python`
- MediaPipe: `pip install mediapipe`
- Arduino IDE (for uploading code to Arduino)

## Setup Instructions

### 1. Hardware Setup

- Connect the **LED** to pin 3 on the Arduino.
- Connect the **Fan (Motor)** to pin 5 on the Arduino.
- Connect the **Buzzer** to pin 6 on the Arduino.

### 2. Software Setup

#### Python Code

1. Clone or download the Python script for gesture recognition and serial communication.

2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe

    Modify the serial port in the Python script (COM3 to your corresponding port if needed).

    Run the Python script:

    python gesture_control.py

Arduino Code

    Open the Arduino IDE and paste the Arduino code provided in the Arduino Code section.

    Upload the code to the Arduino Uno.

3. How to Use

    Gesture Controls:
        Open Palm: LED ON
        Closed Fist: LED OFF
        Thumbs Up: Buzzer ON
        Thumbs Down: Buzzer OFF
        Victory Sign: Fan ON
        One Finger Up: Fan OFF
    Intensity Control: After turning ON any device (LED, Fan, or Buzzer), the intensity can be adjusted by bringing your thumb and index finger closer or farther apart. The closer they are, the lower the intensity (brightness, fan speed, or sound volume), and the farther apart, the higher the intensity.

## Troubleshooting

    Camera not detected: Ensure that your camera is working correctly and is recognized by the system.
    Arduino not responding: Check the serial connection, ensure the correct COM port is used, and verify the wiring of the devices.

## Acknowledgments

    OpenCV and MediaPipe for hand gesture recognition.
    Arduino for hardware control and easy integration with sensors and actuators.
    The community for sharing code and tutorials that helped in developing this project.

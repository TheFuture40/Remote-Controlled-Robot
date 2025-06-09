# Remote-Controlled-Robot
Remote Controlled Robot using arduino and two bluetooth modules as master and receiver.
# 🤖 Bluetooth-Controlled Robot with Joystick and Arduino

A simple remote control robot system using two Arduino boards: one as a **master** with a joystick, and another as a **receiver** controlling motors. Communication is established via **Bluetooth** modules (HC-06).

---

## 🔗 System Overview

- **Master Arduino**: Reads joystick input and sends directional commands over Bluetooth.
- **Receiver Arduino**: Receives commands and moves the robot accordingly using two DC motors connected to a motor driver (Adafruit Motor Shield).

---

## 🧰 Components Used

| Component                | Quantity |
|--------------------------|----------|
| Arduino Uno              | 2        |
| HC-05 / HC-06 Bluetooth Module | 2    |
| Joystick Module          | 1        |
| Adafruit Motor Shield v1 | 1        |
| DC Motors (with wheels)  | 2        |
| Jumper Wires             | -        |
| Power Source (Battery)   | 1        |

---

## 📟 Master Code (Transmitter)

Reads analog joystick values and sends commands via Bluetooth based on direction.

### 🔧 Pin Configuration
- **Joystick X-axis**: `A0`
- **Joystick Y-axis**: `A1`
- **Bluetooth TX/RX**: Pins `10` (RX), `11` (TX)

### 📜 Code Summary
```cpp
const int joyX = A0;
const int joyY = A1;
const int threshold = 200;

SoftwareSerial bluetooth(10, 11);

void setup() {
  pinMode(joyX, INPUT);
  pinMode(joyY, INPUT);
  bluetooth.begin(9600);
  Serial.begin(9600);
}

void loop() {
  int xValue = analogRead(joyX);
  int yValue = analogRead(joyY);

  if (yValue > 512 + threshold) {
    bluetooth.println("FORWARD");
  } else if (yValue < 512 - threshold) {
    bluetooth.println("BACKWARD");
  } else if (xValue > 512 + threshold) {
    bluetooth.println("RIGHT");
  } else if (xValue < 512 - threshold) {
    bluetooth.println("LEFT");
  } else {
    bluetooth.println("STOP");
  }

  delay(100);
}

Receiver Code (Robot Side)

Receives Bluetooth commands and drives motors accordingly.

 Pin Configuration
	•	Bluetooth TX/RX: Pins 10 (RX), 11 (TX)
	•	Motor 1: Port 1 (AFMotor)
	•	Motor 2: Port 2 (AFMotor)

#include <AFMotor.h>
#include <SoftwareSerial.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
SoftwareSerial bluetooth(10, 11);

void setup() {
  bluetooth.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if (bluetooth.available()) {
    String command = bluetooth.readStringUntil('\n');

    if (command == "FORWARD") moveForward();
    else if (command == "BACKWARD") moveBackward();
    else if (command == "RIGHT") turnRight();
    else if (command == "LEFT") turnLeft();
    else if (command == "STOP") stopMotors();
  }
}

void moveForward() {
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}

void moveBackward() {
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
}

void turnRight() {
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
}

void turnLeft() {
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
}

void stopMotors() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

How It Works
	1.	The joystick reads X/Y analog values.
	2.	Based on the direction, the master Arduino sends a keyword (e.g., "FORWARD") via Bluetooth.
	3.	The receiver Arduino interprets the keyword and runs the corresponding motor function.

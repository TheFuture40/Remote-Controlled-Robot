// Receiver Program
#include <AFMotor.h> // Include the motor driver library


// Motor setup
AF_DCMotor motor1(1); // motor1 to port 1
AF_DCMotor motor2(2); // motor2 to port 2


// Bluetooth module pins
#include <SoftwareSerial.h>
SoftwareSerial bluetooth(10, 11); // RX, TX


void setup() {
  bluetooth.begin(9600); 
  Serial.begin(9600);   
}


void loop() {
  if (bluetooth.available()) {
    String command = bluetooth.readStringUntil('\n'); // Read the command


    if (command == "FORWARD") {
      moveForward();
    } else if (command == "BACKWARD") {
      moveBackward();
    } else if (command == "RIGHT") {
      turnRight();
    } else if (command == "LEFT") {
      turnLeft();
    } else if (command == "STOP") {
      stopMotors();
    }
  }
}


// Functions to control the robot
void moveForward() {
  motor1.setSpeed(255); // Max speed
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



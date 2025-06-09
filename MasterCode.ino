// Master Program
#include <SoftwareSerial.h>


// Pins for The joystick
const int joyX = A0; // Joystick X-axis
const int joyY = A1; // Joystick Y-axis


const int threshold = 200; 


// Bluetooth module pins
SoftwareSerial bluetooth(10, 11); // RX, TX


void setup() {
  pinMode(joyX, INPUT);
  pinMode(joyY, INPUT);
  bluetooth.begin(9600); 
  Serial.begin(9600);   
}


void loop() {
  int xValue = analogRead(joyX); // Read X-axis
  int yValue = analogRead(joyY); // Read Y-axis


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
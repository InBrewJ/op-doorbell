// Run this to fix permission stuff:
// sudo chmod a+rw /dev/ttyACM0
// or just add oneself to the 'dialout' group
//
// Tested with an Uno
// Designed for the doorbell @ number 13
// When the button is pressed, the message 'ding' is sent down the serial
// onUp, the message 'dong' is sent down the serial

#include <ArduinoJson.h>
int SWITCH_PIN = 2;
int LED_PIN = 3;


void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(SWITCH_PIN, INPUT);
  Serial.begin(9600);
}

StaticJsonDocument<200> buildPayload(int state) {
  StaticJsonDocument<200> out;
  // ding for down
  out["version"] = 1;
  out["state"]= state;
  return out;
}

void toggleLED() {
  digitalWrite(LED_PIN, !digitalRead(LED_PIN));  
}

void loop() {

  // Praise be to:
  // https://github.com/ArduinoGetStarted/button/blob/master/examples/03.SingleButtonDebounce/03.SingleButtonDebounce.ino

  int state = digitalRead(SWITCH_PIN);

  if (state == LOW) {
    Serial.println("isLOW");
  }

  if (state == HIGH) {
    Serial.println("isHIGH");
  }
  
}

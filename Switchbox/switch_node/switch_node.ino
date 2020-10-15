// Run this to fix permission stuff:
// sudo chmod a+rw /dev/ttyACM0
//
// Tested with an Uno
// Designed for the doorbell @ number 13
// When the button is pressed, the message 'ding' is sent down the serial
// onUp, the message 'dong' is sent down the serial

#include <ArduinoJson.h>
boolean triggered = false;

void setup() {
  pinMode(3, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(5, OUTPUT);
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);
}

StaticJsonDocument<200> buildPayload(String message) {
  StaticJsonDocument<200> out;
  // ding for down
  out["version"] = 1;
  out["message"]= message;
  return out;
}

void toggleLED() {
  digitalWrite(3, !digitalRead(3));  
}

void loop() {

  // Monitor inputs

  int doorbell_in = digitalRead(2);
  
  if (doorbell_in == LOW && triggered == false) {
    toggleLED();
    serializeJson(buildPayload("ding"), Serial);
    Serial.println();  
    triggered = true;
  }

  if (doorbell_in == HIGH && triggered == true) {
    toggleLED();
    serializeJson(buildPayload("dong"), Serial);
    Serial.println();  
    triggered = false;
  }

  
}

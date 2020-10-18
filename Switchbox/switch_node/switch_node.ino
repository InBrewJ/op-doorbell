// Run this to fix permission stuff:
// sudo chmod a+rw /dev/ttyACM0
//
// Tested with an Uno
// Designed for the doorbell @ number 13
// When the button is pressed, the message 'ding' is sent down the serial
// onUp, the message 'dong' is sent down the serial

#include <ArduinoJson.h>
#include <ezButton.h>
boolean triggered = false;
int SWITCH_PIN = 2;
int LED_PIN = 3;

ezButton button(SWITCH_PIN);

void setup() {
  pinMode(LED_PIN, OUTPUT);
//  pinMode(SWITCH_PIN, INPUT_PULLUP);
  Serial.begin(9600);
  button.setDebounceTime(60);
}

StaticJsonDocument<200> buildPayload(String message) {
  StaticJsonDocument<200> out;
  // ding for down
  out["version"] = 1;
  out["message"]= message;
  return out;
}

void toggleLED() {
  digitalWrite(LED_PIN, !digitalRead(LED_PIN));  
}

void loop() {

  // Praise be to:
  // https://github.com/ArduinoGetStarted/button/blob/master/examples/03.SingleButtonDebounce/03.SingleButtonDebounce.ino

  button.loop();

  if(button.isPressed()) {
    toggleLED();
    serializeJson(buildPayload("ding"), Serial);
    Serial.println(); 
  }

  if(button.isReleased()) {
    toggleLED();
    serializeJson(buildPayload("dong"), Serial);
    Serial.println();
  }
  
}

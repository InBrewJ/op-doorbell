// Run this to fix permission stuff:
// sudo chmod a+rw /dev/ttyACM0
// or just add oneself to the 'dialout' group
//
// Tested with an Uno
// Designed for the doorbell @ number 13
// When the button is pressed, the message 'ding' is sent down the serial
// onUp, the message 'dong' is sent down the serial

#include <ArduinoJson.h>
#include <ezButton.h>
int SWITCH_PIN = 2;
int LED_PIN = 3;

ezButton button(SWITCH_PIN);

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  // HUGE debounce because the doorbell cable is v long (maybe 20m)
  // And I don't have (optoisolator | ferrite bands | extra caps lying around)
  button.setDebounceTime(250);
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
    digitalWrite(LED_PIN, HIGH);
    serializeJson(buildPayload("ding"), Serial);
    Serial.println(); 
  }

  if(button.isReleased()) {
    digitalWrite(LED_PIN, LOW);
    serializeJson(buildPayload("dong"), Serial);
    Serial.println();
  }
  
}

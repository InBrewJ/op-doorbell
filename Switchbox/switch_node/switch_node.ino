// Run this to fix permission stuff:
// sudo chmod a+rw /dev/ttyACM0
//
// Tested with an Uno
// Designed for the doorbell @ number 13
// When the button is pressed, the message 'ding' is sent down the serial
// onUp, the message 'dong' is sent down the serial

#include <ArduinoJson.h>

const int SWITCH_PIN = 2;
const int LED_PIN = 3;

// Variables will change:
int ledState = LOW;          // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = HIGH;   // the previous reading from the input pin

// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 300;    // the debounce time; increase if the output flickers

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(SWITCH_PIN, INPUT);
  digitalWrite(LED_PIN, ledState);
  Serial.begin(9600);
}

StaticJsonDocument<200> buildPayload(String message) {
  StaticJsonDocument<200> out;
  // ding for down
  out["version"] = 1;
  out["message"]= message;
  return out;
}

void sendMessage(String message) {
   serializeJson(buildPayload(message), Serial);
   Serial.println();    
}

void turnOnLED() {
  digitalWrite(LED_PIN, HIGH);  
}

void turnOffLED() {
  digitalWrite(LED_PIN, LOW);  
}

void loop() {

   // read the state of the switch into a local variable:
  int reading = digitalRead(SWITCH_PIN);

  // check to see if you just pressed the button
  // (i.e. the input went from LOW to HIGH), and you've waited long enough
  // since the last press to ignore any noise:

  // If the switch changed, due to noise or pressing:
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer than the debounce
    // delay, so take it as the actual current state:

    // if the button state has changed:
    if (reading != buttonState) {
      buttonState = reading;

      // only toggle the LED if the new button state is LOW
      // we're using a 100ohm pullup resistor as described here:
      // https://electronics.stackexchange.com/questions/49824/microcontroller-with-a-long-wire-for-digital-input/49984#49984
      if (buttonState == LOW) {
        turnOnLED();
        sendMessage("ding");
      }

      if (buttonState == HIGH) {
        turnOffLED();
        sendMessage("dong");
      }
    }
  }

  // save the reading. Next time through the loop, it'll be the lastButtonState:
  lastButtonState = reading;
 
}

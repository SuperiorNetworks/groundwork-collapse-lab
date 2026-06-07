/*
Script Name: sensor_logger.ino
Version: 0.1.0
Purpose: Safe Arduino-compatible serial sensor logger for model-structure testing.
Copyright: 2026

Key Features:
- Emits timestamped CSV rows over serial.
- Supports an analog sound or impact-level input.
- Supports a simple digital event-marker button.
- Does not control actuators, ignition devices, pyrotechnics, energetic materials, or firing circuits.

Input Specifications:
- A0: analog sensor input, such as sound or vibration level.
- D2: event marker button to ground, using INPUT_PULLUP.

Output Specifications:
- Serial CSV at 115200 baud.
- Columns: timestamp_ms,sensor_id,x,y,z,sound_level,event_marker

Dependencies:
- Arduino IDE or compatible toolchain.
*/

const int SOUND_PIN = A0;
const int EVENT_PIN = 2;
const unsigned long SAMPLE_INTERVAL_MS = 50;

unsigned long lastSampleMs = 0;
bool lastEventState = HIGH;

void setup() {
  pinMode(EVENT_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  delay(500);
  Serial.println("timestamp_ms,sensor_id,x,y,z,sound_level,event_marker");
  Serial.print(millis());
  Serial.println(",system,,,,,start");
}

void loop() {
  unsigned long now = millis();

  bool eventState = digitalRead(EVENT_PIN);
  if (eventState == LOW && lastEventState == HIGH) {
    Serial.print(now);
    Serial.println(",manual_marker,,,,,event");
  }
  lastEventState = eventState;

  if (now - lastSampleMs >= SAMPLE_INTERVAL_MS) {
    lastSampleMs = now;
    int soundLevel = analogRead(SOUND_PIN);
    Serial.print(now);
    Serial.print(",sound_1,,,,");
    Serial.print(soundLevel);
    Serial.println(",");
  }
}

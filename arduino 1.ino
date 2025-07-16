const int potentiometerPin = 34; // ESP32 analog pin

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(potentiometerPin);
  Serial.print("Potentiometer Value: ");
  Serial.println(sensorValue);
  delay(50);
}
const int signalPin = 15; // GPIO pin connected to the cathode side of the diode (output side)

void setup() {
  Serial.begin(115200);
  pinMode(signalPin, INPUT);
}

void loop() {
  int signalState = digitalRead(signalPin);
  
  if (signalState == HIGH) {
    Serial.println("High voltage detected!");
  } else {
    Serial.println("No high voltage detected (safe).");
  }

  delay(500);
}

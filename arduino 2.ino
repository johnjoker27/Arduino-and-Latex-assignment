// Control LED brightness using a potentiometer on ESP32

// Pin connections
const int potPin = 34;  // Potentiometer connected to pin 34 (analog input)
const int ledPin = 25;  // LED connected to pin 25 (PWM output)

// Variables
int potValue = 0;   // Store the potentiometer reading
int brightness = 0; // LED brightness (0 to 255)

void setup() {
  Serial.begin(115200); // Start Serial Monitor

  // Set up PWM on the LED pin
  ledcSetup(0, 5000, 8); // Channel 0, 5kHz frequency, 8-bit resolution
  ledcAttachPin(ledPin, 0); // Attach pin 25 to channel 0
}

void loop() {
  // Read the potentiometer value (0 to 4095)
  potValue = analogRead(potPin);

  // Convert the potentiometer reading to brightness (0 to 255)
  brightness = map(potValue, 0, 4095, 0, 255);

  // Set the LED brightness
  ledcWrite(0, brightness);

  // Print values to Serial Monitor
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print(" | LED Brightness: ");
  Serial.println(brightness);

  delay(100); // Wait 100 milliseconds before next reading
}

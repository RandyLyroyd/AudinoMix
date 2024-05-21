const int NUM_SLIDERS = 5;
const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3, A4};

int analogSliderValues[NUM_SLIDERS];

void setup() { 
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }
  Serial.begin(9600);
}

void loop() {
  sendSliderValues();
  delay(10);
}

void sendSliderValues() {
  String printString = String("");

  for (int i = 0; i < NUM_SLIDERS; i++) {
    printString += String((int)analogRead(analogInputs[i]));

    if (i < NUM_SLIDERS - 1) {
      printString += String("|");
    }
  }
  
  Serial.println(printString);
}
const int NUM_SLIDERS = 5;
const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3, A4};

int analogSliderValues[NUM_SLIDERS];
bool button_state = false;

void setup() { 
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  sendSliderValues();
  checkButton();
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

void checkButton() {
  int buttonState = digitalRead(2);
  if (buttonState == HIGH && button_state) {
    button_state = false;
  }

  if (buttonState == LOW && not button_state) {
    button_state = true;
    Serial.println("Button");
  }
}
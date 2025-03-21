#define LED_PIN 3
#define FAN_PIN 5
#define BUZZER_PIN 6

bool led_on = false, fan_on = false, buzzer_on = false;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    if (command == "L_ON") {
      led_on = true;
      analogWrite(LED_PIN, 255);
    } else if (command == "L_OFF") {
      led_on = false;
      analogWrite(LED_PIN, 0);
    } else if (command.startsWith("L_") && led_on) {
      int val = command.substring(2).toInt();
      analogWrite(LED_PIN, val);
    }

    else if (command == "F_ON") {
      fan_on = true;
      analogWrite(FAN_PIN, 255);
    } else if (command == "F_OFF") {
      fan_on = false;
      analogWrite(FAN_PIN, 0);
    } else if (command.startsWith("F_") && fan_on) {
      int val = command.substring(2).toInt();
      analogWrite(FAN_PIN, val);
    }

    else if (command == "B_ON") {
      buzzer_on = true;
      analogWrite(BUZZER_PIN, 255);
    } else if (command == "B_OFF") {
      buzzer_on = false;
      analogWrite(BUZZER_PIN, 0);
    } else if (command.startsWith("B_") && buzzer_on) {
      int val = command.substring(2).toInt();
      analogWrite(BUZZER_PIN, val);
    }
  }
}

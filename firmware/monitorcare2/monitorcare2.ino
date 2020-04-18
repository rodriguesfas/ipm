
#define BAUND 9600
#define SENSOR_PIN A0

void setup(){
    Serial.begin(BAUND);
    pinMode(SENSOR_PIN, INPUT);
}

void loop(){
    int value = analogRead(SENSOR_PIN);
    if(value > 0) Serial.println(value);
}

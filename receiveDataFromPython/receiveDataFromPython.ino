String cmd;

int  solarLED = 5;
int  dieselLED = 6;
int  batteryLED = 7;
int  windLED = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(96500);
}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()==0){
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  }

cmd = Serial.readStringUntil("\r");
if(cmd = "solar"){
  digitalWrite(solarLED, HIGH);
  digitalWrite(dieselLED, LOW);
  digitalWrite(batteryLED, LOW);
  digitalWrite(windLED, LOW);
  }

if(cmd = "diesel"){
  digitalWrite(dieselLED, HIGH);
  digitalWrite(solarLED, LOW);
  digitalWrite(batteryLED, LOW);
  digitalWrite(windLED, LOW);
  }
if(cmd = "battery"){
  digitalWrite(batteryLED, HIGH);
  digitalWrite(solarLED, LOW);
  digitalWrite(dieselLED, LOW);
  digitalWrite(windLED, LOW);
  }
if(cmd = "wind"){
  digitalWrite(windLED, HIGH);
  digitalWrite(solarLED, LOW);
  digitalWrite(dieselLED, LOW);
  digitalWrite(batteryLED, LOW);
  }
}

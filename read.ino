int suctionpin = A0;   // select the input pin for the sensor
int deliverypin=A1;
int flowpin=A2;
int amperepin=A3;
int powerpin=A4;
int pfpin=A5;
int buttonpin=9;
int voltagepin=A6;
int rpmpin=A7;
int temppin=A8;
int vibpinx=A9;
int vibpiny=A10;
int vibpinz=A11;


int suction, delivery, flow, ampere, power, pf, voltage, temp, rpm, vibx, viby, vibz ;  // variable to store the value coming from the sensor
int confirm=0;

void setup() {
  // declare the ledPin as an OUTPUT:
  Serial.begin(9600);
  pinMode(suctionpin, INPUT);
  pinMode(deliverypin, INPUT);
  pinMode(flowpin, INPUT);
  pinMode(amperepin, INPUT);
  pinMode(powerpin, INPUT);
  pinMode(pfpin, INPUT);
  pinMode(buttonpin, Input)
  pinMode(voltagepin, INPUT);
  pinMode(rpmpin, INPUT);
  pinMode(vibpinx, INPUT);
  pinMode(vibpiny, INPUT);
  pinMode(vibpinz, INPUT);
}

void loop() {
  // read the value from the sensor:
  confirm=digitalRead(buttonpin);
if (confirm==HIGH){
  suction = analogRead(suctionpin);
  delivery = analogRead(deliverypin);
  flow = analogRead(flowpin);
  ampere = analogRead(amperepin);
  power = analogRead(powerpin);
  pf = analogRead(pfpin);
  voltage=analogRead(voltagepin);
  temp=analogRead(temppin);
  rpm=analogRead(rpmpin);
  vibx=analogRead(vibxpin);
  viby=analogRead(vibypin);
  vibz=analogRead(vibypin);
  

  Serial.println(rpm);
  Serial.println(",")  
  Serial.println(suction);
  Serial.println(",")
  Serial.println(delivery);
  Serial.println(",")
  Serial.println(flow);
  Serial.println(",")
  Serial.println(ampere);
  Serial.println(",")
  Serial.println(power);
  Serial.println(",");
  Serial.println(pf);
  Serial.println(",");
  Serial.println(voltage);
  Serial.println(",");
  Serial.println(temp);
  Serial.println(",");
  Serial.println(vibx);
  Serial.println(",");
  Serial.println(viby);
  Serial.println(",");
  Serial.println(vibz);
  
    
    
    
    
    
  delay(1000);
  }
  
}

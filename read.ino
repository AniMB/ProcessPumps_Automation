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



// Author: Animish Murthy
// Date: 18/05/23

int suction, delivery, flow, ampere, power, pf, voltage, temp, rpm ;  // variable to store the value coming from the sensor
int confirm=0;
long int t1, t2;
void setup() {
  // declare the Pin as an OUTPUT or INPUT
  Serial.begin(9600);
  pinMode(suctionpin, INPUT);
  pinMode(deliverypin, INPUT);
  pinMode(flowpin, INPUT);
  pinMode(amperepin, INPUT);
  pinMode(powerpin, INPUT);
  pinMode(pfpin, INPUT);
  pinMode(buttonpin, INPUT);
  pinMode(voltagepin, INPUT);
  pinMode(rpmpin, INPUT);
  
}

void loop() {
  // readS the value from the sensor IF button is pressed
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
  
  // Author: Animish Murthy
// Date: 18/05/23

  // prints the text with commmas
  Serial.print(rpm);
  Serial.print(",");
  Serial.print(suction);
  Serial.print(",");
  Serial.print(delivery);
  Serial.print(",");
  Serial.print(flow);
  Serial.print(",");
  Serial.print(ampere);
  Serial.print(",");
  Serial.print(power);
  Serial.print(",");
  Serial.print(pf);
  Serial.print(",");
  Serial.print(voltage);
  Serial.print(",");
  Serial.print(temp);
  Serial.print('/n');
 
  
  delay(1000);
  }


}
// Author: Animish Murthy
// Date: 18/05/23


//                                        _                                               _
//                                       / \         \"""\		    /"""/       / \
// 				       /   \         \   \		   /   /       /   \
//                                     /     \         \   \		  /   /       /     \
//                                    /   _   \         \   \ 	         /   /       /   _   \
//                                   /   / \   \         \   \           /   /	    /   / \   \
//                                  /   /   \   \         \   \         /   /       /   /   \   \ 
//                                 /   /     \   \         \   \       /   /   	  /   /     \   \
//                                /    """""""    \         \   \     /   /       /    """""""    \ 
//                               /                 \	    \   \   /   /       /                 \
//                              /    /"""""""""\    \	     \   \ /   /       /    /""""""""""\   \
//                             /    /           \    \ 	      \   V   /	      /    /		\   \
//                            /    /             \    \         \     /       /    /		 \   \
//                            """""               """""          """""        """""                """"  


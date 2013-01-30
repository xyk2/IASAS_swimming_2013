#define R1 9970
#define R2 4980
#define SYSTEM_VOLTAGE 3.3
#include <avr/power.h>


float voltage = 0;
int vDivRatio = (R1+R2)/R2;

void setup() {                
  Serial.begin(9600);  
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(9, OUTPUT); //xbee sleep
  power_twi_disable();
  power_spi_disable();
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(9, LOW);
  delay(100);
  voltage = ((analogRead(5)*(SYSTEM_VOLTAGE/1024)))*vDivRatio   ;
  Serial.println(voltage);
  delay(100);
  digitalWrite(9,HIGH);
  if(voltage > 6.2) { 
    digitalWrite(7, HIGH);
    digitalWrite(8, LOW);
  } else {
    digitalWrite(8, HIGH);
    digitalWrite(7,LOW);
  }
  delay(4800);
}

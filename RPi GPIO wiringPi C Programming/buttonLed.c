// COPYRIGHT (c) Ramzi Al Haddad 2002-2018
// I know its amazing code
#include <stdio.h>
#include <wiringPi.h>

#define led 4
#define button 17

void cleanup(){
	digitalWrite(led, 0);
}

int main(void){
	wiringPiSetupGpio();

	pinMode(led, OUTPUT);
	pinMode(button, INPUT);

	delay(1000);

	for(;;){
		delay(10);
		if(digitalRead(button) == 1){
			digitalWrite(led, 1);
		} else{
			digitalWrite(led, 0);
		}
	}
}

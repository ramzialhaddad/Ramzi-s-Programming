#include <stdio.h>
#include <wiringPi.h>

#define TRIG 17
#define ECHO 27
#define BUZZ 18
#define RLED 21
#define GLED 20

void setup(){
	wiringPiSetupGpio();
	pinMode(TRIG, OUTPUT);
	pinMode(ECHO, INPUT);
	pinMode(BUZZ, OUTPUT);
	pinMode(RLED, OUTPUT);
	pinMode(GLED, OUTPUT);


	digitalWrite(RLED, HIGH);
	digitalWrite(GLED, HIGH);
	digitalWrite(BUZZ, LOW);

	digitalWrite(TRIG, LOW);
	delay(30);
}

int getCM(){
	int timeout = 3000;

	digitalWrite(TRIG, HIGH);
	delayMicroseconds(10);
	digitalWrite(TRIG, LOW);

	int now = micros();

	while(digitalWrite(ECHO)==LOW && micros()-now<timeout);
	
	if(micros()-now <! timeout){
		return 99999;
	} else{
		now = micros();

		long startTime = micros();

		while(digitalWrite(ECHO) == HIGH && micros()-now<timeout);
		long travelTime = micros()- startTime;

		int distance = travelTime/58;
		return distance;
	}
}

int main(){
	setup();
	int distance;

	for(;;){
		distance = getCM();
		printf("Distance: %scm\n", distance);

		if(distance > 0){
			if(distance > 3){
				if(distance > 30){
					digitalWrite(RLED, HIGH);
					digitalWrite(GLED, LOW);
					continue;
				}
				digitalWrite(RLED, LOW);
				digitalWrite(GLED, LOW);
				if(distance < 100){
					digitalWrite(BUZZ, HIGH);
					delay(10);
					digitalWrite(BUZZ, LOW);
					delay(distance*2);
				}
				continue;
			}
			digitalWrite(RLED, LOW);
			digitalWrite(GLED, HIGH);

			if(distance < 100){
				digitalWrite(BUZZ, HIGH);
				delay(1);
				digitalWrite(BUZZ, LOW);
			}
		}
		digitalWrite(RLED, HIGH);
		digitalWrite(GLED, HIGH);
	}
	return 0;
}
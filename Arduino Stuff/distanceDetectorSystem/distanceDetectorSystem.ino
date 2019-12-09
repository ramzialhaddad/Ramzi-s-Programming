#define TRIG 7
#define ECHO 6
#define BUZZ 5
#define RLED 9
#define GLED 8

long duration;
int distance;

void setup() {
	pinMode(TRIG, OUTPUT);
	pinMode(ECHO, INPUT);
	pinMode(BUZZ, OUTPUT);
	pinMode(RLED, OUTPUT);
	pinMode(GLED, OUTPUT);

	digitalWrite(RLED, HIGH);
	digitalWrite(GLED, HIGH);

	// TRIG pin must start LOW
	digitalWrite(TRIG, LOW);
	delay(30);
	Serial.begin(9600); // Starts the serial communication
}

int getCM(){
	digitalWrite(TRIG, LOW);
	delayMicroseconds(2);
	// Sets the trigPin on HIGH state for 10 micro seconds
	digitalWrite(TRIG, HIGH);
	delayMicroseconds(10);
	digitalWrite(TRIG, LOW);
	// Reads the echoPin, returns the sound wave travel time in microseconds
	duration = pulseIn(ECHO, HIGH);
	// Calculating the distance
	return duration*0.034/2;
}

void loop() {
	distance = getCM();
	Serial.println(distance);

	if(distance > 0){
		if(distance > 3){
			if(distance > 30){
				//Do green
				digitalWrite(RLED, HIGH);
				digitalWrite(GLED, LOW);
				return;
			}
			//Do yellow bep bep bep bep bep bep
			digitalWrite(RLED, LOW);
			digitalWrite(GLED, LOW);
			if(distance < 100){
				digitalWrite(BUZZ, HIGH);
				delay(10);
				digitalWrite(BUZZ, LOW);
				delay(distance*2);
			}
			return;	
		}
		//Do red BEEEEEEEEEEEEEEEEEEEp
		digitalWrite(RLED, LOW);
		digitalWrite(GLED, HIGH);
		if(distance < 100){
			digitalWrite(BUZZ, HIGH);
			delay(1);
			digitalWrite(BUZZ, LOW);
			//delay(1);
		}
	}

	digitalWrite(RLED, HIGH);
	digitalWrite(GLED, HIGH);
}

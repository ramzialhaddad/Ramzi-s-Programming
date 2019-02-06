int dataPin = 2;
int clockPin = 3;
int latchPin = 4;

byte data = 0;

void setup() {
	pinMode(dataPin, OUTPUT);
	pinMode(clockPin, OUTPUT);
	pinMode(latchPin, OUTPUT);
}

void loop() {
	increment(100);
	//------------------------\\
	delay(2000);
	oneByOne(20);
	oneByOne(20);
	oneByOne(20);
	oneByOne(20);
	//------------------------\\
	delay(2000);
	for(int x = 50; x >=0;x=x-5){
		oneByOne(x);
	}
	//------------------------\\
	delay(2000);
	oneByOne(100);
	oneByOne(100);
	//------------------------\\
	delay(2000);
	for(int x = 50; x >=0;x=x-5){
		increment(x);
	}
	//------------------------\\
	delay(2000);
	for(int x = 50; x >=0;x=x-5){
		oneByOne(x);
	}
	//------------------------\\
	delay(2000);
	increment(100);
	delay(2000);
}

void shiftWrite(int pin, boolean state){
	bitWrite(data, pin, state);
	shiftOut(dataPin, clockPin, MSBFIRST, data);
	digitalWrite(latchPin, HIGH);
	digitalWrite(latchPin, LOW);	
}

void increment(int Delay){
	int pinNum = 0;
	//int Delay = 100;

	for (pinNum = 0; pinNum < 8; pinNum++){
		shiftWrite(pinNum, HIGH);
		delay(Delay);
	}

	for (pinNum = 7; pinNum >= 0; pinNum--){
		shiftWrite(pinNum, LOW);
		delay(Delay);
	}
}

void oneByOne(int Delay){
	int pinNum = 0;
	//int Delay = 20;

	for (pinNum = 0; pinNum < 8; pinNum++){
		shiftWrite(pinNum, HIGH);
		delay(Delay);
		shiftWrite(pinNum, LOW);
	}

	for (pinNum = 7; pinNum >= 0; pinNum--){
		shiftWrite(pinNum, HIGH);
		delay(Delay);
		shiftWrite(pinNum, LOW);
	}
}








import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12
LED = 11

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,0)

time.sleep(0.1)

print "Starting Measurement..."
try:
	while True:

		time.sleep(0.1)

		GPIO.output(TRIG,1)
		time.sleep(0.00001)
		GPIO.output(TRIG,0)

		while GPIO.input(ECHO) == 0:
			pass
		start = time.time()

		while GPIO.input(ECHO) == 1:
			pass
		stop = time.time()

		distance = (stop - start) * 17000

		print distance

		if distance < 20:
			GPIO.output(LED,1)
		else:
			GPIO.output(LED,0)

except KeyboardInterrupt:

	GPIO.cleanup()



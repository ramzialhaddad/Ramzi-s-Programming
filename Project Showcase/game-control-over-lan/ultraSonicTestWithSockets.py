import RPi.GPIO as GPIO
import time
import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '192.168.1.125'
PORT_NUMBER = 5000
SIZE = 1024
mySocket = socket( AF_INET, SOCK_DGRAM )

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
			myMessage = 'On'
		else:
			GPIO.output(LED,0)
			myMessage = 'Off'

		mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

except KeyboardInterrupt:

	GPIO.cleanup()
	sys.exit()



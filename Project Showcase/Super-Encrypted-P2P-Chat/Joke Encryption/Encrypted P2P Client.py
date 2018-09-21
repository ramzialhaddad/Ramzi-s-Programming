import time
import sys
import os
from socket import socket, AF_INET, SOCK_DGRAM

def encrypt(input):
	lenOfInput = len(input)
	ciph = ""

	for i in range(lenOfInput):
		let = input.lower()[i]
		if let == 'a':
			ciph += "8xUw6"
		if let == 'b':
			ciph += "9xjKo"
		if let == 'c':
			ciph += "jx78A"
		if let == 'd':
			ciph += "qx9Ud"
		if let == 'e':
			ciph += "5xCvs"
		if let == 'f':
			ciph += "ixIwl"
		if let == 'g':
			ciph += "sxDws"
		if let == 'h':
			ciph += "kx913"
		if let == 'i':
			ciph += "ox72s"
		if let == 'j':
			ciph += "fx2ws"
		if let == 'k':
			ciph += "sxsmy"
		if let == 'l':
			ciph += "2x2sq"
		if let == 'm':
			ciph += "lx8Cx"
		if let == 'n':
			ciph += "7x8q2"
		if let == 'o':
			ciph += "fxhqf"
		if let == 'p':
			ciph += "uxUs5"
		if let == 'q':
			ciph += "6xQwq"
		if let == 'r':
			ciph += "AxAab"
		if let == 's':
			ciph += "5xXk2"
		if let == 't':
			ciph += "ix7qk"
		if let == 'u':
			ciph += "9xyW3"
		if let == 'v':
			ciph += "2x52o"
		if let == 'w':
			ciph += "5xdss"
		if let == 'x':
			ciph += "Xxya5"
		if let == 'y':
			ciph += "uxos6"
		if let == 'z':
			ciph += "ox092"
		if let == ' ':
			ciph += "uq52k"
		if let == '>':
			ciph += "7Zdah"

	return ciph

SERVER_IP = str(input("What is the host ip? "))
name = str(input("What is your Nickname? "))
PORT_NUMBER = 5000
SIZE = 1024
mySocket = socket( AF_INET, SOCK_DGRAM )

while True:
	myMessage = name + ">> "
	myMessage = myMessage + input(">> ")
	myMessage = encrypt(myMessage)

	mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

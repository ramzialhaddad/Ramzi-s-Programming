from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import time
import os

PORT_NUMBER = 5000
SIZE = 1024

hostIP = gethostbyname(str(input("What is the host ip? ")))

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostIP, PORT_NUMBER) )

print("Test server listening on port {0}\n".format(PORT_NUMBER))

def decrypt(encryptedText):
	lenOfEncryptedText = len(encryptedText)
	deciph = ""

	def fiveLetterReceiver(encryptedText, amount):
		encryptedTextLetters = ""
		for y in range(5):
			encryptedTextLetters += (encryptedText[(y + amount)])
		return encryptedTextLetters

	count = 0

	for x in range(int(lenOfEncryptedText/5)):
		encryptedTextLetters = fiveLetterReceiver(encryptedText, (5 * count))

		if encryptedTextLetters == '8xUw6':
			deciph += "a"
		if encryptedTextLetters == '9xjKo':
			deciph += "b"
		if encryptedTextLetters == 'jx78A':
			deciph += "c"
		if encryptedTextLetters == 'qx9Ud':
			deciph += "d"
		if encryptedTextLetters == '5xCvs':
			deciph += "e"
		if encryptedTextLetters == 'ixIwl':
			deciph += "f"
		if encryptedTextLetters == 'sxDws':
			deciph += "g"
		if encryptedTextLetters == 'kx913':
			deciph += "h"
		if encryptedTextLetters == 'ox72s':
			deciph += "i"
		if encryptedTextLetters == 'fx2ws':
			deciph += "j"
		if encryptedTextLetters == 'sxsmy':
			deciph += "k"
		if encryptedTextLetters == '2x2sq':
			deciph += "l"
		if encryptedTextLetters == 'lx8Cx':
			deciph += "m"
		if encryptedTextLetters == '7x8q2':
			deciph += "n"
		if encryptedTextLetters == 'fxhqf':
			deciph += "o"
		if encryptedTextLetters == 'uxUs5':
			deciph += "p"
		if encryptedTextLetters == '6xQwq':
			deciph += "q"
		if encryptedTextLetters == 'AxAab':
			deciph += "r"
		if encryptedTextLetters == '5xXk2':
			deciph += "s"
		if encryptedTextLetters == 'ix7qk':
			deciph += "t"
		if encryptedTextLetters == '9xyW3':
			deciph += "u"
		if encryptedTextLetters == '2x52o':
			deciph += "v"
		if encryptedTextLetters == '5xdss':
			deciph += "w"
		if encryptedTextLetters == 'Xxya5':
			deciph += "x"
		if encryptedTextLetters == 'uxos6':
			deciph += "y"
		if encryptedTextLetters == 'ox092':
			deciph += "z"
		if encryptedTextLetters == "uq52k":
			deciph += " "
		if encryptedTextLetters == "7Zdah":
			deciph += ">"

		count += 1

	return deciph

while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        receivedText = data.decode('utf-8')
        print(decrypt(receivedText))
                
sys.ext()

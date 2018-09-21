import os

def encrypt():
	input = open("input.txt", 'r')
	input = input.read()
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

	print(ciph)
	output = open("output.txt", 'w')
	output.write(ciph)

def decrypt():
	input = open("output.txt", 'r')
	input = input.read()
	lenOfInput = len(input)
	deciph = ""
	print(input)
	print(lenOfInput)

	def fiveLetterReceiver(input, amount):
		inputLetters = ""
		for y in range(5):
			inputLetters += (input[(y + amount)])
		return inputLetters

	count = 0

	for x in range(int(lenOfInput/5)):
		inputLetters = fiveLetterReceiver(input, (5 * count))
		print(inputLetters)

		if inputLetters == '8xUw6':
			deciph += "a"
		if inputLetters == '9xjKo':
			deciph += "b"
		if inputLetters == 'jx78A':
			deciph += "c"
		if inputLetters == 'qx9Ud':
			deciph += "d"
		if inputLetters == '5xCvs':
			deciph += "e"
		if inputLetters == 'ixIwl':
			deciph += "f"
		if inputLetters == 'sxDws':
			deciph += "g"
		if inputLetters == 'kx913':
			deciph += "h"
		if inputLetters == 'ox72s':
			deciph += "i"
		if inputLetters == 'fx2ws':
			deciph += "j"
		if inputLetters == 'sxsmy':
			deciph += "k"
		if inputLetters == '2x2sq':
			deciph += "l"
		if inputLetters == 'lx8Cx':
			deciph += "m"
		if inputLetters == '7x8q2':
			deciph += "n"
		if inputLetters == 'fxhqf':
			deciph += "o"
		if inputLetters == 'uxUs5':
			deciph += "p"
		if inputLetters == '6xQwq':
			deciph += "q"
		if inputLetters == 'AxAab':
			deciph += "r"
		if inputLetters == '5xXk2':
			deciph += "s"
		if inputLetters == 'ix7qk':
			deciph += "t"
		if inputLetters == '9xyW':
			deciph += "u"
		if inputLetters == '2x52o':
			deciph += "v"
		if inputLetters == '5xdss':
			deciph += "w"
		if inputLetters == 'Xxya':
			deciph += "x"
		if inputLetters == 'uxos6':
			deciph += "y"
		if inputLetters == 'ox092':
			deciph += "z"
		if inputLetters == "uq52k":
			deciph += " "

		count += 1

	print(deciph)

		

def main():
	print("What would you like to do?")
	print("1.Encrypt Message")
	print("2.Decrypt Message")

	choice = input()
	if choice == 1 or choice == "1" or choice == "Encrypt Message" or choice == "encrypt" or choice == "Encrypt":
		encrypt()
	if choice == 2 or choice == "2" or choice == "Decrypt Message" or choice == "decrypt" or choice == "Decrypt":
		decrypt()

main()

import numpy as np

def peeka():
	inputText = input("Please input text to hide message inside:\n")

	seed = np.random.randint(10000000)
	np.random.seed(seed)
	print("Your seed is {}\nIf you forget this the message is useless.".format(seed))

	message = input("Type message you want to hide in the text:\n")

	inputTextList = list(inputText)
	length = len(inputTextList) -1

	for letter in message:
		inputTextList[np.random.randint(length)] = letter

	inputTextList[np.random.randint(length)] = '|'

	outputText = "".join(inputTextList)
	print("\n{}".format(outputText))
	input("\nPress enter to exit")

def boo():
	seed = int(input("Input seed:\n"))
	np.random.seed(seed)
	message = input("Input message:\n")
	hiddenMessageList = []

	length = len(message) -1
	while True:
		hiddenLetter = message[np.random.randint(length)]

		if hiddenLetter == '|':
			break
		else:
			hiddenMessageList.append(hiddenLetter)

	hiddenMessage = "".join(hiddenMessageList)
	print("\n{}".format(hiddenMessage))
	input()

choice = input("Hide message: 0\nReveal Message: 1\n")
if choice == '0':
	peeka()
elif choice == '1':
	boo()
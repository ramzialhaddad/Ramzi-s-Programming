import time
from pysine import sine

unit = 100
frequency = 1000

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabetValue = [ 
[1,0,3,0,0,0],
[3,0,1,0,1,0,1,0,0,0],
[3,0,1,0,3,0,1,0,0,0],
[3,0,1,0,1,0,0,0],
[1,0,0,0],
[1,0,1,0,3,0,1,0,0,0],
[3,0,3,0,1,0,0,0],
[1,0,1,0,1,0,1,0,0,0],
[1,0,1,0,0,0],
[1,0,3,0,3,0,3,0,0,0],
[3,0,1,0,3,0,0,0],
[1,0,3,0,1,0,1,0,0,0],
[3,0,3,0,0,0],
[3,0,1,0,0,0],
[3,0,3,0,3,0,0,0],
[1,0,3,0,3,0,1,0,0,0],
[3,0,3,0,1,0,3,0,0,0],
[1,0,3,0,1,0,0,0],
[1,0,1,0,1,0,0,0],
[3,0,0,0],
[1,0,1,0,3,0,0,0],
[1,0,1,0,1,0,3,0,0,0],
[1,0,3,0,3,0,0,0],
[3,0,1,0,1,0,3,0,0,0],
[3,0,1,0,3,0,3,0,0,0],
[3,0,3,0,1,0,1,0,0,0] ]

while True:
	print("\n")
	userInput = input("Heyo, type something to translate to morse code!!\n")

	for c in userInput:
		alphaIndex = alphabet.index(c)
		i = 0
		for x in alphabetValue[alphaIndex]:
			if alphabetValue[alphaIndex][i] == 0:
				time.sleep((unit*3)/1000)
			else:
				if alphabetValue[alphaIndex][i] == 1:
					print(".", end="")
				else:
					print("-", end="")
				sine(frequency, (unit*alphabetValue[alphaIndex][i])/1000)
			i += 1
import csv
from os import system as s
from sound import playsound
from random import randint as r

def main():
	def readCSV():
		fileName='thoughts.csv'
		with open(fileName) as csvfile:
			readCSV = csv.reader(csvfile, delimiter='\n')
			finished=[]
			for row in readCSV:
				finished.append(row)
		return finished

	while True:
		file = readCSV()
		randIndex = r(0, (len(file)-1))
		s('cls')
		if input("Do you want to think some more? ") == "y":
			print(file[randIndex][0])
			playsound("music.mp3")

main()
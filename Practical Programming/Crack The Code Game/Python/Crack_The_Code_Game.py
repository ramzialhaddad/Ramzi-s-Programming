"""
(c) Ramzi Al Haddad 2002-2018

Crack the Code Game v0.04

Game Layout, Documentation and Notes

- Choose a random number from 0 to 9 for each of the 3 combination numbers of the lock

- Choose numbers that are not from the chosen 'key' numbers that will be used for the hint boxes

- There are 5 text hints with numbers that correspond to them and they are as listed
    - One number is correct and well placed
    - One number is correct but wrong placed
    - Two numbers are correct but wrong placed
    - Nothing is correct
    - One number is correct but wrong placed

- There are 5 "random" layouts and placements for the hints to make the game more "random". They are determined via randomly generated numbers ranging
    from 0 to 4, thus 5 outcomes that could happen.

- Hopefully, later I can figure out an intelligent solution to keep the indexes and numbers the same throughout in order to make the game playable.

- Of course you can see that there are required inputs for the key this is to future proof the code and not hard code certain aspects that will prevent
    the code from being bad (I can't think of the proper word at the current time)

- The next steps are going to polish the game more and when we reach around v0.5, I think that a proper GUI will be implemented to make the game modern,
    but that is until we get there (and I'm not sure if I'm going to continue this project until then especially with IB on my hands)

"""

import random # For our random numnber generation
from os import system # To clear the console
from time import sleep

def main(magic):

    def keyNumberGeneration(keyLength): # Lets start with our key number generation
        key = []

        while True:
            if len(key) == keyLength:
                break
            else:
                randomNumber = random.randint(0,9)

                if randomNumber not in key:
                    key.append(randomNumber)

        return key

    def invalidNumbers(key, length):
        invalidNumbers = []

        while True:
            if len(invalidNumbers) == 3:
                break
            else:
                randomNumber = random.randint(0,9)

                if randomNumber not in key and randomNumber not in invalidNumbers:
                    invalidNumbers.append(randomNumber)

        return invalidNumbers

    def gameGeneration():

        def a():
            key = keyNumberGeneration(3)
            invalidNumber = invalidNumbers(key, 3)
            attempt = []

            while attempt != key:
                system("cls")

                print([key[0]], [invalidNumber[2]], [invalidNumber[0]], "One number is correct and well placed")
                print([invalidNumber[1]], [invalidNumber[0]], [invalidNumber[2]], "Nothing is correct")
                print([invalidNumber[0]], [key[0]], [invalidNumber[2]], "One number is correct but wrong placed")
                print([key[1]], [key[2]], [invalidNumber[0]], "Two numbers are correct but wrong placed")
                print([invalidNumber[1]], [invalidNumber[2]], [key[0]], "One number is correct but wrong placed")
                print("\n")
                
                attemptRaw = str(input())

                attempt = [int(attemptRaw[0]), int(attemptRaw[1]), int(attemptRaw[2])]

        def b():
            key = keyNumberGeneration(3)
            invalidNumber = invalidNumbers(key, 3)
            attempt = []

            while attempt != key:
                system("cls")

                print([invalidNumber[1]], [invalidNumber[0]], [invalidNumber[2]], "Nothing is correct")
                print([invalidNumber[0]], [key[0]], [invalidNumber[2]], "One number is correct but wrong placed")
                print([invalidNumber[1]], [invalidNumber[2]], [key[2]], "One number is correct and well placed")
                print([key[1]], [key[2]], [invalidNumber[0]], "Two numbers are correct but wrong placed")
                print([invalidNumber[1]], [key[0]], [invalidNumber[2]], "One number is correct but wrong placed")
                print("\n")
                
                attemptRaw = str(input())

                attempt = [int(attemptRaw[0]), int(attemptRaw[1]), int(attemptRaw[2])]

        def c():
            key = keyNumberGeneration()
            invalidNumber = invalidNumbers(key, 3)
            attempt = []

            while attempt != key:
                system("cls")

                print([invalidNumber[0]], [key[2]], [key[0]], "Two numbers are correct but wrong placed")
                print([key[0]], [invalidNumber[2]], [invalidNumber[0]], "One number is correct and well placed")
                print([invalidNumber[1]], [invalidNumber[0]], [invalidNumber[2]], "Nothing is correct")
                print([invalidNumber[0]], [key[2]], [invalidNumber[2]], "One number is correct but wrong placed")
                print([invalidNumber[1]], [invalidNumber[2]], [key[0]], "One number is correct but wrong placed")
                print("\n")
                
                attemptRaw = str(input())

                attempt = [int(attemptRaw[0]), int(attemptRaw[1]), int(attemptRaw[2])]

        def d():
            key = keyNumberGeneration()
            invalidNumber = invalidNumbers(key, 3)
            attempt = []

            while attempt != key:
                system("cls")

                print([key[2]], [invalidNumber[2]], [invalidNumber[1]], "One number is correct but wrong placed")
                print([key[0]], [invalidNumber[2]], [invalidNumber[0]], "One number is correct and well placed")
                print([invalidNumber[1]], [invalidNumber[0]], [invalidNumber[2]], "Nothing is correct")
                print([invalidNumber[0]], [key[0]], [invalidNumber[2]], "One number is correct but wrong placed")
                print([key[1]], [key[2]], [invalidNumber[0]], "Two numbers are correct but wrong placed")
                print("\n")
                
                attemptRaw = str(input())

                attempt = [int(attemptRaw[0]), int(attemptRaw[1]), int(attemptRaw[2])]

        def e():
            key = keyNumberGeneration(3)
            invalidNumber = invalidNumbers(key, 3)
            attempt = []

            while attempt != key:
                system("cls")

                print([key[0]], [invalidNumber[2]], [invalidNumber[0]], "One number is correct and well placed")
                print([invalidNumber[1]], [invalidNumber[0]], [invalidNumber[2]], "Nothing is correct")
                print([invalidNumber[0]], [key[0]], [invalidNumber[2]], "One number is correct but wrong placed")
                print([key[1]], [invalidNumber[1]], [key[0]], "Two numbers are correct but wrong placed")
                print([invalidNumber[1]], [invalidNumber[2]], [key[0]], "One number is correct but wrong placed")
                print("\n")
                
                attemptRaw = str(input())

                attempt = [int(attemptRaw[0]), int(attemptRaw[1]), int(attemptRaw[2])]

        randomChosen = random.randint(0, 4)

        if randomChosen == 0:
            a()
        elif randomChosen == 1:
            b()
        elif randomChosen == 2:
            c()
        elif randomChosen == 3:
            d()
        elif randomChosen == 4:
            e()
            

    gameGeneration()    

main("Computer Magic")
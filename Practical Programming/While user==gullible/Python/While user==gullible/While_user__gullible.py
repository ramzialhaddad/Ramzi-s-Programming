userInput = None
counter = 0

while userInput != 5 and counter != 10:
    print("Enter any number other than 5!")
    userInput = int(input())
    counter = counter + 1

if counter == 10:
    print("Wow, you're more patient then I am, you win.")
else:
    print("Hey! you weren't supposed to enter 5!")

input()

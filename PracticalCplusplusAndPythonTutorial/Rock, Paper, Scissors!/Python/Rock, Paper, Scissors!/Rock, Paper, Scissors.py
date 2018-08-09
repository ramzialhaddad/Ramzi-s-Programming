import random

humanWins = 0
computerWins = 0

choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock, Paper and Scissors")

while True:
    print("Human Wins: {}".format(humanWins))
    print("Computer Wins: {}".format(computerWins))

    userChoice = str(input("Type your choice (Rock, Paper or Scissors): "))
    computerChoice = choices[random.randint(0,2)]

    #Draws
    if userChoice == "Rock" and computerChoice == "Rock":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Draw")
        input()
    elif userChoice == "Paper" and computerChoice == "Paper":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Draw")
        input()
    elif userChoice == "Scissors" and computerChoice == "Scissors":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Draw")
        input()

    # Rock and Paper
    elif userChoice == "Rock" and computerChoice == "Paper":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Computer Win!")
        computerWins += 1
        input()
    elif userChoice == "Paper" and computerChoice == "Rock":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Human Win!")
        humanWins += 1
        input()

    #Paper and Scissors
    elif userChoice == "Paper" and computerChoice == "Scissors":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Computer Win!")
        computerWins += 1
        input()
    elif userChoice == "Scissors" and computerChoice == "Paper":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Human Win!")
        humanWins += 1
        input()

    #Rock and Scissors
    elif userChoice == "Rock" and computerChoice == "Scissors":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Human Win!")
        humanWins += 1
        input()
    elif userChoice == "Scissors" and computerChoice == "Rock":
        print("Human: ", userChoice)
        print("Computer: ", computerChoice)
        print("Computer Win!")
        computerWins += 1
        input()
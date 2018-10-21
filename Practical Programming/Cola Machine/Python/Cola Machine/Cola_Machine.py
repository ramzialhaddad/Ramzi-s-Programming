from time import sleep

print("Hello and Welcome to this non-existent Vending Machine!")

sleep(2)

print("Choose your beverage!\n")

print("1. Pepsi")
print("2. Coke")
print("3. Sprite")
print("4. 7-up")
print("5. Milk")

choice = int(input())

if choice == 1:
    print("You chose Pepsi!")
    sleep(2)

elif choice == 2:
    print("You chose Coke!")
    sleep(2)

elif choice == 3:
    print("You chose Sprite!")
    sleep(2)

elif choice == 4:
    print("You chose 7-up!")
    sleep(2)

elif choice == 5:
    print("You chose Milk!")
    sleep(2)

else:
    print("Hey, that was not vaild!")
    sleep(1)
    print("Here is your money back!")
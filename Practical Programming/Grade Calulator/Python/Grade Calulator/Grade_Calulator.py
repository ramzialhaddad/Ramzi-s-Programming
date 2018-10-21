import time

grade = 0

print("Hello Teacher!")

time.sleep(2)

print("Please Input the student's grade!")
grade = int(input())

if grade >= 0 and grade <= 59:
    print("Your Grade is a F, from a mark of {}".format(grade))
    input()

elif grade >= 60 and grade <= 69:
    print("Your Grade is a D, from a mark of {}".format(grade))
    input()

elif grade >= 70 and grade <= 79:
    print("Your Grade is a C, from a mark of {}".format(grade))
    input()

elif grade >= 80 and grade <= 89:
    print("Your Grade is a B, from a mark of {}".format(grade))
    input()

elif grade >= 90 and grade <= 100:
    if grade == 100:
        print("You got a perfect scrore of 100!")
        input()
    else:
        print("Your Grade is an A, from a mark of {}".format(grade))
        input()

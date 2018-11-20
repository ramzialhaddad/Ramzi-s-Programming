# n Value from https://asecuritysite.com/encryption/prime
g = 5
n = 6168960

from random import randint

b = randint(0,100000000)
gb = g^b
print("gb is {}".format(gb))

ga = int(input("Input ga from the other client:\n"))

sharedSecret = (ga^b)%n

print("Shared Secret is {}".format(sharedSecret))
input()
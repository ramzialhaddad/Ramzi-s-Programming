# n Value from https://asecuritysite.com/encryption/prime
g = 5
n = 6168960

from random import randint

a = randint(0,100000000)
ga = g^a
print("ga is {}".format(ga))

gb = int(input("Input gb from the other client:\n"))

sharedSecret = (gb^a)%n

print("Shared Secret is {}".format(sharedSecret))
input()
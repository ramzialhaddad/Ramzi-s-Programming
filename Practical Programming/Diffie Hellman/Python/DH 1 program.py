# n Value from https://asecuritysite.com/encryption/prime
g = 5
n = 6168960

import random

a = random.randint(0,100000000)
ga = g^a

b = random.randint(0,100000000)
gb = g^b

gab = (gb^a)%n
gba = (ga^b)%n

print(gab, gba)
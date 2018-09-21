import time
from directKeys import PressKey, ReleaseKey, W, A, S, D, f2

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


PressKey(W)
time.sleep(2)
ReleaseKey(W)

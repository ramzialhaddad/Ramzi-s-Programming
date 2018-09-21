import time
import pyautogui
import sys
amount = int(sys.argv[1])
time.sleep(3)
for x in range(amount):
    pyautogui.click(button='left')
    pyautogui.click(button='left')

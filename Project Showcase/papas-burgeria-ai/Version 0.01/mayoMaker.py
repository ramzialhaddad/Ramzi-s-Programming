import pyautogui as pag
import time

def Mayo():
    time.sleep(.75)
    mayoBottleLocation = pag.locateOnScreen('mayoBottle.PNG')
    mayoX, mayoY = pag.center(mayoBottleLocation)
    pag.moveTo(mayoX, mayoY)
    pag.dragTo(859, 241, button = 'left')

while True:
    Mayo()

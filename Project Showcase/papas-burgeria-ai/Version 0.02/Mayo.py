import pyautogui as pag
import time

time.sleep(3)
pag.alert(text = 'Hover just over the top of the flash game for a few seconds', button = 'OK')
time.sleep(7)
mouseX, mouseY = pag.position()
pag.alert(text = 'Mouse Position Captured', button = 'OK')
time.sleep(7)
pag.alert(text = 'Switch to window of game and wait for mayo', button = 'OK')

def Mayo():
    time.sleep(.75)
    mayoBottleLocation = pag.locateOnScreen('mayoBottom.PNG')
    mayoX, mayoY = pag.center(mayoBottleLocation)
    pag.moveTo(mayoX, mayoY)
    pag.dragTo(mouseX, mouseY, button = 'left')

while True:
    Mayo()

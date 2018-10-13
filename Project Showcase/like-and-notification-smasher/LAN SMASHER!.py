import pyautogui as p
import autopy as a
from sound import playsound
from time import sleep

def main():

	def moveMouse():
		constThing = 128
		for y in range(int((a.screen.size()[1])/constThing)):
			for x in range(int((a.screen.size()[0])/constThing)):
				a.mouse.smooth_move(x*constThing,y*constThing, duration = 0.01)

	def verifyStart():
		return p.confirm(text="Do you have a video open that you want to SMASH the Like and Notification Button?", buttons=["Yes", "No"])

	def findLikeAndNotification(theme, type):
		if theme == "light" or theme == "1" or theme == "l":
			if type==0:
				likePosition = p.locateOnScreen('likeLight.png')
				notificationPosition = p.locateOnScreen('bellLight.png')
			elif type==1:
				likePosition = p.locateOnScreen('likeLightAlt.png')
				notificationPosition = p.locateOnScreen('bellLightAlt.png')
			else:
				raise Exception("image type is not valid")
		elif theme == "dark" or theme == "2" or theme == "d":
			if type == 0:
				likePosition = p.locateOnScreen('likeDark.png')
				notificationPosition = p.locateOnScreen('bellDark.png')
			elif type == 1:
				likePosition = p.locateOnScreen('likeDarkAlt.png')
				notificationPosition = p.locateOnScreen('bellDarkAlt.png')
			else:
				raise Exception("image type is not valid")
		else:
			raise Exception('theme is not "dark" or "light"')

		return likePosition, notificationPosition

	if verifyStart() == "Yes":
		a.alert.alert("To ensure maximum epicness, please hover your mouse over the like button, then press enter")
		mouseLikeX, mouseLikeY = p.position()
		a.alert.alert("Now over the notifcation button, then press enter")
		mouseNotificationX, mouseNotificationY = p.position()
		theme = input("Are you using light or dark theme youtube?\n1.light\n2.dark\n")
		a.alert.alert("Scanning Screen...")
		moveMouse()
		sleep(0.5)
		likePosition, notificationPosition = findLikeAndNotification(theme,0)
		if likePosition==None or notificationPosition==None:
			likePosition, notificationPosition = findLikeAndNotification(theme, 1)
			if likePosition==None or notificationPosition==None:
				# This block executes if photo recognition didn't work at all, and it is using the mouse positions previously captured
				print(likePosition, notificationPosition)
				likeX, likeY = p.center(likePosition)
				notificationX, notificationY = p.center(notificationPosition)
				print(likeX, likeY)
				print(notificationX, notificationY)

				a.mouse.smooth_move(likeX, likeY)
				playsound('bass.wav')
				p.click()
				a.mouse.smooth_move(notificationX, notificationY)
				p.click()
				playsound("bass.wav")
				a.alert.alert("Buttons have been SMASHED!")
			# If this else block executes means that the first photos didn't work and the program tried to use the alternative photos
			else:
				print(likePosition, notificationPosition)
				likeX, likeY = p.center(likePosition)
				notificationX, notificationY = p.center(notificationPosition)
				print(likeX, likeY)
				print(notificationX, notificationY)

				a.mouse.smooth_move(likeX, likeY)
				playsound('bass.wav')
				p.click()
				a.mouse.smooth_move(notificationX, notificationY)
				p.click()
				playsound("bass.wav")
				a.alert.alert("Buttons have been SMASHED!")
		# If this else block executes means that the photo position recognition worked the first time!
		else:
			print(likePosition, notificationPosition)
			likeX, likeY = p.center(likePosition)
			notificationX, notificationY = p.center(notificationPosition)
			print(likeX, likeY)
			print(notificationX, notificationY)

			a.mouse.smooth_move(likeX, likeY)
			playsound('bass.wav')
			p.click()
			a.mouse.smooth_move(notificationX, notificationY)
			p.click()
			playsound("bass.wav")
			a.alert.alert("Buttons have been SMASHED!")
	else:
		a.alert.alert("WELL THEN GO OPEN UP A VIDEO THAT YOU WANT TO SMASH THE LIKE AND NOTIFICATION BUTTONS!")


main()
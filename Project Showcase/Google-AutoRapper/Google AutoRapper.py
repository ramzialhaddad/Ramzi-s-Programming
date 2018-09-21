from json import loads
from gtts import gTTS
import urllib.request
import time
import random

link = "http://suggestqueries.google.com/complete/search?client=firefox&q="
rap = ""

def editLinkWithUserInput(link):
    magicWord = str(input("What do you want your starting words to be? "))
    if " " in magicWord:
        magicWord = magicWord.replace(" ", "%20")
    return link + magicWord

def editLink(link, results):
    index = random.randint(0,len(results))-1
    print(index)
    wordChoice = results[index]
    if " " in wordChoice:
        wordChoice = wordChoice.replace(" ", "%20")
    return link + wordChoice, index

editedLink = editLinkWithUserInput(link)

while True:
    response = urllib.request.urlopen(editedLink)
    results = loads((response.read()).decode("utf-8"))[1]
    print(results)
    editedLink, indexOfPhrase = editLink(link, results)
    rap += " " + results[indexOfPhrase]
    print(rap)
    userInput = int(input("Do you want to continue or change the magic word? 0 for no, 1 yes, 2 for change? "))
    if userInput == 0:
        break
    elif userInput == 1:
        editedLink, indexOfPhrase = editLink(link, results)
        
    elif userInput == 2:
        editedLink = editLinkWithUserInput(link)

tts = gTTS(text=rap, lang='en', slow=False)
tts.save("Google Rap.mp3")
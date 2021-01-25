import pyttsx3
import time

speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
rate = speaker.getProperty("rate")
speaker.setProperty( "rate",170) 
while True:
    value = input("Enter your text: \n")
    if value == "!exit":
        exit()
    print(time.strftime("%H:%M"),value)
    speaker.say(value)
    speaker.runAndWait()
    



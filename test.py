from gtts import gTTS #need internet connection
import os
from playsound import playsound #use playsound==1.2.2 package

def speak(text):
    tts = gTTS(text=text, tld='com.vn', lang='vi')
    os.remove("voice.mp3")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)

speak(">")
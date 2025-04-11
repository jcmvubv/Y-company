# Importing the required libraries

import speech_recognition as sr
import datetime
import subprocess
import pyttsx3
import webbrowser

# Intiating the engines for performing text to speech and speech to text

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()
print("Conversation with Cilia")

# Declaring the function for recognizing the voices using speech_recognition library.

def bot() -> str:
    global text
    with sr.Microphone() as source:
        print("Clearing background noises ...... please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ask me anything ... ")
        print("------------------------------------------")
        recordedAudio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recordedAudio, language='en_US')
        text = text.lower()
        print('Me: ', format(text))
    except Exception as ex:
        print(ex)

# Inserting the commands to your voice assistant and logics building

    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%m %p')
        print('Cilia: '+ time)
        engine.say('Sure the time is '+time)
        engine.runAndWait()
    elif 'google' in text:
        a = 'opening Google .....'
        print("Cilia:" + a)
        engine.say(a)
        # Add a URL of Google to open it in a browser
        url = 'https://www.google.com/'
        # Open the URL using open() function of module
        webbrowser.open(url, new=0, autoraise=True)
        engine.runAndWait()
    elif 'youtube' in text:
        a = 'opening Youtube .....'
        print("Cilia:" + a)
        engine.say(a)
        # Add a URL of youtube to open it in a browser
        url = 'https://www.youtube.com/'
        # Open the URL using open() function of module
        webbrowser.open(url, new=0, autoraise=True)
        engine.runAndWait()
        
    elif 'whatsapp' in text:
        a = 'opening Whatsapp .....'
        print("Cilia:" + a)
        engine.say(a)
        # Add a URL of youtube to open it in a browser
        url = 'https://web.whatsapp.com/'
        # Open the URL using open() function of module
        webbrowser.open(url, new=0, autoraise=True)
        engine.runAndWait()
        

    elif 'hi' in text:
        n = 'hi yousef,how are you?'
        print("Cilia:" + n)
        engine.say(n)
        engine.runAndWait()
    else:
        c = "I can't hear you."
        print("Cilia:" + c)
        engine.say(c)
        engine.runAndWait()

while True:
    bot()


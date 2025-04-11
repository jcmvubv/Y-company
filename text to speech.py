from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'Convert this Text to Speech in Python'
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 
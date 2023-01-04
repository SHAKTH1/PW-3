from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'YOUR EXAM WILL CONTAIN 10 QUESTIONS IN TOTAL. YOUR ENTIRE EXAM WILL BE TIMED. ONCE THE QUESTION IS READ YOU CAN START TELLING YOUR ANSWER. PRESS SPACE TO CONTINUE'
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 




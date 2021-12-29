import pyttsx3 
#convert text into speech
import speech_recognition as sr
#recognize the user speech
import datetime
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
 hour=int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
     speak("Good Morning!")
 elif hour>12 and hour<12:
         speak("Good Afternoon!")
 else:
     speak('I am Unesh.How can I help you Man')
def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshould=0.5
        audio=r.listen(source)
    try:
      print("Recognizing...")
      query=r.recognize_google(audio,Language='en-in')
      print(f"User said:{query}\n")
    except Exception as e:
       print("can you say that again please....")
       return "None"
    return query
if_name=="main_":
    

speak("hello Suraj")
wishMe()
takeCommand()
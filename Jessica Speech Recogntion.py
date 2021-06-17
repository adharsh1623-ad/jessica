import speech_recognition as sr # speech recogntion
import webbrowser #for web browser
import os
from gtts import gTTS #google-text-to-speech
import inltk #if we need to use any indian language
import datetime#for date and time
import nltk #this is natural language proccesing
import random
import pyttsx3
import playsound#for playing sound
import time
import torch
import json
from geopy.geocoders import Nominatim
import geocoder
import pyjokes#for some fun
import ibm_watson #importing ibm watson 
from twilio.rest import Client #for sending messages in case of emergency
from ibm_watson import SpeechToTextV1 #by using ibm services using speech-to-text
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator #for authenticating the IBM id,apikey,url,password
from ibm_cloud_sdk_core import ApiException #for reduce any ecxeption errors 

def speak(audio): 
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[0].id')
    engine.say(text)
    engine.runAndWait()

api=IAMAuthenticator("API key") #authenticating the API key
    speech_to_text = SpeechToTextV1(authenticator=api)
    speech_to_text.set_service_url="URL" #speech-to-text URL
    r = sr.Recognizer() #the recognizer 
apikey="API key" #Api key
def record_audio(ask = False): 
    with sr.Microphone() as source: # using microphone to capture the sound or audio
        print("listening");
        r.adjust_for_ambient_noise(source) #to reduce background noise
        if ask :
            print(ask);
        audio = r.listen(source ,phrase_time_limit=3);
        voice_data = ''
    try:
        voice_data = r.recognize_ibm(audio,username= 'Email',password='Password') #ibm recognizer 
        print(voice_data);
    except sr.UnknownValueError: # for unkonwn error or the audio is not understanble
        speak('i could not get it');
    except sr.RequestError: #for request error if the request is not found
        speak('sorry, please repeat it');
        return voice_data.lower()

r = sr.Recognizer() #the recognizer
def record_audio(ask = False): 
    with sr.Microphone() as source: # using microphone to capture the sound or audio
        print("listening");
        r.adjust_for_ambient_noise(source) #to reduce background noise
        if ask :
            print(ask);
        audio = r.listen(source,10,10);
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio); 
        print(voice_data);
    except sr.UnknownValueError: # for unkonwn error or the audio is not understanble
        speak('i could not get it');
    except sr.RequestError: #for request error if the request is not found
        speak('sorry, please repeat it');
    return voice_data.lower()

def wishMe(): #for wishing according to the time i.e good morning
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !") #good morning command
  
    elif hour>= 12 and hour<18:#good afternoon command
        speak("Good Afternoon !")  
  
    else:
        speak("Good Evening  !") #good evening command

def speak(audio_string): #to convert the captured file to mp3 and to save to the sysytem
    tts = gTTS(text=audio_string, lang='en')
    r=random.randint(1,2000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def tellDay():
    # it will return the day
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        Speak("The day is " + day_of_the_week)

def location():
    Nomi_locator = Nominatim(user_agent="My App")#initialize the Nominatim object
    location = Nomi_locator.reverse(f"{latitude}, {longitude}") #get the location
    my_location= geocoder.ip('me')
#my latitude and longitude coordinates
latitude= my_location.geojson['features'][0]['properties']['lat']
longitude = my_location.geojson['features'][0]['properties']['lng']


def Help_me(): # incase of emergrncy situation 
    account_sid = 'ACC-SID'  #this is account id 
    auth_token = 'Account TOKEN'  # this is accounts auth token 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(  
                              messaging_service_sid='MEssage sid', 
                              body=location(),      
                              to='+91************' 
                          ) 
    print(message.sid) #confirmation of the message sent 

def respond(voice_data):
    
    #general communication
    if 'hai' in voice_data:
        speak('my name is jessica'); 
        
     #for time   
    elif 'the time' in voice_data:
        strTime = datetime.datetime.now().strftime("%I:%M:%S")    
        speak(f" the time is {strTime}");
       
    #for general commands
    elif "what are you  jessica"  in voice_data:
        speak('Im  weak  A.I for your help , thanks for asking ');
     
    #greetings
    elif 'how are you' in voice_data:
        speak("I am fine, Thank you");
        speak(" by the way , How are you ");

        #general
    elif 'who are you' in voice_data:
        speak('i am jessica , who is your personal assistant');
        
     #for some fun and joke   
    elif 'joke' in voice_data:
        speak(pyjokes.get_joke())
        
     #for retriving the name jessica  
    elif 'what is your name' in voice_data:
        speak('my name is . jessica');
        
     #for search in web or internet   
    elif'search' in voice_data:
        search = record_audio('what do you want?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('here is what i found for :' + search)
        
       #in case of emergency 
    elif "help me" in voice_data:
        speak("don't panic help will be sent to you");
        Help_me()
        
time.sleep(1) #time to sleep after the execution of every executable statments
wishMe() #for wishing
speak('I am jessica, how may i help you ?')
while 1:
    voice_data = record_audio() #for retriving the data of the voice data that captured
    respond(voice_data) #for respond in captured voice data
    if 'exit'  in voice_data: #for exting the main loop 
        speak("Thanks for giving me your time") 
        break

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr # speech recogntion module
import webbrowser #for exploring web browser
import os 
from gtts import gTTS #google-text-to-sppech
import datetime # for importing time 
import nltk # for natural language processing
import random 
import pyttsx3 #for responding
import playsound
import time #for time 
import torch
import pyjokes
from twilio.rest import Client #for validating the twilio
from ibm_watson import SpeechToTextV1 #for accesing the ibm watson studio
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException #for any exception that occur while importing


# In[2]:


def speak(audio):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[0].id')
    engine.say(text)
    engine.runAndWait()


# In[3]:


api=IAMAuthenticator("99OfdJnQ4kKC-_SU48suO-6EX6ddAlKQVKYttg-xLU_O") #api key authenticator
speech_to_text = SpeechToTextV1(authenticator=api) #authenticator watson speech to text 
speech_to_text.set_service_url="https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/1af1e959-0d77-4df8-9088-8568b0b47903" #url watson speech to text 
r = sr.Recognizer() #reocgnizer
apikey="99OfdJnQ4kKC-_SU48suO-6EX6ddAlKQVKYttg-xLU_O" #api key
def record_audio(ask = False):  #for record the audio for responding the data
    with sr.Microphone() as source: #source
        print("listening");
        r.adjust_for_ambient_noise(source) #reduce background noise
        if ask :
            print(ask);
        audio = r.listen(source ,phrase_time_limit=3);
        voice_data = ''
    try:
        voice_data = r.recognize_ibm(audio,username= 'adharsh1623@gmail.com',password='AdhuAdhi@99') # recognizer ibm watson studio
        print(voice_data);
    except sr.UnknownValueError: # for unknown value other than respond()
        speak('i could not get it');
    except sr.RequestError:  #for request error that show it didnt get what wde are saying other than respond()
        speak('sorry, please repeat it');
        return voice_data.lower()


# In[4]:


#recognize what we are saying
r = sr.Recognizer() #reocgnizer
def record_audio(ask = False):  #for record the audio for responding the data 
    with sr.Microphone() as source: # for source for our speech
        print("listening");
        r.adjust_for_ambient_noise(source)  #for reducing background noise
        if ask :
            print(ask);
        audio = r.listen(source,5,5);
        voice_data = ''   # respond in voice 
    try:
        voice_data = r.recognize_google(audio); #google recogntioner
        print(voice_data);
    except sr.UnknownValueError: # for unknown value other than respond()
        speak('i could not get it');
    except sr.RequestError:  #for request error that show it didnt get what wde are saying
        speak('sorry, please repeat it');
    return voice_data.lower()


# In[5]:


def wishMe():
    #for wishes
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")  
  
    else:
        speak("Good Evening  !")


# In[6]:


def tellDay():
      
    # the weekday method is a method from datetime
    # library which helps us to an integer 
    # corresponding to the day of the week
    # this dictionary will help us to map the
    # integer with the day and we will check for
    # the condition and if the condition is true
    # it will return the day
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        Speak("The day is " + day_of_the_week)


# In[7]:


def Help_me():
    account_sid = ['AC41dd6a9f863fa8d1f5905728830d4958'] #twillio ussage id
    auth_token = ['d94dc71247c1051fb41d8c75077df949']#twillio ussage token 
    client = Client(account_sid, auth_token)
    message = client.messages.create( messaging_service_sid='MGbe3bc98fef5438977cc4004b6e64b399', body="please help me police,i'm in tragedy!", to='+918778593946' )
    print(message.sid)


# In[8]:


def respond(voice_data):
    #basic commands
    if 'hai' in voice_data:
        speak('my name is jessica'); 
        
        #for time 
    elif 'the time' in voice_data:
        strTime = datetime.datetime.now().strftime("%I:%M:%S")    
        speak(f" the time is {strTime}");
        
    elif "day" in voice_data:
        speak(tellDay());
        
      #for waking up twilio  
    elif "help me" in voice_data:
        speak("don't panic help will be sent to you");
        print(Help_me)
        
    elif "what are you  jessica"  in voice_data:
        speak('Im  weak  A.I for your help , thanks for asking ');
        
    elif 'how are you' in voice_data:
        speak("I am fine, Thank you");
        speak(" by the way , How are you ");

    elif 'who are you' in voice_data:
        speak('i am jessica , who is your personal assistant');
        
        #for joke
    elif 'joke' in voice_data:
        speak(pyjokes.get_joke())
        
    elif 'what is your name' in voice_data:
        speak('my name is . jessica');
        
        #for surfing internet  
    elif'search' in voice_data:
        search = record_audio('what do you want?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('here is what i found for :' + search)
        


# In[ ]:


time.sleep(1) #time to sleep after performing in any respond
speak('I am jessica, how may i help you ?') #greetings
wishMe() #wish when we start our program
while 1:
    voice_data = record_audio() #  to record for respond
    respond(voice_data) #for responding voice_data
    if 'exit'  in voice_data: #for exit the program
        speak("Thanks for giving me your time")
        break
    


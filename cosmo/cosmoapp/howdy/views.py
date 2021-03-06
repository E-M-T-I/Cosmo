from django.shortcuts import render
from django.views.generic import TemplateView
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

# home page
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# about page (example)
class AboutPageView(TemplateView):
    template_name = "about.html"


# global variable
r = sr.Recognizer()

# Speech recognition class (Voice)
class VoiceFeature(TemplateView):
    template_name = 'index.html'
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            alexis_speak(voice_data)
        except sr.UnknownValueError:
            alexis_speak('sorry, i did not get that')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')
        return voice_data  

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'    
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)    

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is ')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is location of ' + location)
    if 'exit' in voice_data:
        exit()    

time.sleep(1)
alexis_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)



                        






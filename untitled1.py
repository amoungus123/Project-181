# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:27:33 2023

@author: pulle
"""

from tkinter import*
import speech_recognition as sr
import webbrowser
import pyttsx3
from datatime import datatime


root = Tk()
root.geometry("500x500")
text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How can I help you?")
    speech_recognition= sr.Recognitzer()
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat, I did not get that.')
            speak('Please repeat, I did not get that.')
    respond(voice_data)
         
    
    def respond(voice_data):
        voice_data = voice_data.low()
        print(voice_data)
        if "name" in voice_data:
            speak("My name is Jarvis")
            print('My name is Jarvis')
            
        if "time" in voice_data:
            speak("Current Time is")
            now = datatime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(current_time)
            print(current_time
                  )


r_audio()
root.mainloop()
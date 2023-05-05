'''
Created by Vassilis Antonakakis on 17/10/2022
'''

import speech_recognition as sr
import pyttsx3
import webSearching
import stringManipulation
import tkinter as tk
import GraphicksMain

r = sr.Recognizer()
keyPhrase = "Hey assistant"
    

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def determineCommand(command):
    match command[0]:
        case "request":
            webSearching.internetSearch(command[1])
        
        case "define":
            webSearching.dictSearch(command[1])
        
        
        case _:
            print("Unknown command!")

counter = 0

while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2, phrase_time_limit=4)
            #print("Up and listening:")
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(f'{counter:d} Input: {MyText:45s}')
            
            counter += 1
            
            if(MyText == "terminate"): break;

            commandTokens = stringManipulation.commandParser(MyText)
            print(commandTokens[0])

            determineCommand(commandTokens)

            if((MyText.index(keyPhrase) == 0)):
                print("Did you say " + MyText)
                #SpeakText(MyText)
    except ValueError:
        print("valueError occoured")
    except:
        r = sr.Recognizer()   

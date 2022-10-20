from email.policy import default
from traceback import print_tb
import speech_recognition as sr
import pyttsx3
import webSearching
import stringManipulation

r = sr.Recognizer()
keyPhrase = "Hey assistant"

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def determineCommand(command):
    match command[0]:
        case "search":
            webSearching.internetSearch(command[1])
        case _:
            print("Unknown command!")

while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.8)

            audio2 = r.listen(source2, phrase_time_limit=2)
            MyText = r.recognize_google(audio2)
            print(MyText)
            MyText = MyText.lower()
            print("Input: " + MyText)

            if(MyText == "terminate"): break;

            commandTokens = stringManipulation.commandTokenizer(MyText)
            print(commandTokens[0])

            determineCommand(commandTokens)

            if((MyText.index(keyPhrase) == 0)):
                print("Did you say " + MyText)
                #SpeakText(MyText)
    except ValueError:
        print("valueError occoured")
    except:
        r = sr.Recognizer()
    
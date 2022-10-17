from traceback import print_tb
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
keyPhrase = "Hey assistant"

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.5)

            audio2 = r.listen(source2, phrase_time_limit=5)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Input: " + MyText)

            if(MyText == "end process"): break;
            
            if((MyText.index(keyPhrase) == 0)):
                print("Did you say " + MyText)
                #SpeakText(MyText)
    except ValueError:
        print("I didn't catch that...")
    except:
        r = sr.Recognizer()
    
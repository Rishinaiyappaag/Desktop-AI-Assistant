import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyaudio
from subprocess import call


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 00 and hour < 12:
        speak("Good Morning Rishin!!")
        print("Good Morning Rishin!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Rishin!!")
        print("Good Afternoon Rishin!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Rishin!!")
        print("Good Evening Rishin!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("ELSA at your service , please tell me how may I help you.")
    print("ELSA at your service , please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\RISHIN AYAPPA\\Pictures\\Screenshots")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"
        exit
    

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "hu r u" in query:
            speak("I'm JARVIS created by Mr. Rishin Aiyappa and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Rishin Aiyappa and I'm a desktop voice assistant.")

        elif "how r u" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif"open wikipedia" in query:
            wb.open("wikipedia.org") 

        elif"open calculator"  in query: 
            path="C:\\Users\\RISHIN AYAPPA\\Desktop\\Calculator -.lnk"
            os.startfile(path)


        elif "play music" in query:
            song_dir = "C:\\Users\\RISHIN AYAPPA\\Music"
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open images" in  query:
            imagePath="C:\\Users\\RISHIN AYAPPA\\Pictures\\Saved Pictures"  
            os.startfile(imagePath)
            speak(" Opening images")

        

        


        elif "open chrome" in query:
            chromePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "https://www.google.com/search?q=chrome+search&rlz=1C1ONGR_enIN1011IN1040&oq=chrome+search&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIHCAEQABiABDINCAIQABiDARixAxiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDk1ODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        elif "remember" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "what did i say to remember" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
            


        elif "shutdown" in query:
            quit()



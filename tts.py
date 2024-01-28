import datetime
import json
import os
import smtplib
import webbrowser
from urllib.request import urlopen

import cv2
import pyautogui
#m and key
import pyjokes
import pyttsx3
import pywhatkit as wk #yt
import speech_recognition as sr
import wikipedia
from win32com.server import exception

api_key = "617fba5afc4d424e61fe630ca41d84f8"
#weatherapi
engine = pyttsx3.init('sapi5')  # speech api jarvis le bolne tone ya stored huncha
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()  # recog lai call gar-ya
    with sr.Microphone() as source:
        print('I\'m listening..')
        r.pause_threshold = 1  # 1 sec samma bolena vane ni wait garcha sunna
        audio = r.listen(source)

    try:
        print("Recognizing the voice..")
        text = r.recognize_google(audio, language='en-US')
        print(f"user said :{text}\n")

    except exception as e:
        print("Could you please repeat that again.. ")
        return "none"
    return text


def Wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Eve!")

    speak("What can i do for you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()


    server.login('poodleles@gmail.com', 'ldds dceh vwkz yruk')
    server.sendmail('poodleles@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    Wish()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("Hello!")
            speak("Hello!")

        elif "what is" in query:
            speak("Searching wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif "who is" in query:
            speak("Searching wikipedia...")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'just open Google' in query:
            webbrowser.open("google.com")

        elif 'open google' in query:
            speak("What shall i search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif "just open youtube " in query:
            webbrowser.open("youtube.com")

        elif "open youtube" in query:
            speak("what shall i play?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube" , "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif "just open spotify" in query:
            webbrowser.open("spotify.com")

        elif "close browser" in query:
            os.system("taskkill /f /im msedge.exe")

        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")

        elif "open paint" in query:
            npath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\paint.lnk"
            os.startfile(npath)

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam",img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "maximize this window" in query:
            x, y = 100, 100

            width, height = 500, 500

            pyautogui.click(x, y)

            pyautogui.hotkey('win', 'up')

        elif 'email to travis' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "travis.ass23@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif 'news' in query:
            try:

                api_key = 'f2cb3f76064b4ec6b5f591c2ffd9a13d'

                url =f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f2cb3f76064b4ec6b5f591c2ffd9a13d"
                jsonObj = urlopen(url)
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top news from the selected source:')
                print(f'=============== times-of-india ============\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))







from PyPDF2 import pdf
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
import sys
from time import sleep
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import qrcode
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import smtplib,ssl  #pip install email 
import random
import wikipedia
import requests
from gtts import gTTS
from playsound import playsound
from display import change_wallpaper
from music import play_music, pause_music, stop_music, next_song, previous_song, play_specific_song
from internet_sp import InternetSpeed
from reminder import remind1
from temperature import temperature_info
from pdf_reader import pdf_handler
from speak_module import speak
from news_module import get_news
from qrcodeGenerator import qrCodeGenerator
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
import threading
engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
from requests import get
engine.setProperty('rate',180)
from twilio.rest import Client
account_sid = 'ACfaa783b83a202cb5674f8d5cf2784ec9'
auth_token = 'f3c9638deba9fc694e76dd6103d9d04a'



# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am jarvis") 
    else:
        speak("good evening sir i am jarvis")  

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        # R = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("listening.......")
        #     audio = R.listen(source)
            
        # try:
        #     print("Recognizing......")
        #     text = R.recognize_google(audio,language='en-in')
            
        #     print(">> ",text)
        # except Exception:
        #     speak("Sorry Speak Again")
        #     return "None"
        text=input("me: ")
        text = text.lower()
        return text
    def remind(self,s):
        t1=threading.Thread(target=self.reminder_start(s))
        t2=threading.Thread(target=self.STT())
        t2.start()
        t1.start()
        print("Reminder Set")
        speak("Reminder Set")
    def location(self):
        speak("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
            speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            speak("Sorry boss, due to network issue i am not able to find where we are.")
            pass
    def verifyMail(self):
        try:
            speak("what should I say?")
            content = self.STT()
            speak("To whom do u want to send the email?")
            to = self.STT()
            self.SendEmail(to,content)
            speak("Email has been sent to "+str(to))
        except Exception as e:
            print(e)
            speak("Sorry sir I am not \ able to send this email")
    
    #Email Sender
    def SendEmail(self,to,content):
        print(content)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("srujanpenta31@gmail.com","Srujan@3112")
        server.sendmail("srujanpenta31@gmail.com",to,content)
        server.close()
    def sending_text(self,msg, number):
        client = Client(account_sid, auth_token)
        number = "+91" + number
        client.messages \
            .create(
                body=msg,
                from_='+15734848925',
                to=number
            )
        speak("Message Sent to " + number)
    def reminder_set(self,s):
    # s = "Remind me to call Shivam at 10:00 on 21 July"
        ind1 = s.index('to')
        ind2 = re.search(r"at \d+:\d+", s)

        time = re.findall(r'\d+:\d+', s)
        msg = s[ind1+3:ind2.span()[0]]

        day = re.search(r'on \d+', s).span()[0]
        day_date = s[day+3:]

        return remind1(msg, day_date, time)
    def Clock_time(self):
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak("Current time is "+time)
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        speak("Today is "+day_of_the_week)
        return day_of_the_week
    def reminder_start(self,s):
        while True:
            status = self.reminder_set(s)
            if status:
                break
    def close_browser(self):
        os.system('pkill chrome')
    def JARVIS(self):
        wish()
            
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            elif "shutdown" in self.query:
                speak("Do you really want to shut down your pc Say Yes or else No")
                print("Say Yes or else No")
                ans_from_user=self.STT()
                if 'yes' in ans_from_user:
                    speak('Shutting Down...')
                    os.system('shutdown -s') 
                elif 'no' in ans_from_user:
                    speak('shutdown abort Speak Again')
                    self.STT()
            elif "location" in self.query:
                self.location()
            elif "send email" in self.query:
                self.verifyMail()
            elif "wikipedia" in self.query:
                speak("searching details....Wait")
                self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=4)
                print(results)
                speak(results)
            elif "time" in self.query:
                self.Clock_time()
            elif "close browser" in self.query:
                self.close_browser()
            elif "what's today" in self.query:
                self.Cal_day()
            elif ("remind me" in self.query) or ("alarm" in self.query):
                if "remind me" in self.query:
                    print("Enter msg to remind")
                    msg = self.STT()
                    print("Enter time(like 11:15)")
                    time = self.STT()
                    print("Enter date(like 21 july)")
                    date = self.STT()
                    res = "remind me to "+ msg + "at " + time + "on " + date
                    self.remind(res)
                else:
                    msg = "Alarm"
                    print("Enter time(like 11:15)")
                    time = self.STT()
                    print("Enter date(like 21 july)")
                    date =self.STT()
                    res = "remind me to " + msg + "at " + time + "on " + date
                    self.remind(res)
                     # Volume
            elif "send text" in self.query:
                print("Type message :")
                message=self.STT()
                print("Type number :")
                number=self.STT()
                self.sending_text(message,number)
            elif (self.query.find("volume") != -1):
                le = self.query.find("volume")+len("volume")+1
                self.query= self.query[le:]

                try:
                    # Up
                    if (self.query == "up" or self.query== "high"):
                        os.system("amixer set 'Master' 5%+")
                    # Down
                    elif (self.query== "down" or self.query == "low"):
                        os.system("amixer set 'Master' 5%-")

                except:

                    print("Couldn't do it")

            # Brightness/Volume Up
            elif (self.query.find("increase") != -1):
                le = self.query.find("increase")+len("increase")+1
                self.query = self.query[le:]

                try:

                    # Brightness
                    if (self.query == "brightness" or self.query== "light"):
                        os.system("xbacklight -inc 5")

                    # Volume
                    elif (self.query == "volume" or self.query == "sound"):
                        os.system("amixer set 'Master' 5%+")

                except:

                    print("Couldn't do it")

            # Brightness/Volume Down
            elif (self.query.find("decrease") != -1):
                le = self.query.find("decrease")+len("decrease")+1
                self.query= self.query[le:]

                try:

                    # Brightness
                    if (self.query== "brightness" or self.query == "light"):
                        os.system("xbacklight -dec 5")

                    # Volume
                    elif (self.query == "volume" or self.query == "sound"):
                        os.system("amixer set 'Master' 5%-")

                except:

                    print("Couldn't do it")

            # Set Volume/Brightness
            elif (self.query.find("set") != -1):
                le = self.query.find("set")+len("set")+1
                self.query= self.query[le:]

                try:

                    if (self.query == "volume" or self.query== "sound"):
                        n = int(filter(str.isdigit, self.query))
                        os.system("amixer set 'Master' " + n + "%")

                    if (self.query == "brightness" or self.query == "light"):
                        n = int(filter(str.isdigit, self.query))
                        os.system("xbacklight -set " + n)

                except:

                    print("Couldn't set")
            elif 'open youtube' in self.query or "open video online" in self.query:
                webbrowser.open("https://www.youtube.com")
                speak("opening youtube")
            elif 'open github' in self.query:
                webbrowser.open("https://www.github.com")
                speak("opening github")  
            elif 'open google' in self.query:
                webbrowser.open("https://www.google.com")
                speak("opening google")
            elif 'open gmail' in self.query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail")
            elif 'open amazon' in self.query or 'shop online' in self.query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            elif 'play music' in self.query:
                speak("ok i am playing music")
                play_music()
            elif "pause music" in self.query:
                speak("ok i am pausing music")
                pause_music() 
            elif "stop music" in self.query:
                stop_music() 
            elif "next song" in self.query:
                next_song()
            elif "previous song" in self.query:
                previous_song()
            elif 'play' in self.query and 'music' not in self.query:
                play_specific_song(self.query)
            elif "get news" in self.query:
                get_news()
            elif "change wallpaper" in self.query:
                change_wallpaper()
            elif  "create a qr code" in self.query:
                qrCodeGenerator()
            elif "temperature" in self.query:
                temperature_info()
            elif 'open video' in self.query or "video" in self.query:
                speak("ok i am playing videos")
                video_dir = 'D:/movies/'
                videos = os.listdir(video_dir)
                os.startfile(os.path.join(video_dir,videos[0]))  
            elif "whats up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)  
                ans_take_from_user_how_are_you = self.STT()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'ok' in ans_take_from_user_how_are_you:
                    speak('okey..')  
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                    speak('oh sorry..')  
            elif 'make you' in self.query or 'created you' in self.query or 'develop you' in self.query:
                ans_m = " For your information a group of five members Created me ! I give Lot of Thanks to Him "
                print(ans_m)
                speak(ans_m)
            elif "who are you" in self.query or "about you" in self.query or "your details" in self.query:
                about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                print(about)
                speak(about)
            elif "hello" in self.query or "hello Jarvis" in self.query:
                hel = "Hello Srujan ! How May i Help you.."
                print(hel)
                speak(hel)
            elif "your name" in self.query or "sweet name" in self.query:
                na_me = "Thanks for Asking my name my self ! Jarvis"  
                print(na_me)
                speak(na_me)
            elif "internet speed" in self.query:
                InternetSpeed()
            elif "how you feel" in self.query:
                print("feeling Very sweet after meeting with you")
                speak("feeling Very sweet after meeting with you")
            elif "read pdf" in self.query:
                pdf_handler()
            elif 'exit' in self.query or 'abort' in self.query or 'stop' in self.query or 'bye' in self.query or 'quit' in self.query :
                ex_exit = 'I felt very sweet after meeting with you but you are going! i am very sad'
                speak(ex_exit)
                exit()
            
            elif self.query == 'none':
                continue
            else:
                temp = self.query.replace(' ','+')
                g_url="https://www.google.com/search?q="    
                res_g = "sorry! i cant understand but if you want to search on internet say Yes or else No"
                speak(res_g)
                print("Say Yes or No")
                ans_from_user=self.STT()
                if 'yes' in ans_from_user:
                    speak('Opening Google...')
                    webbrowser.open(g_url+temp)
                elif 'no' in ans_from_user:
                    speak('Google Search Aborted,Speak Again')
                    self.STT()
    

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/redclose.png);border:none;")
        self.exitB.clicked.connect(self.close)

        self.minB.setStyleSheet("background-image:url(./lib/mini40.png);border:none;")
        self.minB.clicked.connect(self.showMinimized)
        self.setWindowFlags(flags)
        def shutDown():
            speak("Shutting down")
            os.system('shutdown /s /t 5') 
            self.shutB.clicked.connect(self.shutDown)
        def reStart():
            speak("Your PC is Restarting")
            os.system('shutdown /r /t 5') 
            self.restartB.clicked.connect(self.reStart)
        
        self.pauseB.clicked.connect(self.close)
            
        self.label_2.setStyleSheet("background-image:url(./lib/dashboard.png);")
        self.label_3.setStyleSheet("background-image:url(./lib/army.png);")
        self.label_6.setStyleSheet("background-image:url(./lib/panel.png);")
        self.label_10.setStyleSheet("background-image:url(./lib/panel.png);")
        
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()
        
        self.ts = time.strftime("%A, %d %B")
        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText(self.ts)
        self.label_5.setFont(QFont(QFont('Arial',8)))
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label_11.setText(label_time)
        

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())

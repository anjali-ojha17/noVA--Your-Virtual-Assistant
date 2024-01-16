import customtkinter as ct
from tkinter import *
import tkinter as tk
import pyttsx3 #text to speech
import datetime
import speech_recognition as sr #recognizing of our speech with the help of google speech converter
import wikipedia
import pywhatkit as w 
import os
import random
import pyjokes
import pyautogui
from selenium import webdriver
import time


ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')

name='user'

class App():
    def __init__(self):
        self.root=ct.CTk()
        self.root.title("noVA - Your Virtual Assistant")          #screen layout
        self.root.geometry("650x480")
        
        self.frame=ct.CTkFrame(master=self.root,height=950,width=2000)
        self.frame.place(x=0,y=0)
        # self.gif = PhotoImage(file='pic.png')
        self.gif = PhotoImage(file=r'C:\Users\ANJALI OJHA\OneDrive - BENNETT UNIVERSITY\NOVA THE VIRTUAL ASSISTANT\noVA\pic.png')


        self.label = Label(self.root,bg='black')
        self.label.place(x=0,y=0)
        self.label.configure(image=self.gif)  
          
        self.run=ct.CTkButton(master=self.root,fg_color='transparent',width=100,text='Run',command=self.Start)
        self.run.place(x=280,y=320)
        self.stop=ct.CTkButton(master=self.root,fg_color='transparent',width=100,text='Stop',command=self.Stop)
        self.stop.place(x=280,y=350)
        self.run=ct.CTkButton(master=self.root,fg_color='transparent',width=100,text='Help',command=self.help)
        self.run.place(x=280,y=380)
        self.run=ct.CTkButton(master=self.root,fg_color='transparent',width=100,text='Exit',command=self.destroy)
        self.run.place(x=280,y=410)
        self.textframe=tk.Label(master=self.root,text='',bg='black',fg='white',height=4,width=37,font=('montserrat',20,'bold'))               #frame to display text
        self.textframe.place(x=0,y=50)
        self.value=True
        self.contacts={'a':122,'b':1222}           #program begins
        self.engine=pyttsx3.init('sapi5')           #text-to-speech conversion                                             #sapi5 for speech recognition
        self.voices=self.engine.getProperty('voices')           #getting voices from system
        self.engine.setProperty('voice',self.voices[0].id)      #setting the default voice as first one
        
    def speak(self,text):          #function to speak the text 
        self.engine.say(text)
        self.engine.runAndWait()
        
    def Stop(self):
        self.value=False
        self.textframe['text']='Stopped'
        self.textframe.update()   

    def help(self):
        self.Stop()
        self.help_window=ct.CTkFrame(self.root,height=500,width=650)
        self.help_window.place(x=0,y=0)
        self.heading=ct.CTkLabel(self.help_window,text = ' Help ',font=('montserrat bold',30,'underline'))
        self.heading.place(x=290,y=20)
        self.canvas=ct.CTkCanvas(self.help_window,bg='white',height=420,width=760)
        self.canvas.place(x=20,y=100)
        self.scroll=Scrollbar(self.canvas,orient='vertical')
        self.scroll.pack(side=tk.RIGHT,fill=Y)
        self.text=tk.Text(self.canvas,fg='white',bg='black',width=71,height=19,padx=20,pady=20,yscrollcommand=self.scroll.set)
        
        file=open('help.txt','r')
        text1=file.read()
        
        self.text.insert('1.0',text1)
        self.text.configure(state=DISABLED)
        self.scroll.config(command=self.text.yview)
        self.text.pack()
        back=ct.CTkButton(self.help_window,text='Back',command=self.help_window.destroy)
        back.place(x=250,y=430)

    def destroy(self):
        self.textframe['text']='Thank you for spending time with me. \n Have a nice day!'
        self.textframe.update()
        self.speak('Thank you for spending time with me. Have a nice day!')     
        self.root.destroy()

  

    def Start(self):
        self.value=True
        self.contacts={'a':122,'b':1222}           #program begins
        self.engine=pyttsx3.init('sapi5')           #text-to-speech conversion                                             #sapi5 for speech recognition
        self.voices=self.engine.getProperty('voices')           #getting voices from system
        self.engine.setProperty('voice',self.voices[0].id)      #setting the default voice as first one
        

        def wish(self):
            self.hour=int(datetime.datetime.now().hour)
            a=''
            if self.hour>=0 and self.hour<12:
                a=[f'Good morning {name}',f'Hello {name} Good morning']
                greet=random.choice(a)
                self.textframe['text']=greet
                self.textframe.update()
                self.speak(greet)
            elif self.hour>=12 and self.hour<=16:
                a=[f'Good afternoon {name}',f'Hello {name} Good afternoon']
                greet=random.choice(a)
                self.textframe['text']=greet
                self.textframe.update()
                self.speak(greet)            
            else:
                a=[f'Good evening {name}',f'Hello {name} Good evening']
                greet=random.choice(a)
                self.textframe['text']=greet
                self.textframe.update()
                self.speak(greet)
                
            wel=['So how can I help you?','How can I help?','Give me a command, please','What can I do for you?']
            welcome=random.choice(wel)
            self.textframe['text']=welcome
            self.textframe.update()
            self.speak(welcome)
        wish(self)

        def takeCommand(self):
            r=sr.Recognizer()
            with sr.Microphone(device_index=1) as source:
                self.textframe['text']='Listening...'
                self.textframe.update()
                r.pause_threshold=1
                audio=r.listen(source)
            try:
                self.textframe['text']='Recognizing...'
                self.textframe.update()
                command=r.recognize_google(audio,language='en-in')
                self.textframe['text']=f'User said {command}'
                self.textframe.update()
                time.sleep(2)
            except Exception as e:
                self.textframe['text']='Say it again please...'  
                self.textframe.update()
                self.speak('Say it again please...') 

                return 'None'
            return command
        
        
        while self.value:
            
            command = takeCommand(self).lower()
            
            if 'who are you' in command or 'give me your introduction' in command:
                
                self.textframe['text']='Wait i am introducing myself. \nMy Name is nova, I am an assistant made by \npython programming, I can do many works like \nplaying games, opening programs, opening youtube\n, searching web and many more'  
                self.textframe.update()
                self.speak('Wait i am introducing myself. My Name is nova, I am an assistant made by python programming, I can do many works like playing games, opening programs, opening youtube, searching web and many more')
            elif "who am i" in command:
                jh = "if you are speaking then, definately you are a human", "You aare a user", "You are a human", "I cant identify peoples with their vocies,\n may be you are the user or anybody with relation of user"
                ahd=(random.choice(jh))
                self.textframe['text']=ahd
                self.textframe.update()
                self.speak(ahd)
        
            elif 'hello' in command:
                gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and \ngethering information, how can i help?", "Online and ready"
                sp=(random.choice(gf))
                self.textframe['text']=sp
                self.textframe.update()
                self.speak(sp)
            
            
        
            elif 'wikipedia' in command:
                    self.textframe['text']='searching wikipedia... please wait'
                    self.textframe.update()
                    self.speak('Searching Wikipedia...please wait')
                    command = command.replace("wikipedia", "")
                    results =  wikipedia.summary(command, sentences = 4)
                    self.textframe['text']='According to wikipedia..'
                    self.textframe.update()
                    self.speak("According to wikipedia")
                    self.txt=tk.Text(self.root,height=7,width=55,bg='black',fg='white',font=('helvetica',14))
                    self.txt.insert('1.0',results)
                    self.txt.place(x=20,y=30)
                    self.root.update()
                    self.speak(results)
                    self.txt.destroy()
                   
                    
                    
                
            
            elif 'top' in command or 'stop' in command:
                self.Stop()
                
            elif 'joke' in command:
                jok=(pyjokes.get_joke())
                
                self.txt=tk.Text(self.root,height=7,width=55,bg='black',fg='white',font=('helvetica',15))
                self.txt.insert('1.0',jok)
                self.txt.place(x=20,y=30)
                self.root.update()
                self.speak(jok)
                
            elif 'help' in command:
                self.help()  
             
            elif 'bye' in command:
                self.destroy()      
                
            elif 'weather' in command:    
                
     
                self.textframe['text']='please provide the location: '
                self.textframe.update()
                self.speak('please provide the location')
                city=takeCommand(self)
                self.textframe['text']='I am searching for the weather'
                self.textframe.update()
                self.speak('I am searching for the weather')
                
                try:
                    driver = webdriver.Chrome()
                    driver.get("https://www.timeanddate.com/weather/india/"+city)
                    out=(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
                    self.textframe['text']=out
                    self.textframe.update()
                    self.speak(out)
                except:
                    print("Something went wrong")    
                
            elif 'shutdown' in command or 'shut down' in command:
                self.textframe['text']='Do you really want to shutdown the system sir!'
                self.textframe.update()
                self.speak("Do you really want to shutdown the system sir?")
                ch = takeCommand(self)
                if "yes" or "please" in ch:
                    self.textframe['text']='shutting down the system!'
                    self.textframe.update()
                
                    os.system("shutdown /s /t 1")
                else:
                    self.textframe['text']='ok sir!'
                    self.textframe.update()
                    self.speak('ok sir!!')
                
            elif 'restart' in command:
                self.textframe['text']='Ok sir i will restart the system!'
                self.textframe.update()
                self.speak("Ok sir i will restart the system ")
           
                os.system("restart /r /t 1")
            
            elif 'switch the window' in command:
           
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                    
            elif 'time' in command:
                strTime = datetime.datetime.now().strftime("%I:%M:%S")
                self.textframe['text']=strTime
                self.textframe.update()
                self.speak(f"sir, the time is {strTime}")
            
            elif 'the date' in command:
                strdate = datetime.datetime.today().strftime("%d %m %y")
                self.textframe['text']=strdate
                self.textframe.update()
                self.speak("Sir today's date is %s" %strdate)    
                
            elif 'document' in command:
                
                self.textframe['text']='ok sir! i am opening microsoft word file'
                self.textframe.update()
                self.speak('ok sir! i am opening microsoft word file')
                doc="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(doc)
            
            elif 'can you do for me' in command:
                self.textframe['text']='I can do multiple tasks for you sir.\n tell me whatever you want to perform Sir'
                self.textframe.update()
           
                self.speak('I can do multiple tasks for you sir. tell me whatever you want to perform Sir')

            elif 'old are you' in command:
                self.textframe['text']='I am Artificial Intelligence i am not born\n instead i am developed'
                self.textframe.update()
                self.speak("I am Artificial Intelligence i am not born, instead i am developed")       
            elif 'send message' in command:
                
                self.window=ct.CTk()
                self.window.geometry('450x400')
                
                def mic():
                    message=takeCommand(self)  
                    self.messag.insert(0,message)
                                
                def send():
                    numb=self.no.get()
                    mess=self.messag.get()
                    w.sendwhatmsg('+91'+ numb, f"{mess}" , int(self.hour.get()) , int(self.minutes.get()) )
                    
                self.label1=ct.CTkLabel(self.window,text='Please enter mobile number:')
                self.label1.place(x=30,y=30)
                self.no=ct.CTkEntry(self.window,width=185,placeholder_text='Mobile no.')
                self.no.place(x=200,y=30)
               
                self.label3=ct.CTkLabel(self.window,text='Please enter the text message:')
                self.label3.place(x=30,y=80)
                self.messag=ct.CTkEntry(self.window,width=185)
                self.messag.place(x=200,y=80)
                self.button=ct.CTkButton(self.window,width=1,text=' ',command=mic)
                self.button.place(x=400,y=80)
                
            
                self.label2=ct.CTkLabel(self.window,text='Please enter time: ')
                self.label2.place(x=30,y=130)
                self.hour=ct.CTkOptionMenu(self.window,width=150,dynamic_resizing=False,values=['hour','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'])
                self.hour.place(x=200,y=130)
                
                l=[str(a) for a in range(61)]
                l.insert(0,'minutes')
                self.minutes=ct.CTkOptionMenu(self.window,width=150,dynamic_resizing=False,values=l)
                self.minutes.place(x=200,y=180)
                self.enter=ct.CTkButton(self.window,text='Enter', command=send )
                self.enter.place(x=30,y=250)
            
                self.window.mainloop()
                continue
                
                
                
            elif 'close' in command:
                driver.close()
        
            elif 'search youtube' in command:
                self.textframe['text']='What do you want to search?'
                self.textframe.update()
                self.speak('what do you want to search?')
                u=takeCommand(self)
                self.textframe['text']=u
                self.textframe.update()
                self.speak('ok sir, i am launching it.')
        
                driver = webdriver.Chrome("C:\\Users\\vandit\\OneDrive - BENNETT UNIVERSITY\\Desktop\\noVA\\chromedriver.exe")
                driver.get('https://www.youtube.com/results?search_query='+u)
            
            elif 'search google' in command:
                self.textframe['text']='What do I search for you?'
                self.textframe.update()
                self.speak('what do i search for you?')
                search = takeCommand(self)
                self.textframe['text']=search 
                self.textframe.update()
                self.speak('ok sir! i am launching it.')
            
                driver = webdriver.Chrome("C:\\Users\\vandit\\OneDrive - BENNETT UNIVERSITY\\Desktop\\noVA\\chromedriver.exe")
                driver.get('https://google.com/search?q='+search) 
                
                
            elif 'create file' in command or 'create a file' in command:
                self.speak('Enter your file name:-')
                self.textframe['text']='Enter your file name: '
                self.textframe.update()
                r=takeCommand(self)
                
                fileptr = open(r+".txt","a");    
                if fileptr:
                   
                    self.speak("File created successfully")
                    self.speak('Enter tha data you want to store:-')
                    self.textframe['text']='Enter the data you want to store:-' 
                    self.textframe.update()   
                    fileptr.write(takeCommand(self))
                    self.speak('your file has been created and written successfully')
                    self.textframe['text']='Your file has been created and written successfully'
                    self.textframe.update()
                    fileptr.close()   
            elif 'open file' in command:
                self.speak('sir!! please tell me the name of the file you want to read!')
                self.textframe['text']='Sir!! please tell me the name \n of file you want to read :- '
                self.textframe.update()
                r=takeCommand(self)    
                fileptr=open(r+'.txt','r')
                readi=fileptr.readlines()
                self.textframe['text']=readi
                self.textframe.update()
                self.speak(readi) 
                   
                
            elif "take screenshot" in command or "take a screenshot" in command or "screenshot" in command:
                self.textframe['text']='sir, please tell me the name of this \n screenshhot file name'
                self.textframe.update()
                self.speak('sir, please tell me the name of this screenshhot file name')
                name1 = takeCommand(self).lower()
                self.textframe['text']= name1
                self.textframe.update()
                self.speak('please sir hold the screen for a seconds, i am taking screenshot')
                self.textframe['text']='please sir hold the screen for a seconds,\n i am taking screenshot' 
                self.textframe.update()
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name1}.png")
                self.speak('i am done sir, the screenshot is saved in our main folder. now i am ready for the next command.. ')
                
            elif  "you can sleep" in command or "sleep now" in command:
                self.textframe['text']='okay sir, i am going to\n sleep you can call me anytime..'
                self.textframe.update()
                self.speak('okay sir, i am going to sleep you can call me anytime..')
                break
            
            elif 'play music' in command or 'change music' in command:
                self.textframe['text']='Here are your favourites'
                self.textframe.update()
                self.speak('Here are your favorites')
                music_dir = "C:\\Users\\vandit\\OneDrive - BENNETT UNIVERSITY\\Desktop\\noVA\\music"
                music = os.listdir(music_dir)
                l=len(music)
                n = random.randint(0,l)
                os.startfile(os.path.join(music_dir, music[n])) 
        
            elif 'thank you' in command:
                self.textframe['text']='Welcome Sir!'
                self.textframe.update()
                self.speak("Welcome Sir")
            
                       
if __name__ == "__main__":
    app = App()
    app.root.mainloop()
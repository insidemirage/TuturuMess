import browser_cookie3
import requests
from bs4 import BeautifulSoup
from threading import Timer
from plyer import notification
class Exchange(object):
    def __init__(self, url, logdata, projects, projectsind, mess, messind, upd):
        self.url = url  # url - sign in url
        self.logdata =  logdata # logdata - post for sign in 
        self.projects = projects    # projects - url projects page
        self.projectsind = projectsind  # prijectsind - ind for find proj
        self.mess = mess    # mess - message url
        self.messind = messind  # messind - ind to find message
        self.session = requests.Session() 
        self.lastprojtext = '' # to check for upd
        self.timer = Timer(upd, self.Update) #time of checking
        self.lastmessage = ''
        self.upd = upd
    def Login(self):
        self.r = self.session.post(self.url, data=self.logdata)
        self.timer.start()
        self.Update()
   
    def Update(self):
        self.CheckforProj()
        self.CheckforMess()
        self.timer.cancel()
        self.timer = Timer(self.upd, self.Update)
        self.timer.start()
        
class Kwork(Exchange):
    def CheckforProj(self):
        z = requests.get(self.projects, cookies=self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        text = str(soup.find("div", {"class": self.projectsind}).text)
        if(text == self.lastprojtext):
            print('no new project appeared')
            fss.write(text+' = '+self.lastprojtext+'\n') #debg

        else:
            print('you have got new project')
            self.lastprojtext = text
            notification.notify(title='Tuturu',message='You got proj',app_name='Tuturu')
            fss.write(text+' not '+self.lastprojtext+'\n') #debg
    def CheckforMess(self):
        z = requests.get(self.mess, cookies=self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        nuser = soup.find_all("span", {"class": self.messind}) #fix it
        if not nuser:
            print('New messages:0')
            return False
        text = nuser[0].text
        print(text)
        if(text == self.lastmessage):
            print('no new message')
            print('New messages: '+str(len(nuser)))
        else:
            print('new message')
            self.lastmessage = text
            notification.notify(title='Tuturu',message='You got mess',app_name='Tuturu')
            print('New messages: '+str(len(nuser)))
            
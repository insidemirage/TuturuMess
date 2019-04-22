import requests
from bs4 import BeautifulSoup
from plyer import notification
class Exchange(object):
    def __init__(self, url, logdata, projects, projectsind, mess, messind, upd, messagelabel, projectlabel):
        self.url = url  # url - sign in url
        self.logdata =  logdata # logdata - post for sign in 
        self.projects = projects    # projects - url projects page
        self.projectsind = projectsind  # prijectsind - ind for find proj
        self.mess = mess    # mess - message url
        self.messind = messind  # messind - ind to find message
        self.session = requests.Session() 
        self.lastprojtext = '' # to check for upd
        self.lastmessage = ''
        self.upd = upd
        self.messagelabel = messagelabel
        self.projectlabel = projectlabel
        self.Login()
    def Login(self):
        print(self.logdata['l_username'])

        self.r = self.session.post(self.url, data=self.logdata)
        self.Update()
   
   
        
class Kwork(Exchange):
    def CheckforProj(self):
        z = requests.get(self.projects, cookies=self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        text = str(soup.find("div", {"class": self.projectsind}).text)
        if(text == self.lastprojtext):
            print('no new project appeared')

        else:
            print('you have got new project')
            self.lastprojtext = text
            # notification.notify(title='Tuturu',message='You got proj',app_name='Tuturu')
    def CheckforMess(self):
        z = requests.get(self.mess, cookies=self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        nuser = soup.find_all("span", {"class": self.messind}) #fix it
        if not nuser:
            print('New messages:0')
            return False
        text = nuser[0].text
        print(text)
        print(self.logdata['l_username'])
        self.messagelabel.config(text = 'new')
        if(text == self.lastmessage):
            print('no new message')
            print('New messages: '+str(len(nuser)))
            
        else:
            print('new message')
            self.lastmessage = text
            notification.notify(title='Tuturu',message='You got mess',app_name='Tuturu')
            print('New messages: '+str(len(nuser)))
    def Update(self):
        self.CheckforProj()
        self.CheckforMess()
            
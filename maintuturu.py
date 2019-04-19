import browser_cookie3
import requests
from bs4 import BeautifulSoup
from threading import Timer
from plyer import notification



# it'll be removed
f = open('password.txt')
passlog = [];
for i in f:
    passlog.append(i)

#  exchange class
class Exchange(object):
    def __init__(self, url, logdata, projects, projectsind, mess, messind):
        self.url = url  # url - sign in url
        self.logdata =  logdata # logdata - post for sign in 
        self.projects = projects    # projects - url projects page
        self.projectsind = projectsind  # prijectsind - ind for find proj
        self.mess = mess    # mess - message url
        self.messind = messind  # messind - ind to find message
        self.session = requests.Session() 
        self.lastprojtext = '' # to check for upd
        self.timer = Timer(300, self.Update) #time of checking
        self.lastmessage = ''
    def Login(self):
        self.r = self.session.post(self.url, data=self.logdata)
        self.timer.start()
        self.Update()
    def CheckforProj(self):
        z = requests.get(self.projects, cookies=self.session.cookies)
        fss = open('log.txt','a', encoding='utf-8') #just for check the answer
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
        nuser = soup.find("span", {"class": self.messind}).text #fix it
        text = str(nuser)
        print(nuser) #deb
        fss = open('log.txt','a', encoding='utf-8') #just for check the answer

        if(text == self.lastmessage):
            print('no new message')
            fss.write(text+' = '+self.lastmessage+'\n') #debg

        else:
            print('new message')
            self.lastmessage = text
            notification.notify(title='Tuturu',message='You got mess',app_name='Tuturu')
            fss.write(text+' not '+self.lastmessage+'\n') #debg
        
    def Update(self):
        self.CheckforProj()
        self.CheckforMess()
        self.timer.cancel()
        self.timer = Timer(300, self.Update)
        self.timer.start()

#creating kwork object
data = {'track_client_id': '2131145171.1548624821', 'l_username': passlog[0],'l_password':passlog[1]}
#makin' request data
kwork = Exchange('https://kwork.ru/api/user/login',data, 'https://kwork.ru/projects', 'wants-card__header-title', 'https://kwork.ru/inbox' , 'm-bold' )
kwork.Login()


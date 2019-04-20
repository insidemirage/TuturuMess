import browser_cookie3
import requests
from bs4 import BeautifulSoup
from threading import Timer
from plyer import notification


passlog = []
passlog.append(input('login:'))
passlog.append(input('pass:'))

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
            text = str(soup.find("div", {"class": 'breakwords'}).text)
            print(text)
            text = str(soup.find("div", {"class": 'wants-card__header-price'}).text)
            print(text)
        
  
       
    def Update(self):
        self.CheckforProj()
        self.timer.cancel()
        self.timer = Timer(300, self.Update)
        self.timer.start()

#creating kwork object
data = {'track_client_id': '2131145171.1548624821', 'l_username': passlog[0],'l_password':passlog[1]}
#makin' request data
kwork = Exchange('https://kwork.ru/api/user/login',data, 'https://kwork.ru/projects?c=11&', 'wants-card__header-title', 'https://kwork.ru/inbox' , 'm-bold' )
kwork.Login()



import browser_cookie3
import requests
from bs4 import BeautifulSoup
from threading import Timer
# it'll be removed
f = open('password.txt')
passlog = [];
for i in f:
    passlog.append(i)
# 
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
        self.timer = Timer(15, self.Update) #time of checking
    def Login(self):
        self.r = self.session.post(self.url, data=self.logdata)
        self.timer.start()
    def CheckforProj(self):
        z = requests.get(self.projects, cookies=self.session.cookies)
        fss = open('answer.html','w', encoding='utf-8') #just for check the answer
        soup = BeautifulSoup(z.text, 'html.parser')
        text = str(soup.find("div", {"class": "card"}))
        fss.write(text) #debg
        if(text != self.lastprojtext):
            print('you have got new project')
            self.lastprojtext = text
        else:
            print('no new project appeared')
    def Update(self):
        self.CheckforProj()
        self.timer.cancel()
        self.timer = Timer(15, self.Update)
        self.timer.start()

#creating kwork object
data = {'track_client_id': '2131145171.1548624821', 'l_username': passlog[0],'l_password':passlog[1]}
#makin' request data
kwork = Exchange('https://kwork.ru/api/user/login',data, 'https://kwork.ru/projects', 'card', 1 , 2 )
kwork.Login()


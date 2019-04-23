import requests
from bs4 import BeautifulSoup
import time
from threading import *
from tkinter import *
import sqlite3
import os
# from plyer import notification

class Program(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Tuturu Mess")
        self.root.geometry("300x400")
        self.root.configure(background='white')
        self.root.iconbitmap('icon.ico')
        self.labelmessage = []
        self.labelproj = []
        self.frame = []
        self.btnadd = Button(text='Add exchange')
        self.exch = []
        #connecting to db
        if os.path.isfile('data.db'):
            self.connection = sqlite3.connect('data.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute("""SELECT * FROM logdata""")
            self.data = self.cursor.fetchall()
        else:
            print('Error db not found')
            sys.exit(0)
        for i in range(0, len(self.data)):
            self.frame.append(Frame(self.root,bd=1,bg='white', relief=RAISED))
            self.labelmessage.append(Label(self.frame[i], text='Messages: 0',bg='white', justify='left'))
            self.labelproj.append(Label(self.frame[i], text='Projects: 0',bg='white', justify='left'))
            self.labelmessage[i].pack(anchor='nw')            
            self.labelproj[i].pack(anchor='nw')
            self.frame[i].pack(fill='x', ipady=5)
        self.exch.append(Exchange('https://kwork.ru/api/user/login', 'ksajfkq214@yandex.ru', '84j27696R3', 'https://kwork.ru/projects', 'wants-card__header-title',self.labelproj[0], 10))
        self.exch.append(Exchange('https://kwork.ru/api/user/login', 'kikstarter', 'safv231vas', 'https://kwork.ru/projects', 'wants-card__header-title',self.labelproj[1], 10))
        self.root.mainloop()



class Exchange(object):
    def __init__(self, logurl, username, password, projectpage, projectsfind, projlb, timer ):
        self.loginurl = logurl
        self.uspass = username
        self.passw = password
        self.projp = projectpage
        self.projf = projectsfind
        self.updtime = timer
        self.updtimer = Timer(timer, self.Update)
        self.updtimer.start()
        self.logdata = {'l_username':username, 'l_password':password}
        self.session = requests.Session()
        self.r = self.session.post(logurl, self.logdata)
        self.numberofproj = 0
        self.lastproj = ''
        self.projlb = projlb
        self.Update()
    def CheckForProjects(self):
        z = requests.get(self.projp, cookies= self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        nuser = str(soup.find("div", {"class": self.projf}).text)

        if  self.lastproj != nuser:
            print('new project')
            self.numberofproj = self.numberofproj+1
            txtfpl = 'New projects: {0}'.format(self.numberofproj)
            self.projlb.config(text=txtfpl)
            print(self.numberofproj)
            print(nuser)
            self.lastproj = nuser
        else:
            print('no new projects')
    def Update(self):
        self.CheckForProjects()
        print(self.logdata)
        self.updtimer.cancel()
        self.updtimer = Timer(self.updtime, self.Update)
        self.updtimer.start()
ex = Program()
kwork = []
# kwork.append(Exchange('https://kwork.ru/api/user/login', 'ksajfkq214@yandex.ru', '84j27696R3', 'https://kwork.ru/projects', 'wants-card__header-title', 10))
# kwork.append(Exchange('https://kwork.ru/api/user/login', 'kikstarter', 'safv231vas', 'https://kwork.ru/projects', 'wants-card__header-title', 10))

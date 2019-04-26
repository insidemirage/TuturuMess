import requests
from bs4 import BeautifulSoup
import time
from threading import *
from tkinter import *
import sqlite3
import os
from playsound import playsound
# from plyer import notification

class Program(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Tuturu Mess")
        x = int((self.root.winfo_screenwidth() - 250) / 2)
        y = int((self.root.winfo_screenheight() - 400) / 2)
        self.root.geometry("250x400+{0}+{1}".format(x,y))
        self.root.configure(background='white')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(width=False, height=False)
        self.mainmenu = Menu(self.root) 
        self.root.config(menu=self.mainmenu)
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.mainmenu.add_cascade(label='Файл', menu = self.filemenu)
        self.filemenu.add_command(label="Открыть...")
        self.filemenu.add_command(label="Выход")
        self.basemenu = Menu(self.mainmenu, tearoff=0)
        self.mainmenu.add_cascade(label='База данных', menu = self.basemenu)
        self.basemenu.add_command(label = 'База данных')
        self.basemenu.add_command(label = 'Импорт')

        self.labelmessage = []
        self.labelproj = []
        self.frame = []
        self.btnadd = Button(text='Add exchange', bg='white', command=self.AddExchange)
        self.exch = []
        self.debug = ['https://kwork.ru/projects?c=15&','https://kwork.ru/projects']
        self.txt = []
        
        
        #connecting to db
        if (not os.path.isfile('ru.uis')):
            #here's a modal if u got no text file
            top = Toplevel(self.root)
            top.transient(self.root)
            x = int((self.root.winfo_screenwidth() - 300) / 2)
            y = int((self.root.winfo_screenheight() - 100) / 2)
            top.protocol("WM_DELETE_WINDOW", self.root.destroy) #u will not close it
            top.geometry("300x100+{0}+{1}".format(x,y))
            
            Label(top,bg='white',text='На вашем компьтере отсутствуют файлы с текстом').pack(fill='x')
            Button(top, text='ОК', width=5, command=self.root.destroy).pack()
            top.iconbitmap('icon.ico')
            top.configure(bg='white')
            top.grab_set()
            top.focus_set()
            top.resizable(width=False, height=False)
            top.wait_window()
        else:
            #getin' lines from text file
            with open('ru.uis', encoding='utf-8') as txtsrc:
                self.txt = txtsrc.readlines()
        #checkin for bd
        if os.path.isfile('data.db'):
            #collectin' userdata
            self.connection = sqlite3.connect('data.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute("""SELECT * FROM logdata""")
            self.data = self.cursor.fetchall()
            #making frames with status labels
            for i in range(0, len(self.data)):
                self.frame.append(Frame(self.root,bd=1,bg='white', relief=RAISED))
                self.labelmessage.append(Label(self.frame[i], text='Messages: 0',bg='white', justify='left'))
                self.labelproj.append(Label(self.frame[i], text='Projects: 0',bg='white', justify='left'))
                self.labelmessage[i].pack(anchor='nw')            
                self.labelproj[i].pack(anchor='nw')
                self.frame[i].pack(fill='x', ipady=5)
                self.exch.append(Exchange('https://kwork.ru/api/user/login', self.data[i][1], self.data[i][2], self.debug[i], 'wants-card__header-title',self.labelproj[i], 'https://kwork.ru/inbox', 'm-bold', self.labelmessage[i], 300))
        else:
            #modal if db ! db
            print('Error db not found')
            if(self.txt):
                top = Toplevel(self.root)
                x = int((self.root.winfo_screenwidth() - 400) / 2)
                y = int((self.root.winfo_screenheight() - 190) / 2)
                top.geometry("400x190+{0}+{1}".format(x,y))
                Label(top,bg='white',text=self.txt[0],wraplength=300).pack(fill='x')
                Label(top,bg='white',text=self.txt[1]).pack(fill='x')
                Label(top,bg='white',text=self.txt[2]).pack(fill='x')
                Button(top, text='ОК', width=10, command=top.destroy).pack()
                top.iconbitmap('icon.ico')
                top.configure(bg='white')
                top.grab_set()
                top.focus_set()
                top.resizable(width=False, height=False)
                top.wait_window()
            
            # sys.exit(0)
        self.btnadd.pack(pady=20)
        
        self.root.mainloop()
    def AddExchange(self):
        #adding exchange modal
        top = Toplevel(self.root)
        x = int((self.root.winfo_screenwidth() - 200) / 2)
        y = int((self.root.winfo_screenheight() - 190) / 2)
        top.geometry("200x190+{0}+{1}".format(x,y))

        Label(top,bg='white',text='Login:').pack()
        login = Entry(top, bg='white')
        login.pack()
        Label(top,bg='white',text='Password:').pack()
        passw = Entry(top, bg='white')
        passw.pack()
        frm = Frame(top, bg='white')
        frm.pack(pady=10)
        Button(frm, bg='white',text='OK').pack(side='left', padx=3)
        Button(frm,bg='white',text='CANCEL', command=top.destroy).pack(side='left', padx=3)
        top.iconbitmap('icon.ico')
        top.configure(bg='white')
        top.grab_set()
        top.focus_set()
        top.resizable(width=False, height=False)
        top.wait_window()


class Exchange(object):
    def __init__(self, logurl, username, password, projectpage, projectsfind, projlb,messpage, messind, messl ,timer ):
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
        self.messp = messpage
        self.messi = messind
        self.messagelabel = messl
        self.lmessage = ''
        self.nubmerofmess = 0
        self.Update()
    def CheckForProjects(self):
        z = requests.get(self.projp, cookies= self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        nuser = str(soup.find("div", {"class": self.projf}).text)
        #get last proj from exchange and check if it equals prev
        if  self.lastproj != nuser:
            print('new project')
            playsound('./src/song.mp3')
            self.numberofproj = self.numberofproj+1
            txtfpl = 'New projects: {0}'.format(self.numberofproj)
            self.projlb.config(text=txtfpl)
            print(self.numberofproj)
            print(nuser)
            self.lastproj = nuser
        else:
            print('no new projects')
    def CheckForMess(self):
        z = requests.get(self.messp, cookies=self.session.cookies)
        soup = BeautifulSoup(z.text, 'html.parser')
        nuser = soup.find_all("span", {"class": self.messi}) #fix it
        if not nuser:
            print('New messages:0')
            return False
        text = nuser[0].text
        print(text)
        print(self.logdata['l_username'])
        if(text == self.lmessage):
            print('no new message')
            print('New messages: '+str(len(nuser)))
            self.messagelabel.config(text = 'New messages:{0}'.format(len(nuser)))
        else:
            print('new message')
            self.lmessage = text
            # notification.notify(title='Tuturu',message='You got mess',app_name='Tuturu')
            playsound('./src/song.mp3')
            print('New messages: '+str(len(nuser)))
            self.messagelabel.config(text = 'New messages:{0}'.format(len(nuser)))

    def Update(self):
        #update module
        self.CheckForProjects()
        self.CheckForMess()
        print(self.logdata)
        self.updtimer.cancel()
        self.updtimer = Timer(self.updtime, self.Update)
        self.updtimer.start()
        # upd
ex = Program()

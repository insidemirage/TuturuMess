from tkinter import *
from exchange import *
# need to make timer here not exchange!!
class Window(object):
    def __init__(self, data):
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
        for i in range(0, len(data)):
            self.frame.append(Frame(self.root,bd=1,bg='white', relief=RAISED))
            self.labelmessage.append(Label(self.frame[i], text='Messages: 0',bg='white', justify='left'))
            self.labelproj.append(Label(self.frame[i], text='Projects: 0',bg='white', justify='left'))
            self.frame[i].pack(fill='x', ipady=5)
            self.labelmessage[i].pack(anchor='nw')            
            self.labelproj[i].pack(anchor='nw')
            dates = {'l_username': data[i][1],'l_password':data[i][2]}
            self.exch.append(Kwork('https://kwork.ru/api/user/login',dates, 'https://kwork.ru/projects', 'wants-card__header-title', 'https://kwork.ru/inbox?s=unread' , 'm-bold', 15+(i*10), self.labelmessage[i],self.labelproj[i]))

    def InitForm(self):
        self.btnadd.pack()
        self.root.mainloop()

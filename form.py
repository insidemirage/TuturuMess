from tkinter import *
from exchange import *

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
        for i in range(0, len(data)):
            self.frame.append(Frame(self.root))
            self.labelmessage.append(Label(self.frame[-1], text='Messages:',bg='red', justify='left'))
            self.labelproj.append(Label(self.frame[-1], text='Projects:',bg='red', justify='left'))
            self.frame[-1].pack(fill='x', ipady=5)
            self.labelmessage[-1].pack(anchor='nw')            
            self.labelproj[-1].pack(anchor='nw')

    def InitForm(self):
        self.root.mainloop()
# def CreateForm(passw,login):
#     data = {'l_username': login,'l_password':passw}
#     kwork = Kwork('https://kwork.ru/api/user/login',data, 'https://kwork.ru/projects', 'wants-card__header-title', 'https://kwork.ru/inbox?s=unread' , 'm-bold', 150)
#     root = Tk()
#     root.title("Tuturu Mess")
#     root.geometry('300x400')
#     root.configure(background='white')
#     root.iconbitmap('icon.ico')
#     # exbtn0 = Button(root, text='Kwork', height=2, width=17, bg='white', borderwidth=1, command=kwork.Login)
#     exbtn0.pack(pady=20)
#     exbtn1.pack(pady=20)
#     exbtn2.pack(pady=20)
#     root.mainloop()
from tkinter import *
from exchange import Exchange
def CreateForm(passw,login):
    data = {'l_username': login,'l_password':passw}
    kwork = Exchange('https://kwork.ru/api/user/login',data, 'https://kwork.ru/projects', 'wants-card__header-title', 'https://kwork.ru/inbox?s=unread' , 'm-bold', 150)
    root = Tk()
    root.title("Tuturu Mess")
    root.geometry('300x400')
    root.configure(background='white')
    root.iconbitmap('icon.ico')
    exbtn0 = Button(root, text='Kwork', height=2, width=17, bg='white', borderwidth=1, command=kwork.Login)
    exbtn1 = Button(root, text='Add Extend', height=2, width=17, bg='white', borderwidth=1)
    exbtn2 = Button(root, text='Add Extend', height=2, width=17, bg='white', borderwidth=1)
    exbtn0.pack(pady=20)
    exbtn1.pack(pady=20)
    exbtn2.pack(pady=20)
    root.mainloop()
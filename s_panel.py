from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import pymysql as db 
from s_login import S_Log
from register import Register
from PIL import ImageTk, Image
def Log_Panel():
    s_top=tk.Toplevel()
    s_top.geometry('600x600')
    s_top.title('Hostel Management')
    s_top.configure(background = '#3B2C35')

# Creating title icon
    s_top.iconbitmap('img/Logo.ico')
    top_frame = Label(s_top, text='If you are a new user please click on Register otherwise Click on Login Button...  ',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')




    frame = LabelFrame(s_top,text='SERVICES',padx=300, pady=30, bg='white', bd='5', relief='groove')
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)



    login = tk.Button(frame, text = "Login",command=S_Log, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='8')
    login.pack()
         
    label = Label(frame, bg='white').pack()

  
    register = tk.Button(frame, text = "Register", width="22", bd = '3',command=Register, font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
    register.pack()
    label = Label(frame, bg='white').pack()
    def Quit():
        response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
        if response == 1:
            s_top.destroy()
        else:
            pass
    
    Quit = tk.Button(s_top, text = "Quit", width="10", command = Quit, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)

# Displyaing Widget to Screen
    s_top.mainloop()
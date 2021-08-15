from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import pymysql as db 
from PIL import ImageTk, Image
#from view_profile import profile_view
from change_pass import password_change
from s_login import profile_view
from s_login import stu_alloc_date
from s_login import room_complain


s_top=tk.Toplevel()
s_top.geometry('600x600')
s_top.title('Student Panel')
s_top.configure(background = '#3B2C35')

# Creating title icon
s_top.iconbitmap('img/Logo.ico')
top_frame = Label(s_top, text='WELCOME TO THE SYSTEM',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
top_frame.pack(side='top')


''' Background Image Start'''

''' Background Image End'''

# Creating Frame
frame = LabelFrame(s_top,text='SERVICES',padx=300, pady=30, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


# Creating login button and positioning it
login = tk.Button(frame, text = "View Profile",command=profile_view, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='8')
login.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating and Positioning Button in Main Frame    
register = tk.Button(frame, text = "Change Password",command=password_change, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.pack()
label = Label(frame, bg='white').pack()
register = tk.Button(frame, text = "View Your Allocation Details",command=stu_alloc_date, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.pack()
label = Label(frame, bg='white').pack()
register = tk.Button(frame, text = "Query or Complain",command=room_complain, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.pack()
# Quit Button of main frame 

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
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import pymysql as db 
from PIL import ImageTk, Image
from room import room_registry
from View_detail import view_student
from alloc_delloc import aloc_deloc
from delocation import deloc
from view_allocate import view_alloc_room
from view_deallocate import view_delloc_room
from View_room import view_room
from report import view_report
from complain_page import view_message
from ad_change_pass import admin_password

top=tk.Toplevel()
top.geometry('600x600')
top.title('login details')
top.configure(background = '#3B2C35')

# Creating title icon
top.iconbitmap('img/Logo.ico')
top_frame = Label(top, text='WELCOME TO THE SYSTEM',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
top_frame.pack(side='top')


''' Background Image Start'''

''' Background Image End'''

# Creating Frame
frame = LabelFrame(top,text='SERVICES',padx=300, pady=30, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


# Creating login button and positioning it
login = tk.Button(frame, text = "Room Entry",command=room_registry, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='8')
login.grid(row=5,column=1)
# Creating and Positioning Button in Main Frame    
register = tk.Button(frame, text = "View Student", width="22", bd = '3',command=view_student, font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=5,column=10)

register = tk.Button(frame, text = "Allocation",command=aloc_deloc, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=1,column=1)

register = tk.Button(frame, text = "Deallocation",command=deloc, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=1,column=10)

register = tk.Button(frame, text = "View Room",command=view_room, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=2,column=1)

register = tk.Button(frame, text = "Student Allocation",command=view_alloc_room, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=2,column=10)
register = tk.Button(frame, text = "Student Deallocation",command=view_delloc_room, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=3,column=1)
register = tk.Button(frame, text = "Message Box",command=view_message, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=3,column=10)
register = tk.Button(frame, text = "Change Password",command=admin_password, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=4,column=1)
register = tk.Button(frame, text = "Report",command=view_report, width="22", bd = '3', font = ('Times', 12, 'bold'), bg='#7268A6',fg='white', relief='groove', justify = 'center', pady='8')
register.grid(row=4,column=10)

# Quit Button of main frame 

def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        top.destroy()
    else:
        pass
    
Quit = tk.Button(top, text = "Quit", width="10", command = Quit, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.775)

# Displyaing Widget to Screen
top.mainloop()


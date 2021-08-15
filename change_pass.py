from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import pymysql as db 
import hashlib

# Creating Input
def password_change():
    
    # Creating a new window
    pass_change = tk.Tk()
    pass_change.geometry('500x500')
    pass_change.title('Change Password')

    # Background Colors
    pass_change.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    pass_change.iconbitmap('img/loginlogo.ico')

    # Top Frame
    top_frame = Label(pass_change, text='Change Password',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(pass_change, padx=40, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Creating function for connecting to database and checking username
    def Search1():
        global t
        global a2  
        global hid     
        t  = str(username_entry.get()) 
        t1 = str(password_entry.get())   
        result2=hashlib.md5(t1.encode())
        a2=result2.hexdigest()
        h=(t,a2)  
        f1=c_password_entry.get()  
        f2=hashlib.md5(f1.encode())
        f3=f2.hexdigest()
        con = db.connect(host="localhost", user="root", password="", database="hms")
        y = ("select * from stu_login where name =%s and password =%s ")  #here %s will get the data
        cur = con.cursor()
        result=cur.execute(y,h)
        if result==True:
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            row=cur.fetchall()
            hid=row[0][0]
            query = "update `stu_login` set `password`= '{}' where hstl_id={}".format(f3,hid)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            ms.showinfo('Success','Successfully Updated')
            cursor.close()
            conn.close()    
        else:
            ms.showerror('error','Invalid Credential')
       
                
            
    # creating a label for username and password using Label 
    username = tk.Label(frame, text = 'Username',font=('Arial',12, 'bold'),bg='white', fg='green')
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'),bg='white', fg='green') 
    c_password = tk.Label(frame, text = 'New Password', font = ('Arial',12,'bold'),bg='white', fg='green') 
  
    global r
    global r1
    global r2
    r=StringVar()
    r1=StringVar()
    r2=StringVar()
    # creating a entry for username 
    username_entry = tk.Entry(frame, font=('calibre',10,'normal'),textvariable=r, justify = 'center', bg='#FBB13C')
    username_entry.bind('<Return>', Search1)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'),textvariable=r1, show = '*', justify = 'center', bg='#FBB13C') 
    password_entry.bind('<Return>', Search1)
    c_password_entry=tk.Entry(frame, font = ('calibre',10,'normal'),textvariable=r2, show = '*', justify = 'center', bg='#FBB13C') 
    c_password_entry.bind('<Return>', Search1)
    # Button that will call the submit function  
    change=tk.Button(frame,text = 'Change Password', command = Search1, width="15",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 
    
    # Placing the label and entry   
    username.pack()
    username_entry.focus_set()
    username_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    c_password.pack() 
    c_password_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    change.pack()
    
    # Quit Button

    Quit = tk.Button(pass_change, text = "Quit", width="10", command = pass_change.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
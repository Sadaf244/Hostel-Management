
# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import os
import re
from datetime import date
from tkcalendar import DateEntry
import tkinter as tk
import pymysql as db 
from s_login import S_Log
from PIL import ImageTk, Image
import hashlib

# Creating register function
def Register():
    global p8
    global p5
    global p4
    def isValid(p8):
        
        reg="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        Pattern = re.compile(reg)
        return Pattern.match(p8)
    def test_name1(str):
        flag = 0
        for i in str:
            if not(i.isalpha() or i == " " or i == "."):
                flag = 1
                break
        if flag == 1:
            return True
        else:
            return False
    def calculateAge(dob):
        d1=dob.split('-')
        y=int(d1[0])
        m=int(d1[1])
        d=int(d1[2])
        birthDate=date(y,m,d)
        today = date.today()
        age=today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
        return age
    def test_age1(str):
        flag = 0
        for i in str:
            if not(i.isnumeric()):
                flag = 1
                break
        if flag == 1:
            return True
        else:
            return False

    def isValid_email(p5):
        Email1 = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        return Email1.match(p5)
    def isValid_no(p4):
        Number= re.compile("^[7-9]\d{9}$")
        return Number.match(p4)
    Reg = tk.Tk()
    Reg.title('Register in System')
    Reg.geometry('700x700')

    # Background Colors
    Reg.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    Reg.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(Reg, text='Registration',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Reg, padx=300, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    # ecting to database with registration form
    def database(arg=None):
      
        # Getting entries
        p1 = name_entry.get()
        p2 = Duration_entry.get()
        p3 = Course_reg_no_entry.get()
        p4 = contact_entry.get()
        p5 = email_entry.get()
        p6 = age_entry.get()
        p7= gender.get()
        p8 = password_entry.get()
        r2=hashlib.md5(p8.encode())
        r1=r2.hexdigest()
        p9 = id_proof_entry.get()
        
        if (name_entry.get() == "" or Duration_entry.get() == "" or Course_reg_no_entry.get() == "" or contact_entry.get() == "" or email_entry.get() == "" or age_entry.get() == "" or password_entry.get() == "" or id_proof_entry.get() == ""):
            ms.showerror("Error !", "All Fields are Required !")
        
        elif test_name1(p1.strip()):
            ms.showinfo("alert","name only contain alphabet, space and .") 
        elif not(isValid(p8)):
            ms.showinfo("alert","Password is not in correct format")
        elif not(isValid_email(p5)):
            ms.showinfo("alert","Email is not in correct format")
        elif not(isValid_no(p4)):
            ms.showinfo("alert","Phone Number is not in correct format")
        elif calculateAge(age_entry.get())<18:
            ms.showinfo("information","you are not valid")
        else:
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()
            
            cur.execute('INSERT INTO stu_login (name,Duration,Course_reg,contact,email,age,gender,password,id_proof) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(p1,p2,p3,p4,p5,p6,p7,r1,p9))
            
            
            con.commit()
            
            
            S_Log()
            con.close()
            cur.close()
        
    
    # creating a label for contact and email using Label
    name = tk.Label(frame, text = 'Full Name', font=('Arial',12, 'bold'), bg='white', fg='green')
    Duration = tk.Label(frame, text = 'Duration', font=('Arial',12, 'bold'), bg='white', fg='green')
    Course_reg_no = tk.Label(frame, text = 'Course reg No.', font=('Arial',12, 'bold'), bg='white', fg='green')
    contact = tk.Label(frame, text = 'Contact', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    email = tk.Label(frame, text = 'Email', font = ('Arial',12,'bold'), bg='white', fg='green')
    age = tk.Label(frame, text = 'Age', font=('Arial',12, 'bold'), bg='white', fg='green')
    Gender = tk.Label(frame, text = 'Gender', font=('Arial',12, 'bold'), bg='white', fg='green')
    password = tk.Label(frame, text = 'Password', font=('Arial',12, 'bold'), bg='white', fg='green')
    id_proof = tk.Label(frame, text = 'Id-Proof', font=('Arial',12, 'bold'), bg='white', fg='green')
    # creating a entry for elements and returning values to the databse function
    name_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    name_entry.bind("<Return>", database)
    Duration_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    Duration_entry.bind("<Return>",database)
    Course_reg_no_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    Course_reg_no_entry.bind("<Return>",database)
    contact_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    contact_entry.bind("<Return>",database)
    a=StringVar()
    email_entry=tk.Entry(frame,textvariable=a, font = ('Arial',12,'normal'), bg='#FBB13C')
    email_entry.bind("<Return>",database)
    age_entry=DateEntry(frame,font=('Arial',12,'normal'), bg='white',date_pattern='yyyy-MM-dd')
    age_entry.bind("<Return>",database)
    gender=StringVar()   
    gender_entry1=tk.Radiobutton(frame,text="male" , value="male",variable=gender, font = ('Arial',12,'normal'), bg='#FBB13C')
    gender_entry1.bind("<Return>",database)
    gender_entry2=tk.Radiobutton(frame,text="female" , value="female",variable=gender, font = ('Arial',12,'normal'), bg='#FBB13C')
    gender_entry2.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#FBB13C')
    password_entry.bind("<Return>",database)
    id_proof_entry=tk.Entry(frame, font = ('Arial',12,'normal'), bg='#FBB13C')
    id_proof_entry.bind("<Return>",database)
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Register', command = database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    name.grid(row=0,column=0)
    name_entry.focus_set()
    name_entry.grid(row=0,column=1)
    
    # Label for seperating Buttons
    
    
    Duration.grid(row=1,column=0)
    Duration_entry.grid(row=1,column=1)

    # Label for seperating Buttons
    
    Course_reg_no.grid(row=2,column=0)
    Course_reg_no_entry.grid(row=2,column=1)
    # Label for seperating Buttons
    
    
    contact.grid(row=3,column=0)
    contact_entry.grid(row=3,column=1)
    # Label for seperating Buttons
   
    
    email.grid(row=4,column=0)
    email_entry.grid(row=4,column=1)
   
    # Label for seperating Buttons
    
    
    age.grid(row=5,column=0)
    age_entry.grid(row=5,column=1)
    # Label for seperating Buttons
    
    
    Gender.grid(row=6,column=0)
    gender_entry1.grid(row=6,column=1)
    gender_entry2.grid(row=6,column=2)
    # Label for seperating Buttons
    
    password.grid(row=7,column=0)
    password_entry.grid(row=7,column=1)
    # Label for seperating Buttons
    
    id_proof.grid(row=8,column=0)
    id_proof_entry.grid(row=8,column=1)
    # Label for seperating Buttons
    
    
    submit.grid(row=10,column=1)

    # Quit Button

    Quit = tk.Button(Reg, text = "Quit", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)

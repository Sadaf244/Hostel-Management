
# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import pymysql as db 
import hashlib
import smtplib, ssl
import os,math
import random,sys
# Creating Input
global s

def S_Log():
    
    # Creating a new window
    Login = tk.Tk()
    Login.geometry('500x500')
    Login.title('Login to System !')

    # Background Colors
    Login.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    Login.iconbitmap('img/loginlogo.ico')

    # Top Frame
    top_frame = Label(Login, text='Login To System',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Login, padx=40, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    def forget_password(arg=None):
        Forget = tk.Tk()
        Forget.geometry('500x500')
        Forget.title('Forget Password !')

    # Background Colors
        Forget.configure(background='#3B2C35')
        Forget.iconbitmap('img/loginlogo.ico')
        top_frame = Label(Forget, text='Forget Password',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
        top_frame.pack(side='top')
        frame1 = LabelFrame(Forget, padx=60, pady=60, bg='white')
        frame1.place(relx = 0.5, rely = 0.55, anchor = CENTER)
        enter_email = tk.Label(frame1, text = 'Enter your Email',font=('Arial',12, 'bold'),bg='white', fg='green')
        global enter_email_entry
        enter_email_entry=StringVar()
        
        enter_email_entry = tk.Entry(frame1, font=('calibre',15,'normal'), justify = 'center',width="40", bg='#FBB13C')
        enter_email_entry.bind('<Return>', search_pass)
        enter_email.pack()
        enter_email_entry.focus_set()
        enter_email_entry.pack()
 
        label = Label(frame1, bg='white').pack()
        forget_pass1=tk.Button(frame1,text = 'Forget Password', command = search_pass, width="15",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5')
        forget_pass1.pack()
        Quit = tk.Button(Forget, text = "Quit", width="10", command = Forget.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
        Quit.place(anchor ='sw',rely=1,relx=0.775)
    def search_pass(arg=None):
        if (enter_email_entry.get() ==''): 
            ms.showerror('Oops', 'Enter Email !!')
        else:
            e=enter_email_entry.get()
            
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()
            y = "select * from stu_login where email ='{}'".format(e)  
            result=cur.execute(y)
            row=cur.fetchall()
            t=StringVar()
            t=row[0][5]
            n=StringVar()
            n=row[0][1]
            hid=StringVar()
            hid=row[0][0]
            con.commit()
            digits="absdef012@3456ghijkl789"
            OTP=""
            for i in range(8):
                OTP+=digits[math.floor(random.random()*10)]
            f1=OTP  
            f2=hashlib.md5(f1.encode())
            f3=f2.hexdigest()
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()
            query = "update `stu_login` set `password`= '{}' where hstl_id={}".format(f3,hid) 
            cur.execute(query)
            con.commit()    
            con.close()
            cur.close()
            if result==True:
                port = 465 
                smtp_server = "smtp.gmail.com"
                sender_email = ""  # Enter your address
                receiver_email = t  
                password =''
                message = """\
                Subject: Hi """+n+"""

                Your New Password is """+OTP+""" Message is sent by Nielit"""

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
            else:
                ms.showerror('error','Invalid Email ID')
    # Creating function for connecting to database and checking username
    def Search(arg = None):
        
        if (username_entry.get() =='' or password_entry.get() == ''): 
            ms.showerror('Oops', 'Enter Username !!')    
        else:
            global t
            t = str(username_entry.get())
            global t1
            global s5
            global s6
            global result
            global w2
            t1 = str(password_entry.get())
            w1=hashlib.md5(t1.encode())
            w2=w1.hexdigest()
            h=(t,w2)
            # Making connection
            #conn = sqlite3.connect('Database.db')
            con = db.connect(host="localhost", user="root", password="", database="hms")
            y = ("select * from stu_login where name = %s and password =%s ")  #here %s will get the data
            cur = con.cursor()
            result=cur.execute(y,h)
            row=cur.fetchall() 
    
            
            # Creating cur
            

            # Searching for users
            
            

            # if user then new window
            if result==True:
                s5=row[0][0]
                s6=row[0][1]
                import s_main_screen2
                
            else:
                ms.showerror('error','login fail')
       
                # Showing Result
                #label = tk.Label(result, text = 'Hi '+ username +'\nThank You For Using Our System !!!!',font=('Arial',12, 'bold'),bg='white', fg='green').place(relx = 0.5, rely = 0.5, anchor = CENTER)

            # if user do not exist
            
    # creating a label for username and password using Label 
    username = tk.Label(frame, text = 'Username',font=('Arial',12, 'bold'),bg='white', fg='green')
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'),bg='white', fg='green')   
    global r
    global r1
    r=StringVar()
    r1=StringVar()
    # creating a entry for username 
    username_entry = tk.Entry(frame, font=('calibre',10,'normal'),textvariable=r, justify = 'center', bg='#FBB13C')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'),textvariable=r1, show = '*', justify = 'center', bg='#FBB13C') 
    password_entry.bind('<Return>', Search)
    
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Login', command = Search, width="10",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 
    forget_pass=tk.Button(frame,text = 'Forget Password', command = forget_password, width="15",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 
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
    
    submit.pack()
    label = Label(frame, bg='white').pack()
    forget_pass.pack()
    # Quit Button

    Quit = tk.Button(Login, text = "Quit", width="10", command = Login.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
def profile_view():
    global s
    V_prof = tk.Tk()
    V_prof.title('View Profile')
    V_prof.geometry('700x700')

    # Background Colors
    V_prof.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    V_prof.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(V_prof, text='View Profile',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(V_prof, padx=300, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    
    
    t2=StringVar()
    t2=s5
       
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    y = ("select * from stu_login where hstl_id =%s ")  #here %s will get the data
    cursor = conn.cursor()
    result=cursor.execute(y,t2)
    conn.commit()
    row=cursor.fetchall() 
    s=row[0][0]
    a=row[0][2]
    b=row[0][3]
    c=row[0][4]
    global d
    d=row[0][5]
    e=row[0][6]
    f=row[0][7]
    g=row[0][9]
    h=row[0][1]
    
    conn.close()
    cursor.close()
    
    hstl = tk.Label(frame, text = 'Hostel Id', font=('Arial',12, 'bold'), bg='white', fg='green')
    hstl_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    #view_Profile=tk.Button(frame,text = 'View Profile', command = prof, width="15",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 
    name = tk.Label(frame, text = 'Name', font=('Arial',12, 'bold'), bg='white', fg='green')
    name_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    Duration = tk.Label(frame, text = 'Duration', font=('Arial',12, 'bold'), bg='white', fg='green')
    Duration_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    Course_no = tk.Label(frame, text = 'Course Reg No.', font=('Arial',12, 'bold'), bg='white', fg='green')
    Course_no_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    contact = tk.Label(frame, text = 'Contact', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    contact_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    email = tk.Label(frame, text = 'Email', font = ('Arial',12,'bold'), bg='white', fg='green')
    email_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    age = tk.Label(frame, text = 'Age', font=('Arial',12, 'bold'), bg='white', fg='green')
    age_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    Gender = tk.Label(frame, text = 'Gender', font=('Arial',12, 'bold'), bg='white', fg='green')
    Gender_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    id_proof = tk.Label(frame, text = 'Id-Proof', font=('Arial',12, 'bold'), bg='white', fg='green')
    id_proof_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    # creating a entry for elements and returning values to the databse function
    
    hstl.grid(row=0,column=0)
    hstl_entry.grid(row=0,column=1)  
    # Button that will call the submit function 
    # label = Label(frame, bg='white').pack() 
    #view_Profile.pack()
    # Placing the label and entry
    name.grid(row=1,column=0)
    name_entry.grid(row=1,column=1)
    
    # Label for seperating Buttons
    
    
    Duration.grid(row=2,column=0)
    Duration_entry.grid(row=2,column=1)

    # Label for seperating Buttons
   
    
    Course_no.grid(row=3,column=0)
    Course_no_entry.grid(row=3,column=1)

    # Label for seperating Buttons
   
    
    contact.grid(row=4,column=0)
    contact_entry.grid(row=4,column=1)

    # Label for seperating Buttons
   
    
    email.grid(row=5,column=0)
    email_entry.grid(row=5,column=1)

    # Label for seperating Buttons
   
    
    age.grid(row=6,column=0)
    age_entry.grid(row=6,column=1)
    # Label for seperating Buttons
    
    
    Gender.grid(row=7,column=0)
    Gender_entry.grid(row=7,column=1)
    
    
    # Label for seperating Buttons
    
    
    id_proof.grid(row=8,column=0)
    id_proof_entry.grid(row=8,column=1)


    hstl_entry.insert(0,s)
    name_entry.insert(0,h)
    Duration_entry.insert(0,a)
    Course_no_entry.insert(0,b)
    contact_entry.insert(0,c)
    email_entry.insert(0,d)
    age_entry.insert(0,e)
    Gender_entry.insert(0,f)
    id_proof_entry.insert(0,g)
    
    # Quit Button

    Quit = tk.Button(V_prof, text = "Quit", width="10",command = V_prof.destroy,  bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84) 

def stu_alloc_date():
    aloc_date =tk.Tk()
    aloc_date.title('Room Allocation Details')
    aloc_date.geometry('700x700')

    # Background Colors
    aloc_date.configure(background='#3B2C35')

    # Locking the window size
    aloc_date.resizable(width=False, height=False)

    # Creating title icon
    aloc_date.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(aloc_date, text='Room Allocation Details',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = tk.LabelFrame(aloc_date, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    y1=StringVar()
    y1=str(s5) 
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    y = ("select * from room_aloc where hstl_id =%s ")  #here %s will get the data
    cursor = conn.cursor()
    result=cursor.execute(y,y1)
    conn.commit()
    row=cursor.fetchall() 
    date_aloc=row[0][6]
    room_no_aloc=row[0][3]
    conn.close()
    cursor.close()
       
    # creating a label for contact and email using Label
    date1 = tk.Label(frame, text = 'Allocation Date and Time', font=('Arial',12, 'bold'), bg='white', fg='green')
    date1_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    # Label for seperating Buttons
    
    room_no = tk.Label(frame, text = 'Room No', font=('Arial',12, 'bold'), bg='white', fg='green')
    room_no_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    
    date1.pack()
    date1_entry.pack()
    label = Label(frame, bg='white').pack()
    room_no.pack()
    room_no_entry.pack()
    label = Label(frame, bg='white').pack()
    date1_entry.insert(0,date_aloc)
    room_no_entry.insert(0,room_no_aloc)
    Quit = tk.Button(aloc_date, text = "Quit", width="10",command = aloc_date.destroy,  bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84) 

def room_complain():
    
    query1 =tk.Tk()
    query1.title('Complain Or Query')
    query1.geometry('700x700')

    # Background Colors
    query1.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    query1.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(query1, text='Complain or Query',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    v1=StringVar()
    v2=StringVar()
    v1=s5
    v2=s6
    # Creating Frame
    frame = tk.LabelFrame(query1, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # ecting to database with registration form
    def rum_complain():
        p1 = subject_entry.get()
        p2 = description_entry.get(0.0,END)
        
        
        if (subject_entry.get() == "" or description_entry == "" ):
            ms.showerror("Error !", "All Fields are Required !")
       
        else:
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()
            
            cur.execute('INSERT INTO message_box (hstl_id,name,subject,description) VALUES (%s,%s,%s,%s)',(v1,v2,p1,p2))
            con.commit()
            ms.showinfo("Success ", "Successfully Added ")
            con.close()
            cur.close()
    
    
    # creating a label for contact and email using Label
    subject = tk.Label(frame, text = 'Subject', font=('Arial',12, 'bold'), bg='white', fg='green')
    description =tk.Label(frame, text = 'Description', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    
    
    subject_entry =tk.Entry(frame,font=('Arial',12,'normal'), bg='white')
  
    description_entry =tk.Text(frame,height=10,width=20,font=('Arial',12,'normal'), bg='white')
    
    
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Submit',command=rum_complain,width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    subject.pack()
    subject_entry.focus_set()
    subject_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    description.pack()
    description_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit =tk.Button(query1, text = "Quit",command=query1.destroy, width="10", bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)


        
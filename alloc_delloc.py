from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import datetime
import smtplib, ssl
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def aloc_deloc():
    global tkvar3
    # Creating a new window
    
    aloc =tk.Tk()
    aloc.title('Room Allocation')
    aloc.geometry('700x700')

    # Background Colors
    aloc.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    aloc.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(aloc, text='Room Allocation',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = tk.LabelFrame(aloc, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # ecting to database with registration form
    def aloc_database(arg=None):
        global a1
        global a2
        a4=now.strftime("%d-%m-%Y %H:%M:%S")
        
        stu_name_info1 = sel_stu_entry.get()
        stu_name_info2 = stu_name_info1.split("-")
        a1 = int(stu_name_info2[0])
        a0 = stu_name_info2[1]
        a2 = str(sel_room_entry.get())
        a5=sel_person_entry.get()
        a3 = remarks_entry.get()
        
        if (sel_stu_entry.get() == "" or sel_room_entry.get() == "" or remarks_entry.get() == "" ):
            ms.showerror("Error !", "All Fields are Required !")
       
        else:
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()

            qr="INSERT INTO room_aloc (hstl_id,name,room_no,person,remark,a_date) VALUES (%d,'%s','%s','%s','%s','%s')"%(a1,a0,a2,a5,a3,a4)
            result1=cur.execute(qr)
            
            
            con.commit()
            
            ms.showinfo("Success ", "Successfully Added ")
            con.close()
            cur.close()
            if result1==True:
                conn = db.connect(host='localhost', user='root', password='', db='hms')
                y = ("select * from stu_login where hstl_id =%s ")  #here %s will get the data
                cursor = conn.cursor()
                result=cursor.execute(y,a1)
                conn.commit()
                row=cursor.fetchall() 
                s=row[0][5]
                n=row[0][1]
                port = 465 
                smtp_server = "smtp.gmail.com"
                sender_email = ""  # Enter your address
                receiver_email = s  
                password =''
                message = """\
                Subject: Hi """+n+"""

                Successfully Allocated your Room No. """+format(a2)+""" Message is sent by Nielit"""
                
               
                

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
            else:
                ms.showerror('error','not allocated')

    def printemp1(event):
        
        listperson=['-select person-']
        con=db.connect(host='localhost',user='root',password='',db='hms')
        query="select * from room where room_no='{}'".format(sel_room_entry.get())
        cur=con.cursor()
        cur.execute(query)
        row=cur.fetchone()
        listperson.append(row[4])
        sel_person_entry['values']=listperson
        
        
        cur.close()
        con.close()
    
    # creating a label for contact and email using Label
    
    tkvar=StringVar()
    # database code start
    liststu=['--select student--']
    con=db.connect(host='localhost',user='root',password='',db='hms')
    query="select * from  stu_login where allocation_status=0" 
    cur=con.cursor()
    cur.execute(query)
    row=cur.fetchall()
    
    for i in row:
        stuid_name = str(i[0]) + "-" + i[1]
        liststu.append(stuid_name)
        

    con.commit()
    cur.close()
    con.close()
    #end db code
    slr=liststu
    sel_stu = tk.Label(frame, text = 'Select Student', font=('Arial',12, 'bold'), bg='white', fg='green')
    sel_room = tk.Label(frame, text = 'Select ROOM', font=('Arial',12, 'bold'), bg='white', fg='green')
    sel_person=tk.Label(frame, text = 'Vacant Seat', font=('Arial',12, 'bold'), bg='white', fg='green')
    sel_date = tk.Label(frame,text = 'Date', font=('Arial',12, 'bold'), bg='white', fg='green')
    remarks =tk. Label(frame, text = 'Remarks', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    
    # creating a entry for elements and returning values to the databse function
    sel_stu_entry = ttk.Combobox(frame ,state="readonly",font=('Arial',12,'normal'),textvariable=tkvar,value=slr)
    sel_stu_entry.bind("<Return>",aloc_database)
    tkvar2=StringVar()
    # database code start
    listrumm=['--select room--']
    con=db.connect(host='localhost',user='root',password='',db='hms')
    query="select  room_no from room where person > 0 order by room_no asc"  
    cur=con.cursor()
    cur.execute(query)
    row=cur.fetchall()
    for i in row:
        listrumm.append(i[0])

    con.commit()
    cur.close()
    con.close()
    #end db code
    slr2=listrumm
    sel_room_entry = ttk.Combobox(frame,state="readonly",font=('Arial',12,'normal'),textvariable=tkvar2,value=slr2)
    sel_room_entry.bind("<Return>",aloc_database)
    sel_room_entry.bind('<<ComboboxSelected>>',printemp1)

    tkvar3=StringVar()
    sel_person_entry = ttk.Combobox(frame,state="readonly",font=('Arial',12,'normal'),textvariable=tkvar3)
    sel_person_entry.bind("<Return>",aloc_database)
    now = datetime.datetime.now()
    now_date=now.strftime("%d-%m-%Y %H:%M:%S")
    sel_date_result=tk.Label(frame,text = now_date, font=('Arial',12, 'bold'), bg='white', fg='red')
    sel_date_result.bind("<Return>",aloc_database)
    remarks_entry =tk.Entry(frame,font=('Arial',12,'normal'), bg='white')
    remarks_entry.bind("<Return>",aloc_database)
    
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Allocation ', command = aloc_database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    sel_stu.pack()
    sel_stu_entry.focus_set()
    sel_stu_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    sel_room.pack()
    sel_room_entry.pack()
# Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    sel_person.pack()
    sel_person_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    remarks.pack()
    remarks_entry.pack()

    # Label for seperating Buttons
    
    label = Label(frame,bg='white').pack()
    sel_date.pack()

    sel_date_result.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit =tk.Button(aloc, text = "Quit", width="10", command = aloc.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
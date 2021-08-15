from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import tkinter.ttk as ttk
import datetime
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def deloc():
    def deloc_database(arg=None):
        a4=now.strftime("%d-%m-%Y %H:%M:%S")
        stu_name_info1 = sel_stu_entry.get()
        stu_name_info2 = stu_name_info1.split("-")
        a1 = int(stu_name_info2[0])
        a0 = stu_name_info2[1]
        a2 = str(sel_room_entry.get())
        a3 = remarks_entry.get()
        
        if (sel_stu_entry.get() == "" or sel_room_entry.get() == "" or remarks_entry.get() == "" ):
            ms.showerror("Error !", "All Fields are Required !")
       
        else:
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()
            qr="INSERT INTO room_delocate (hstl_id,name,room_no,remark,d_date) VALUES (%d,'%s','%s','%s','%s')"%(a1,a0,a2,a3,a4)
            cur.execute(qr)
            
            
            con.commit()
            
            ms.showinfo("Success ", "Successfully Deallocated ")
            con.close()
            cur.close()
    
    
    aloc =tk.Tk()
    aloc.title('Room Deallocation')
    aloc.geometry('700x700')

    # Background Colors
    aloc.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    aloc.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(aloc, text='Room Deallocation',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = tk.LabelFrame(aloc, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # ecting to database with registration form
    def room_bind(event):
       
        listroom1=['-select room-']
        stu_name_info1 = sel_stu_entry.get()
        stu_name_info2 = stu_name_info1.split("-")
        a1 = stu_name_info2[1]
        con=db.connect(host='localhost',user='root',password='',db='hms')
        query="select * from room_aloc where name='{}'".format(a1)
        
        cur=con.cursor()
        cur.execute(query)
        row=cur.fetchall()
        for i in row:
            listroom1.append(i[3])
        
        sel_room_entry['values']=listroom1
    
        con.commit()
        cur.close()
        con.close()
    
    
    
    # creating a label for contact and email using Label
    
    tkvard=StringVar()
    # database code start
    liststu1=['--select student--']
    con=db.connect(host='localhost',user='root',password='',db='hms')
    query="select * from room_aloc" 
    cur=con.cursor()
    cur.execute(query)
    row=cur.fetchall()
    for i in row:
        stuid1_name=str(i[1]) + "-" + i[2] 
        liststu1.append(stuid1_name)
    con.commit()
    cur.close()
    con.close()
    #end db code
    dlr=liststu1
    sel_stu = tk.Label(frame, text = 'Select Student', font=('Arial',12, 'bold'), bg='white', fg='green')
    sel_room = tk.Label(frame, text = 'Select ROOM', font=('Arial',12, 'bold'), bg='white', fg='green')
    sel_date1 = tk.Label(frame, text = 'Date', font=('Arial',12, 'bold'), bg='white', fg='green')
    remarks =tk. Label(frame, text = 'Remarks', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    
    # creating a entry for elements and returning values to the databse function
    sel_stu_entry = ttk.Combobox(frame ,font=('Arial',12,'normal'),textvariable=tkvard,value=dlr)
    
    sel_stu_entry.bind('<<ComboboxSelected>>',room_bind)
    tkvard2=StringVar()
    sel_room_entry = ttk.Combobox(frame,font=('Arial',12,'normal'),textvariable=tkvard2)
    now = datetime.datetime.now()
    now_date=now.strftime("%d-%m-%Y %H:%M:%S")
    sel_date_result1=tk.Label(frame,text = now_date, font=('Arial',12, 'bold'), bg='white', fg='red')
    sel_date_result1.bind("<Return>",deloc_database)
    remarks_entry =tk.Entry(frame,font=('Arial',12,'normal'), bg='white')
   
    
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Deallocation ',command=deloc_database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
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
    
    remarks.pack()
    remarks_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    sel_date1.pack()
    sel_date_result1.pack()

    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit =tk.Button(aloc, text = "Quit", width="10", command = aloc.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
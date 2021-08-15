
# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 

import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def room_registry():
    
    # Creating a new window
    
    Rum =tk.Tk()
    Rum.title('Room Entry')
    Rum.geometry('700x700')

    # Background Colors
    Rum.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    Rum.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(Rum, text='Room Entry',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = tk.LabelFrame(Rum, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # ecting to database with registration form
    def rum_database(arg=None):
      
        # Getting entries
        p1 = room_entry.get()
        p2 = floor_entry.get()
        p3 = rent_entry.get()
        p4 = person_entry.get()
        

        if (floor_entry.get() == "" or room_entry.get() == "" or rent_entry.get() == "" or person_entry.get() == "" ):
            ms.showerror("Error !", "All Fields are Required !")
       
        else:
            con = db.connect(host="localhost", user="root", password="", database="hms")
            cur = con.cursor()
            
            cur.execute('INSERT INTO room (room_no,floor_no,rent,person) VALUES (%s,%s,%s,%s)',(p1,p2,p3,p4))
            
            
            con.commit()
            
            ms.showinfo("Success ", "Successfully Added ")
            con.close()
            cur.close()
    def printemp(event):
    
        listroom=['-select room-']
        con=db.connect(host='localhost',user='root',password='',db='hms')
        query="select * from room where floor_no='{}'".format(floor_entry.get())
        cur=con.cursor()
        cur.execute(query)
        row=cur.fetchall()
        for i in row:
            listroom.append(i[1])
        
        room_entry['values']=listroom
    
        con.commit()
        cur.close()
        con.close()
    
    # creating a label for contact and email using Label
    floor = tk.Label(frame, text = 'Floor', font=('Arial',12, 'bold'), bg='white', fg='green')
    tkvar=StringVar()
    # database code start
    listfloor=['--select floor--']
    con=db.connect(host='localhost',user='root',password='',db='hms')
    query="select distinct floor_no from room" 
    cur=con.cursor()
    cur.execute(query)
    row=cur.fetchall()
    for i in row:
        listfloor.append(i[0])

    con.commit()
    cur.close()
    con.close()
    #end db code
    flr=listfloor
    room = tk.Label(frame, text = 'Room', font=('Arial',12, 'bold'), bg='white', fg='green')
    rent = tk.Label(frame, text = 'Rent', font=('Arial',12, 'bold'), bg='white', fg='green')
    person =tk. Label(frame, text = 'No. Of Person', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    
    # creating a entry for elements and returning values to the databse function
    floor_entry = ttk.Combobox(frame ,font=('Arial',12,'normal'),textvariable=tkvar,value=flr)
    floor_entry.bind("<Return>",rum_database)
    floor_entry.bind('<<ComboboxSelected>>',printemp)
    tkvar2=StringVar()
    room_entry = ttk.Combobox(frame,font=('Arial',12,'normal'),textvariable=tkvar2)
    room_entry.bind("<Return>",rum_database)
    rent_entry =tk.Entry(frame,font=('Arial',12,'normal'), bg='white')
    rent_entry.bind("<Return>",rum_database)
    person_entry =tk.Spinbox(frame,from_=0, to=100,font=('Arial',12,'normal'), bg='white')
    person_entry.bind("<Return>",rum_database)
    
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Submit', command = rum_database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    floor.pack()
    floor_entry.focus_set()
    floor_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    room.pack()
    room_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    rent.pack()
    rent_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    person.pack() 
    person_entry.pack()

    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit =tk.Button(Rum, text = "Quit", width="10", command = Rum.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)

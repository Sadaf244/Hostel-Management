from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
from tkcalendar import DateEntry
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def view_report():
    global tkvar4
    def room_report(arg=None):
        a=str(Report_entry.get())
        if a == 'Room wise':
            s=str(To_date_entry.get())
            f=str(Fr_date_entry.get())
            updatewindow = Toplevel()
            updatewindow.configure(background='#3B2C35')
            updatewindow.title("Roomwise Report Panel")
            updatewindow.geometry("600x300")
            frame = LabelFrame(updatewindow, padx=30, pady=30, bg='white')
            frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
            scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
            scrollbary = Scrollbar(frame, orient=VERTICAL)
            tree=ttk.Treeview(frame,columns=("v","a"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('v',text="Room No.")
            tree.heading('a',text="Count(room_no)")
            tree.column('#0', minwidth="0", width=0)
            tree.column('#1', anchor='center')
            tree.column('#2', anchor='center')
        
            tree.pack()
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            query = "SELECT room_no,COUNT(room_no) AS COUNT_room FROM room_aloc WHERE a_date BETWEEN '{}' AND '{}' GROUP BY room_no".format(s,f)
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            for i in row:
                tree.insert('', 'end', values=(i))
        if a=='gender wise':
            s=str(To_date_entry.get())
            f=str(Fr_date_entry.get())
            updatewindow = Toplevel()
            updatewindow.configure(background='#3B2C35')
            updatewindow.title("Genderwise Report Panel")
            updatewindow.geometry("600x300")
            frame = LabelFrame(updatewindow, padx=30, pady=30, bg='white')
            frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
            scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
            scrollbary = Scrollbar(frame, orient=VERTICAL)
            tree=ttk.Treeview(frame,columns=("v","a"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('v',text="Gender")
            tree.heading('a',text="Count(Gender)")
            tree.column('#0', minwidth="0", width=0)
            tree.column('#1', anchor='center')
            tree.column('#2', anchor='center')
        
            tree.pack()
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            query = "SELECT gender,COUNT(gender) from stu_login WHERE hstl_id IN(SELECT hstl_id FROM room_aloc WHERE a_date BETWEEN '{}' AND '{}' )GROUP BY gender".format(s,f)
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            for i in row:
                tree.insert('', 'end', values=(i))

    Rep =tk.Tk()
    Rep.title('Report')
    Rep.geometry('700x700')

    # Background Colors
    Rep.configure(background='#3B2C35')

    # Locking the window size
    Rep.resizable(width=False, height=False)

    # Creating title icon
    Rep.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(Rep, text='Report',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = tk.LabelFrame(Rep, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
 
    # creating a label for contact and email using Label
    To_date = tk.Label(frame, text = 'From', font=('Arial',12, 'bold'), bg='white', fg='green')
    Fr_date = tk.Label(frame, text = 'To', font=('Arial',12, 'bold'), bg='white', fg='green')
    Report = tk.Label(frame, text = 'Report By', font=('Arial',12, 'bold'), bg='white', fg='green')
    
    

    To_date_entry =DateEntry(frame,font=('Arial',12,'normal'),bg='white',date_pattern='dd-MM-yyyy')
    #To_date_entry.bind("<Return>",room_report)
    
    
    Fr_date_entry =DateEntry(frame,font=('Arial',12,'normal'), bg='white',date_pattern='dd-MM-yyyy')
    
    #Fr_date_entry.bind("<Return>",room_report)
    
    tkvar4=StringVar()
    Report_entry = ttk.Combobox(frame,font=('Arial',12,'normal'),textvariable=tkvar4)
    Report_entry['values'] = ('gender wise','Room wise') 
    Report_entry.current()
    submit=tk.Button(frame,command=room_report,text = 'Submit', width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
       
    # Placing the label and entry
    To_date.pack()
    To_date_entry.focus_set()
    To_date_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    Fr_date.pack()
    Fr_date_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    Report.pack()
    Report_entry.pack()

    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit =tk.Button(Rep, text = "Quit", width="10", command = Rep.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import tkinter.ttk as ttk
from report import view_report
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def room_report():
    print(To_date_entry)
    print(Fr_date_entry)
    repo =tk.Tk()
    repo.title('View Student Allocation')
    repo.geometry('900x700')

    # Background Colors
    repo.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    repo.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(repo, text='View report',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame=Frame(repo, height="10", width="100")
    frame.pack()
    scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame, orient=VERTICAL)
    # ecting to database with registration form
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
    tree.column('#3',  anchor=W)
    tree.pack()
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    query = "SELECT room_no,COUNT(room_no) AS COUNT_room FROM room_aloc WHERE a_date BETWEEN 'To_date_entry' AND 'Fr_date_entry' GROUP BY room_no"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    for i in row:
        tree.insert('', 'end', values=(i))
    conn.commit()
    cursor.close()
    conn.close()
    repo.mainloop()
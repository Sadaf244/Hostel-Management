from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def view_alloc_room():
    def a_reload_data():
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="select * from room_aloc"
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        cursor.close()
        conn.close()
    def r_search_record1():  
        r1=r_search_entry1.get()
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="SELECT * FROM `room_aloc` WHERE `name` LIKE '%{}%'".format(r1)
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        
        cursor.close()
        conn.close()
    vallocateroom =tk.Tk()
    vallocateroom.title('View Student Allocation')
    vallocateroom.geometry('900x700')

    # Background Colors
    vallocateroom.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    vallocateroom.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(vallocateroom, text='View Student Allocation',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame=Frame(vallocateroom, height="10", width="100")
    frame.pack()
    scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame, orient=VERTICAL)
    # ecting to database with registration form
    tree=ttk.Treeview(frame,columns=("v","a","b","c","d","e","f"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('v',text="Serial No.")
    tree.heading('a',text="Hostel Id")
    tree.heading('b',text="Name.")
    tree.heading('c',text="Room No.")
    tree.heading('d',text="Person.")
    tree.heading('e',text="Remarks.")
    tree.heading('f',text="Date and Time.")
    tree.column('#0', minwidth="0", width=0)
    tree.column('#1', anchor='center')
    tree.column('#2', anchor='center')
    tree.column('#3', anchor='center')
    tree.column('#4', anchor='center')
    tree.column('#5', anchor='center')
    tree.column('#6', anchor='center')
    tree.column('#7', anchor='center')
    tree.pack()
    lb1 = tk.Label(vallocateroom, text="Search:",font=('Arial',12, 'bold'),bg='#3B2C35', fg='green')
    lb1.pack()
    r_search_entry1 = Entry(vallocateroom, width=15,font=('calibre',10,'normal'), justify = 'center', bg='white')
    r_search_entry1.pack()
    r_search_entry1.bind('<Return>', r_search_record1)   
    btn = tk.Button(vallocateroom, text="search",command=r_search_record1,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack() 
    btn = tk.Button(vallocateroom, text="reload",command=a_reload_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()       
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    query = "select * from room_aloc"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    for i in row:
        tree.insert('', 'end', values=(i))
    conn.commit()
    cursor.close()
    conn.close()
    vallocateroom.mainloop()
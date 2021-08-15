from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def view_delloc_room():
    def d_reload_data():
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="select * from room_delocate"
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        cursor.close()
        conn.close()
    def r_search_record2():  
        r2=r_search_entry2.get()
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="SELECT * FROM `room_delocate` WHERE `name` LIKE '%{}%'".format(r2)
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        
        cursor.close()
        conn.close()
    vdeallocateroom =tk.Tk()
    vdeallocateroom.title('View Student Deallocation')
    vdeallocateroom.geometry('900x700')

    # Background Colors
    vdeallocateroom.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    vdeallocateroom.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(vdeallocateroom, text='View Student Deallocation',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame=Frame(vdeallocateroom, height="10", width="100")
    frame.pack()
    scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame, orient=VERTICAL)
    # ecting to database with registration form
    tree=ttk.Treeview(frame,columns=("v","a","b","c","d","e"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('v',text="Serial No.")
    tree.heading('a',text="Hostel Id")
    tree.heading('b',text="Name.")
    tree.heading('c',text="Room No.")
    tree.heading('d',text="Remarks.")
    tree.heading('e',text="Date and Time.")
    tree.column('#0', minwidth="0", width=0)
    tree.column('#1', anchor='center')
    tree.column('#2', anchor='center')
    tree.column('#3', anchor='center')
    tree.column('#4', anchor='center')
    tree.column('#5', anchor='center')
    tree.column('#6', anchor='center')
    tree.pack()
    lb1 = tk.Label(vdeallocateroom, text="Search:",font=('Arial',12, 'bold'),bg='#3B2C35', fg='green')
    lb1.pack()

    r_search_entry2 = Entry(vdeallocateroom, width=15,font=('calibre',10,'normal'), justify = 'center', bg='white')
    r_search_entry2.pack()
    r_search_entry2.bind('<Return>', r_search_record2)   
    btn = tk.Button(vdeallocateroom, text="search",command=r_search_record2,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()
    btn = tk.Button(vdeallocateroom, text="reload",command=d_reload_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()       
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    query = "select * from room_delocate"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    for i in row:
        tree.insert('', 'end', values=(i))
    conn.commit()
    cursor.close()
    conn.close()
    vdeallocateroom.mainloop()
from tkinter import *
from tkinter import messagebox as ms
import pymysql as db
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def view_message():

    def d_reload_data():
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="select * from message_box"
        
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
        query="SELECT * FROM `message_box` WHERE `name` LIKE '%{}%'".format(r2)
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        
        cursor.close()
        conn.close()
    stumsg =tk.Tk()
    stumsg.title('Message Box')
    stumsg.geometry('900x700')

    # Background Colors
    stumsg.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    stumsg.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(stumsg, text='Message Box',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame=Frame(stumsg, height="10", width="200")
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame, orient=VERTICAL)
    # ecting to database with registration form
    tree=ttk.Treeview(frame,columns=("v","a","b","c"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('v',text="Hostel Id.")
    tree.heading('a',text="Name")
    tree.heading('b',text="Subject")
    tree.heading('c',text="Description")
    tree.column('#0', minwidth="0", width=0)
    tree.column('#1', anchor='center')
    tree.column('#2', anchor='center')
    tree.column('#3', anchor='center')
    tree.column('#4',  anchor=W)
    tree.pack()
    lb1 = tk.Label(stumsg, text="Search:",font=('Arial',12, 'bold'),bg='#3B2C35', fg='green')
    lb1.pack()

    r_search_entry2 = Entry(stumsg, width=15,font=('calibre',10,'normal'), justify = 'center', bg='white')
    r_search_entry2.pack()
    r_search_entry2.bind('<Return>', r_search_record2)   
    btn = tk.Button(stumsg, text="search",command=r_search_record2,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()
    btn = tk.Button(stumsg, text="reload",command=d_reload_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()       
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    query = "select * from message_box"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    for i in row:
        tree.insert('', 'end', values=(i))
    conn.commit()
    cursor.close()
    conn.close()
    Quit = tk.Button(stumsg, text = "Quit", width="10", command = stumsg.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
    stumsg.mainloop()
    
    

    
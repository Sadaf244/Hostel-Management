from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def view_room():
    def r_reload_data():
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="select * from room"
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        cursor.close()
        conn.close()
    def r_search_record():  
        r1=r_search_entry.get()
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="SELECT * FROM `room` WHERE `room_no` LIKE '%{}%'".format(r1)
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        cursor.close()
        conn.close()
    def r_del_data():
        if not tree.selection():
            ms.showerror('alert', 'please select atleast one row')
        else:
            curItem = tree.focus()
            content = tree.item(curItem)
            row_data = content['values']
            sl_no1 = row_data[0]
            tree.delete(curItem)
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            query = "delete from room where sl_no={}".format(sl_no1)
            cursor = conn.cursor()
            cursor.execute(query)

            conn.commit()
            ms.showinfo('Success','Successfully Deleted')
            cursor.close()
            conn.close()


    def r_update_data():
        def r_updatefinal(): 
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            query = "update room set `room_no`='{}',`floor_no`='{}',`rent`='{}',`person`='{}' where sl_no={}".format(room.get(), floor.get(), rent1.get(),person_no.get(), slno1)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            ms.showinfo('Success','Successfully Updated')
            cur.close()
            conn.close()
        if not tree.selection():
            ms.showerror('alert', 'please select atleast one row')
        else:
            updatewindow1 = Toplevel()
            updatewindow1.configure(background='#3B2C35')
            updatewindow1.title("update panel")
            updatewindow1.geometry("600x300")
            frame1 = LabelFrame(updatewindow1, padx=30, pady=30, bg='white')
            frame1.place(relx = 0.5, rely = 0.55, anchor = CENTER)
            room = StringVar()
            floor = StringVar()
            rent1 = StringVar()
            person_no = StringVar()
            l1=Label(frame1,text="Room No.",font=('Arial',12, 'bold'),bg='white', fg='green')
            l1.pack()

            u1 = Entry(frame1, textvariable=room,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u1.pack()
            l2=Label(frame1,text="Floor No",font=('Arial',12, 'bold'),bg='white', fg='green')
            l2.pack()
            u2 = Entry(frame1, textvariable=floor,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u2.pack()
            l3=Label(frame1,text="Rent",font=('Arial',12, 'bold'),bg='white', fg='green')
            l3.pack()
            u3 = Entry(frame1, textvariable=rent1,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u3.pack()
            l4=Label(frame1,text="Person",font=('Arial',12, 'bold'),bg='white', fg='green')
            l4.pack()
            u4 = Entry(frame1, textvariable=person_no,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u4.pack()
            u3 = Button(frame1, text="update", command=r_updatefinal)
            u3.pack()

            curItem = tree.focus()
            
            content = tree.item(curItem)

            row_data = content['values']
            
            room.set(row_data[1])
            floor.set(row_data[2])
            rent1.set(row_data[3])
            person_no.set(row_data[4])
            slno1 = row_data[0]
            
    vroom =tk.Tk()
    vroom.title('View Room Details')
    vroom.geometry('900x700')

    # Background Colors
    vroom.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    vroom.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(vroom, text='View Room Details',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame=Frame(vroom, height="10", width="100")
    frame.pack()
    scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame, orient=VERTICAL)
    # ecting to database with registration form
    tree=ttk.Treeview(frame,columns=("v","a","b","c","d"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('v',text="Serial No.")
    tree.heading('a',text="Room No")
    tree.heading('b',text="Floor No.")
    tree.heading('c',text="Rent")
    tree.heading('d',text="Person")
    tree.column('#0', minwidth="0", width=0)
    tree.column('#1', anchor='center')
    tree.column('#2', anchor='center')
    tree.column('#3',  anchor=W)
    tree.pack()
    lb1 = tk.Label(vroom, text="Search:",font=('Arial',12, 'bold'),bg='#3B2C35', fg='green')
    lb1.pack()
    r_search_entry = Entry(vroom, width=15,font=('calibre',10,'normal'), justify = 'center', bg='white')
    r_search_entry.pack()
    r_search_entry.bind('<Return>', r_search_record)   
    btn = tk.Button(vroom, text="search",command=r_search_record,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()       
    b1 = tk.Button(vroom, text="delete",command=r_del_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    b1.pack()
    b1 = tk.Button(vroom, text="update",command=r_update_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    b1.pack()
    b1 = tk.Button(vroom, text="reload",command=r_reload_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    b1.pack()
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    query = "select * from room"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    for i in row:
        tree.insert('', 'end', values=(i))
    conn.commit()
    cursor.close()
    conn.close()
    vroom.mainloop()
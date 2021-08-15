from tkinter import *
from tkinter import messagebox as ms
import pymysql as db 
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter as tk
# Creating register function
def view_student():
    def reload_data():
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="select * from stu_login"
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        cursor.close()
        conn.close()
    def search_record():  
        q1=search_entry.get()
        conn = db.connect(host='localhost', user='root', password='', db='hms')
        cursor = conn.cursor()
        query="SELECT * FROM `stu_login` WHERE `name` LIKE '%{}%'".format(q1)
        
        cursor.execute(query)
        row1=cursor.fetchall()
        tree.delete(*tree.get_children())
        for i in row1:
            tree.insert('', 'end', values=(i))
        conn.commit()
        cursor.close()
        conn.close()
    def del_data():
        if not tree.selection():
            ms.showerror('alert', 'please select atleast one row')
        else:
            curItem = tree.focus()
            content = tree.item(curItem)
            row_data = content['values']
            hstl_id1 = row_data[0]
            tree.delete(curItem)
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            query = "delete from stu_login where hstl_id={}".format(hstl_id1)
            cursor = conn.cursor()
            cursor.execute(query)

            conn.commit()
            ms.showinfo('Success','Successfully Deleted')
            cursor.close()
            conn.close()


    def update_data():
        def updatefinal():
            
            conn = db.connect(host='localhost', user='root', password='', db='hms')
            query = "update stu_login set `name`='{}',`contact`='{}',`email`='{}' where hstl_id={}".format(name.get(), contact.get(), email.get(), hid)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            ms.showinfo('Success','Successfully Updated')
            cursor.close()
            conn.close()
        if not tree.selection():
            ms.showerror('alert', 'please select atleast one row')
        else:
            updatewindow = Toplevel()
            updatewindow.configure(background='#3B2C35')
            updatewindow.title("update panel")
            updatewindow.geometry("600x300")
            frame = LabelFrame(updatewindow, padx=30, pady=30, bg='white')
            frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
            name = StringVar()
            contact = StringVar()
            email = StringVar()
            l1=Label(frame,text="Name",font=('Arial',12, 'bold'),bg='white', fg='green')
            l1.pack()

            u1 = Entry(frame, textvariable=name,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u1.pack()
            l2=Label(frame,text="Contact",font=('Arial',12, 'bold'),bg='white', fg='green')
            l2.pack()
            u2 = Entry(frame, textvariable=contact,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u2.pack()
            l3=Label(frame,text="Email",font=('Arial',12, 'bold'),bg='white', fg='green')
            l3.pack()
            u3 = Entry(frame, textvariable=email,font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
            u3.pack()
            u3 = Button(frame, text="update", command=updatefinal)
            u3.pack()

            curItem = tree.focus()
            
            content = tree.item(curItem)

            row_data = content['values']
            
            name.set(row_data[1])
            contact.set(row_data[4])
            email.set(row_data[5])
            hid = row_data[0]
        
   
    
    stu =tk.Tk()
    stu.title('View Student')
    stu.geometry('900x700')

    # Background Colors
    stu.configure(background='#3B2C35')

    # Locking the window size
    

    # Creating title icon
    stu.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(stu, text='View Student',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame=Frame(stu, height="10", width="100")
    frame.pack()
    scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame, orient=VERTICAL)
    # ecting to database with registration form
    tree=ttk.Treeview(frame,columns=("v","a","b","c","d","e","f","g","i","p","q"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('v',text="Hostel_id")
    tree.heading('a',text="Name")
    tree.heading('b',text="Duration")
    tree.heading('c',text="Course_reg_no")
    tree.heading('d',text="Phn_no")
    tree.heading('e',text="Email_id")
    tree.heading('f',text="Age")
    tree.heading('g',text="Gender")
    
    tree.heading('i',text="ID Proof")
    tree.heading('p',text="Allocation Date")
    tree.heading('q',text="Deallocation Date")
    tree.column('#0', minwidth="0", width=0)
    tree.column('#1', anchor='center')
    tree.column('#2', anchor='center')
    tree.column('#3', anchor='center')
    tree.column('#4', anchor='center')
    tree.column('#5', anchor='center')
    tree.column('#6', anchor='center')
    tree.column('#7', anchor='center')
    tree.column('#8', anchor='center')
    tree.column('#9', anchor='center')
    tree.column('#10', anchor='center')
    tree.column('#11', anchor='center')
    
    tree.pack()
    ttk.Style().configure(tree, background="red", foreground="coral1")
    ttk.Style().configure(tree.heading, background="blue", foreground="palevioletRed1")
    lb1 = tk.Label(stu, text="Search:",font=('Arial',12, 'bold'),bg='#3B2C35', fg='green')
    lb1.pack()
    search_entry = Entry(stu, width=15,font=('calibre',10,'normal'), justify = 'center', bg='white')
    search_entry.pack()
    search_entry.bind('<Return>', search_record)   
    btn = tk.Button(stu, text="search",command=search_record,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    btn.pack()       
    b1 = tk.Button(stu, text="delete",command=del_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    b1.pack()
    b1 = tk.Button(stu, text="update",command=update_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    b1.pack()
    b1 = tk.Button(stu, text="reload",command=reload_data,width="20",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5' )
    b1.pack()
    conn = db.connect(host='localhost', user='root', password='', db='hms')
    query = "SELECT stu_login.hstl_id,stu_login.name,stu_login.Duration,stu_login.Course_reg,stu_login.contact,stu_login.email,stu_login.age,stu_login.gender,stu_login.id_proof,room_aloc.a_date,room_delocate.d_date FROM stu_login LEFT JOIN room_aloc ON stu_login.hstl_id=room_aloc.hstl_id LEFT Join room_delocate ON room_delocate.hstl_id=room_aloc.hstl_id"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    
    for i in row:
        tree.insert('', 'end', values=(i))
    conn.commit()
    cursor.close()
    conn.close()
    stu.mainloop()
from pydoc import text
from tkinter import *
from tkinter import messagebox
import sqlite3

import data

root=Tk()
root.title("DATABASE")
root.geometry("400x400")

# conn=sqlite3.connect("student_records.db")
# cur=conn.cursor()

# already created so we can comment it ---------
# cur.execute('''
#             CREATE TABLE if not exists student(
#                 first_name text,
#                 last_name text,
#                 address text
                
#             )''')
# cur.execute("INSERT INTO student (first_name,last_name,address) VALUES(?,?,?)",("Nischal","Shrestha","kathmandu"))
# conn.commit()
# conn.close()

def submit():
    conn=sqlite3.connect("student_records.db")
    cur=conn.cursor()
    
    if not f_name.get():
        messagebox.showwarning("Input Error","First name is srequired")
        return
        
    if not l_name.get():
        messagebox.showwarning("Input Error","Last name is srequired")
        return  
        
    if not address.get():
        messagebox.showwarning("Input Error","Address is srequired")
        return
    cur.execute("INSERT INTO student  VALUES(?,?,?)",(f_name.get(),l_name.get(),address.get()))
    messagebox.showinfo("Records","Inserted Succesfully")
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    conn.commit()
    conn.close()
    
    
def query():
    conn=sqlite3.connect("student_records.db")
    cur=conn.cursor()
    cur.execute("SELECT *,oid FROM student")
    global records
    records=cur.fetchall()
    print("F name  |  L name | address" )
    for i in records:
        print(f"{i[0]} | {i[1]}  | {i[2]}  | {i[3]}")
   
 
def delete():
    if not delete_box.get():
        messagebox.showerror("Input error","Please enter an ID to delete!")
        return
    conn=sqlite3.connect("student_records.db")
    cur=conn.cursor()
    cur.execute("DELETE from student WHERE oid="+ delete_box.get())
    print("Delete Successfully")
    delete_box.delete(0,END)
    conn.commit()
    conn.close()
    query()

def update():
    conn=sqlite3.connect("student_records.db")
    cur=conn.cursor()
    data= (f_name_editor.get(),l_name_editor.get(),address_editor.get(),delete_box.get())
    cur.execute("UPDATE student SET first_name=?, last_name=?, address=? Where oid=?",data)
    conn.commit()
    conn.close()

def edit():
    
    if not delete_box.get():
        messagebox.showwarning("input error","Please enter ID")
        return
    
    global top_editor
    top_editor=Tk()
    top_editor.title("DATABASE")
    top_editor.geometry("600x400")
    top_editor.config(bg="blue")
    conn=sqlite3.connect("student_records.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE oid="+ delete_box.get())
    print("Edit Successfully")
    
    records=cur.fetchall()



    global f_name_editor,l_name_editor,address_editor
    f_name_editor=Entry(top_editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0),ipady=5)
    l_name_editor=Entry(top_editor,width=30)
    l_name_editor.grid(row=1,column=1,ipady=5)
    address_editor=Entry(top_editor,width=30)
    address_editor.grid(row=2,column=1,ipady=5)

    f_name_label_editor=Label(top_editor,text="First name :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
    f_name_label_editor.grid(row=0,column=0,pady=(10,0))
    l_name_label_editor=Label(top_editor,text="Last name :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
    l_name_label_editor.grid(row=1,column=0,pady=5)
    address_label_editor=Label(top_editor,text="Address :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
    address_label_editor.grid(row=2,column=0,pady=5)
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
    
    edit_btn=Button(top_editor,text="save" ,bg="#7538c0", fg="#ecf0f1",height=2,command=update )
    edit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=1,ipadx=100)


f_name=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)

f_name.grid(row=0,column=1,padx=20,pady=(10,0),ipady=5)
l_name=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)
l_name.grid(row=1,column=1,ipady=5)

address=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)
address.grid(row=2,column=1,ipady=5)

delete_box=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1")
delete_box.grid(row=3,column=1,pady=5,ipady=5)


f_name_label=Label(root,text="First name :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last name :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
l_name_label.grid(row=1,column=0,pady=5)

address_label=Label(root,text="Address :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
address_label.grid(row=2,column=0,pady=5)

delete_label=Label(root,text="ID :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
delete_label.grid(row=3,column=0,pady=(10,0))




submit_btn=Button(root,text="Add Records" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=submit)
submit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(root,text="Show Records" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=query)
query_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# delete_btn=Button(root,text="Delete ID" ,bg="#7538c0", fg="#ecf0f1",height=2 )
# delete_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100 )

delete_btn=Button(root,text="Delete" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=delete)
delete_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=1,ipadx=100)

edit_btn=Button(root,text="Update" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=edit)
edit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=1,ipadx=100)

# data_box=Label()
# data_box.grid(row=8,column=0,columnspan=2,pady=1,padx=10,ipadx=10)

root.mainloop()
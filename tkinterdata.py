from pydoc import text
from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("DATABASE")
root.geometry("600x400")

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
    return

f_name=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)
f_name.grid(row=0,column=1,padx=20,pady=(10,0),ipady=5)
l_name=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)
l_name.grid(row=1,column=1,ipady=5)

address=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)
address.grid(row=2,column=1,ipady=5)

# delete_box=Entry(root,width=30,bg="#2c3e50",fg="#ecf0f1",)
# delete_box.grid(row=9,column=1,ipady=5)

f_name_label=Label(root,text="First name :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last name :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
l_name_label.grid(row=1,column=0,pady=5)

address_label=Label(root,text="Address :",bg="#2c3e50",fg="#ecf0f1",font=("Segoe UI",9,"bold"))
address_label.grid(row=2,column=0,pady=5)

submit_btn=Button(root,text="Add Records" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=submit)
submit_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(root,text="Show Records" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=query)
query_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

delete_btn=Button(root,text="Delete all Records" ,bg="#7538c0", fg="#ecf0f1",height=2 ,command=delete)
delete_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

data_box=Label()
data_box.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

root.mainloop()
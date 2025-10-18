from tkinter import *
from datetime import date
window=Tk()
window.title("widgets")
window.geometry("500x600")

lb1=Label(text="hey there", fg="white", bg="#072F5F",height=1,width=300)
namelbl=Label(text="full name", fg="red",bg="green")
name_entry=Entry()

def display():
    name=name_entry.get()
    global message 
    message="welcome to the apllication\ntodays  date is: "
    greet="hello"+name+"\n"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END,date.today())

text_box=Text(height=3)
btn = Button(text="begin",command=display,height=1, bg="#1261A0", fg="white")

lb1.pack()
namelbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()
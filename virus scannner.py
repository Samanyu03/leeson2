from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("alert","virus found!!!")
    
button=Button(root,text="scan for virus",command=msg)
button.place(x=80,y=50)
root.mainloop()
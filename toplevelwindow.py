from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("main")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    
    l2=Label(top,root, text="hi this is toplevel window")
    l2.pack()
    
a=Label(root,text="hi this is a window")
b=Button(root,text="click to open toplevel window",command=topwin)

a.pack()
b.pack()

root.mainloop()
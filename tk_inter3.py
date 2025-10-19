from tkinter import *
window=Tk()
window.title("HELLO WORLD!!!!")
window.geometry("500x600")

#frame=Frame(master=window,height=200,width=360,bg="RED")
nums=[[9,8,7], [6,5,4], [3,2,1],  ["*",0,"#"]]

for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
for i in range(4):
    for j in range(3):
        FRAME=Frame(master=window,relief=SUNKEN,borderwidth=1)
        
    FRAME.grid(row=i,column=j)
    label=Label(master=FRAME,text=nums[i][j],bg="#d0efff")
    label.pack(padx=3,pady=3)
    
window.mainloop()
# List box:->It display alternative lists || Listbox ek GUI widget hai jo Tkinter mein use hota hai list of items dikhane ke liye. Isme user ek ya multiple items select kar sakta hai.

from tkinter import *
root=Tk()
root.geometry("455x333")
root.title("ListBox tutorial")
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")#ACTIVE = Ye special constant hai jo currently selected (active) item ke just before naye item ko insert karta hai.
    i+=1
i=0
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")#END = Listbox ke end mein item ko insert karta hai.

Button(root,text="Add Item",command=add).pack()
root.mainloop()
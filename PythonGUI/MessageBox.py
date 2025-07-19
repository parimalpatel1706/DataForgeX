## Message Box:->tkinter.messagebox ek module hai jo GUI me pop-up dialogs dikhane ke kaam aata hai ― jaise alert, info, warning, error, confirmation, etc.
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("733x566")
root.title("Pycharm")
def myfun():
    print("strong function")
def help1():
    print("I will help you")
    a=tmsg.showinfo("Help","Parimal will help you with this gui")
def rate():
    print("rate us")
    value=tmsg.askquestion("was your experience Good?","You used this gui.. Was your experience Good?")## askquestion is used for yes or no
    print(value)
    if value == "yes":
        msg= "Great. rate us on playstore please"
    else:
        msg="Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience",msg)




## creating dropdown menu
mainmenu= Menu(root)
m1=Menu(mainmenu,tearoff=0)


m1.add_command(label="New project",command=myfun)
m1.add_command(label="Save",command=myfun)
m1.add_separator()
m1.add_command(label="Save As",command=myfun)
m1.add_command(label="Print",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo",command=myfun)
m2.add_command(label="Redo",command=myfun)
m2.add_separator()
m2.add_command(label="Paste",command=myfun)
m2.add_command(label="Find",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)


m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help1)
m3.add_command(label="Rate us",command=rate)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)
root.mainloop()


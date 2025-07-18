from tkinter import *
root=Tk()
root.geometry("655x333")
def getvalues():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")
## grid layout
user= Label(root,text="username")
password=Label(root,text="Password")
user.grid()## here grid is used for pack
password.grid(row=1)

# variable classes in tkinter
## booleanvar, Doublevar, intvar,Stringvar
## Entry Widget
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Sumbit",command=getvalues).grid()
root.mainloop()
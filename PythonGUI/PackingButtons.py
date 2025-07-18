from tkinter import *
root=Tk()
root.geometry("655x355")
def hello():
    print("Hello Tkinter Buttons")
f1=Frame(root,borderwidth=6,bg="green",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")
b1 = Button(f1,fg="red",text="Print now",command=hello)# in command we have only pass the function name
b1.pack(side=LEFT,padx=23)
b2 = Button(f1,fg="blue",text="Print now")
b2.pack(side=LEFT,padx=23)
b3 = Button(f1,fg="black",text="tap")
b3.pack(side=LEFT,padx=23)
b4 = Button(f1,fg="yellow",text="Print now")
b4.pack(side=LEFT,padx=23)
b5 = Button(f1,fg="violet",text="Print now")
b5.pack(side=LEFT,padx=23)

root.mainloop()
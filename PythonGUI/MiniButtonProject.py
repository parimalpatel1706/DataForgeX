from tkinter import *
root=Tk()
root.geometry("655x333")
def open():
    print("open the file")
def file():
    print("welcome to the file")
def close():
        print("close the file")
f1=Frame(root,borderwidth=9,bg="red",relief=SUNKEN)
f1.pack(side=TOP,anchor="nw")
b1=Button(f1,bg="blue",text="tap it",command=open)
b1.pack(side=LEFT,padx=24)
b2=Button(f1,bg="blue",text="tap it",command=file)
b2.pack(side=LEFT,padx=24)
b3=Button(f1,bg="blue",text="tap it",command=close)
b3.pack(side=LEFT,padx=24)
root.mainloop()
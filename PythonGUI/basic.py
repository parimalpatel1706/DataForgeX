from tkinter import *
parimal_root=Tk()
# gui logic
# Width x height:this parameter is taken by geomentry function
parimal_root.geometry("444x234")## size change karne ke liye geomentry function ka use karte hai

#width,height: this parameter is taken by minsize function
parimal_root.minsize(300,100)

#width,height:this parameter is taken by maxsize function
parimal_root.maxsize(1200,988)

siddhart = Label(text="Siddhart is a good boy and this is his GUI")
siddhart.pack()## yeh karna jarui hai
parimal_root.mainloop()
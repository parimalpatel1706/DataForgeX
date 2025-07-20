from tkinter import *
root=Tk()
root.geometry("455x233")
root.title("Radio Button")
ItemList = [ 'Pizza', 'Briyani', 'Fried Rice', 'Dosa']
var=StringVar()
for i in range(len(ItemList)):
    button = Radiobutton(root, text= ItemList[i],padx=14,variable=var, value= i+1).pack(anchor='w')
root.mainloop()
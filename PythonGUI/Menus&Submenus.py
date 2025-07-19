from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("Pycharm")
def myfun():
    print("strong function")
## Use these to create a non dropdown menu

#mymenu=Menu(root)
#mymenu.add_command(label="File",command=myfun)## add_command function yeh karta hai ki yeh ek command assign kar deta hai
#mymenu.add_command(label="Exit",command=quit)
#root.config(menu=mymenu)## here config is uded for packing


## creating dropdown menu
mainmenu= Menu(root)#Ye line root window ke liye ek main menu bar create karti hai. (Jaise: File, Edit, View waala menu bar hota hai)
m1=Menu(mainmenu,tearoff=0)#Ye line ek submenu banata hai jo main menu ke andar aayega (jaise File ke andar New, Save). tearoff=0 ka matlab hai ki user is menu ko alag window me detach (khol) nahi kar sakta.


m1.add_command(label="New project",command=myfun)
m1.add_command(label="Save",command=myfun)
m1.add_separator()
m1.add_command(label="Save As",command=myfun)
m1.add_command(label="Print",command=myfun)
root.config(menu=mainmenu)#Is line se main menu ko root window ke upar attach kar dete hain — jisse menu window me dikhne lage.
mainmenu.add_cascade(label="File",menu=m1)##  ek menu ke andar dropdown menu (submenu) add karne ke liye use hota hai.

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo",command=myfun)
m2.add_command(label="Redo",command=myfun)
m2.add_separator()#Ye line menu ke andar ek horizontal line (divider) banata hai.
m2.add_command(label="Paste",command=myfun)
m2.add_command(label="Find",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)## here mainmenu play a role of submenu
root.mainloop()


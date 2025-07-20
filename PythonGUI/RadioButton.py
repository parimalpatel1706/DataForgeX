## Radio Button:->Radio Buttons allow the user to select only one option from a set of options.
#Radio button ek aise option group ko banata hai jisme ek hi option select ho sakta hai.
#Har radio button ko same variable dena hota hai (like IntVar() ya StringVar()).
#Jo button select hota hai, uska value us variable mein store hota hai.
#command se aap action perform kar sakte ho jab user option change kare.
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x333")
root.title("Radiobutton tutorial")

def order():
    tmsg.showinfo("Order Received!",f"We have received your order for {var.get()} . Thanks for ordering")

#var= IntVar()
var=StringVar()
var.set(1)
Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14,bg="red").pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Panner Dosa",padx=14,variable=var,value="Panner Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Rice",padx=14,variable=var,value="Rice").pack(anchor="w")
radio=Radiobutton(root,text="Pizza",padx=14,variable=var,value="Pizza").pack(anchor="w")

## aapne ky select kara
Button(text="Order now",command=order).pack()
root.mainloop()
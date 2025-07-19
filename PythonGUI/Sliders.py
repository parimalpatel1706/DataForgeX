from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("Slider tutorial")
def getdollar():
    print(f"we have credited {myslider2.get()}dollars to your bank account")
    tmsg.showinfo("Amount Credited",f"we have credited {myslider2.get()} dollars to your bank account")

## To create a  VERTICAL slider 
#myslider=Scale(root,from_=0,to=100)
#myslider.pack()

# for creating a horizontal slider 
Label(root,text="How many dollars do you want?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)#tickinterval:-> meri jo value mein woh ek particular interval mein chale
## for achecving its intial value
myslider2.set(34)
myslider2.pack()
Button(root,text="Get dollars",pady=5,command=getdollar).pack()

root.mainloop()

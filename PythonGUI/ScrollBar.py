from tkinter import *
root=Tk()
root.geometry("455x333")
root.title("ScrollBar Tutorial")
## kisi bhi widget ko scrollbar se connect karne ke liye two cheez ki needs hoti hai
#1.widget(yscrollcommand) == scrollar view
#2. scrollbar.config(command==widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(root, yscrollcommand=scrollbar.set)#Jyscorllbarcommand=ab widget scroll ho, toh scrollbar ka position automatically update ho.
for i in range(344):
    listbox.insert(END,f"Item {i}")
listbox.pack(fill=BOTH,padx=22)
scrollbar.config(command=listbox.yview)#command=widget.yview:-> Jab scrollbar ko move karein, toh widget ka content bhi accordingly scroll ho.

root.mainloop()
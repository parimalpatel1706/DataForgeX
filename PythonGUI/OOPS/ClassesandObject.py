from tkinter import *


class GUI(Tk):
    def __init__(self):## jo root huva karta tha woh abhi self hai yeha
        super().__init__()
        self.geometry("744x377")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar =Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)
    def createbutton(self,inptext):
        Button(text=inptext,command=self.click).pack()  
    def click(self):
        print("Button Clicked")
        
if __name__=='__main__':
    window= GUI()#jo root huva karta tha woh abhi window hai yeha
    window.status()
    window.createbutton("click me")
    window.mainloop()
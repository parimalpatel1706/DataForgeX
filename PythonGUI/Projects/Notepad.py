from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

if __name__ =='__main__':
    # Basic tkinter setup
    root=Tk()
    root.title("Untitled -Notepad")
    root.geometry("644x788")
    def newFile():
         global file
         root.title("Untitled - Notepad")
         file=None
         TextArea.delete(1.0,END)
    
    def openFile():
        global file
        file=askopenfilename(defaultextension=".txt",filetypes=[("all Files","*.*"),("Text Documents","*.txt")])
        if file== "":
            file=None
        else:
            root.title(os.path.basename(file)+" - Notepad")
            TextArea.delete(1.0,END)
            f=open(file,"r")
            TextArea.insert(1.0,f.read())
            f.close()
            

    def saveFile():
        global file
        if file == None:
            file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("all Files","*.*"),("Text Documents","*.txt")])
            if file =="":
                file=None
            else:
               # save as a new file
                f=open(file,"w")
                f.write(TextArea.get(1.0, END))
                f.close()
                
                root.title(os.path.basename(file)+ " - Notepad")
                print("file saved")
        else:
               # save the file
                f=open(file,"w")
                f.write(TextArea.get(1.0, END))
                f.close()

    def quitApp():
        root.destroy()

    
    def cut():
        TextArea.event_generate(("<<Cut>>"))#event_generate function use kiya jata hai jab hume kisi event ko manually chalana hota hai — jaise ki normally Ctrl+C dabane se "Copy" hota hai, lekin agar hum ek button click ya menu se copy karna chahein, to uske liye hum TextArea.event_generate("<<Copy>>") likhte hain.

    
    def copy():
       TextArea.event_generate(("<<Copy>>"))
    def paste():
        TextArea.event_generate(("<<Paste>>"))

    def about():
        showinfo("Notepad","Notepad by Parimal Patel")
    
    

    # Add TextArea
    TextArea= Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH,)
    
    # Lets create a menubar
    MenuBar=Menu(root)
    # File Menu Starts
    FileMenu=Menu(MenuBar,tearoff=0)
    
    # to open new file
    FileMenu.add_command(label="New",command=newFile)
    
    # To Open Already existing file
    FileMenu.add_command(label="Open",command=openFile)
    
    # to save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
   
    # File menu Ends
    
    ## Edit menu Starts
    EditMenu=Menu(MenuBar,tearoff=0)
    # to give a feature of cut,copy and paste
    
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
     ## Edit menu Ends
    
    
    ## Help menu Starts
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    ## Help menu Ends
    root.config(menu=MenuBar)
    
    
    ## Adding Scrollbar 
    
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    root.mainloop()

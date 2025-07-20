from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("Title of My GUI")
# change the icon of Gui which is feather for that we need ico file
#root.wm_iconbitmap(r"C:\Users\PARIMAL\OneDrive\Desktop\Data Science\PythonGUI\1.ico")
## jab bhi koi changes lana hai toh hum configure function ka use karte hai
root.configure(background="green")

## if we have to know the width and heiht of the GUI screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close",command=root.destroy).pack()#command=root.destroyJab user is button ko click karega, tab root.destroy() function call hoga.2 root.destroy() ka matlab hai poora GUI window close kar dena.Yani, yeh button kaam karega "Exit" ya "Close Window" jaise.
root.mainloop()
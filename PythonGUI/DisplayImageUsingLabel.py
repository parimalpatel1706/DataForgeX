from tkinter import *
from PIL import Image, ImageTk#Imports the Image and ImageTk modules from the Pillow library. Image is used to open and manipulate images. ImageTk is used to convert images into a format that Tkinter can display.

image_root = Tk()#Creates the main Tkinter window, often called the root window.
image_root.geometry("1000x1000")
#photo=PhotoImage(file=r"C:\Users\PARIMAL\OneDrive\Desktop\Data Science\PythonGUI\1.png.png")

## For JPG Iage
image=Image.open(r"C:\Users\PARIMAL\OneDrive\Desktop\Data Science\PythonGUI\upsc.jpg")
photo=ImageTk.PhotoImage(image)

label=Label(image=photo)
label.pack()


image_root.mainloop()
from tkinter import *

m = Tk()

# Function to set window size based on entry values
def setsize():
    try:
        w = int(entry_width.get())
        h = int(entry_height.get())
        m.geometry(f"{w}x{h}")
    except ValueError:
        print("Please enter valid integers")

# Frame setup
f1 = Frame(bg="red", height=200, width=250)
f1.pack(anchor="w")

# Entry widgets to input width and height
entry_width = Entry(f1)
entry_width.pack(side=LEFT)
entry_height = Entry(f1)
entry_height.pack(side=LEFT)

# Button to apply the size
but = Button(f1, text="Set Size", command=setsize)
but.pack(side=LEFT)

m.mainloop()

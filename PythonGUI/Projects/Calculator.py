from tkinter import *

# Function to handle button click
def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            value = eval(screen.get())
        except:
            value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

# Create root window
root = Tk()
root.geometry("644x900")
root.title("Calculator By Parimal Patel")
root.wm_iconbitmap(r"C:\Users\PARIMAL\OneDrive\Desktop\Data Science\Calculator.ico")

# Apply dark theme
root.configure(bg="#2E2E2E")

# Screen Entry
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", bg="#1E1E1E", fg="white", insertbackground='white')
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Frame 1
f = Frame(root, bg="#2E2E2E")
b = Button(f, text="9", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Frame 2
f = Frame(root, bg="#2E2E2E")
b = Button(f, text="6", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Frame 3
f = Frame(root, bg="#2E2E2E")
b = Button(f, text="3", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Frame 4
f = Frame(root, bg="#2E2E2E")
b = Button(f, text="0", padx=31, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=34, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=34, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Frame 5
f = Frame(root, bg="#2E2E2E")
b = Button(f, text="/", padx=34, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=25, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=27, pady=20, font="lucida 20 bold", bg="#0A84FF", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Frame 6
f = Frame(root, bg="#2E2E2E")
b = Button(f, text="C", padx=24, pady=20, font="lucida 20 bold", bg="#FF453A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=26, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=30, pady=20, font="lucida 20 bold", bg="#3A3A3A", fg="white")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Start the GUI
root.mainloop()

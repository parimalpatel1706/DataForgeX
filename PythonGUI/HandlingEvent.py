from tkinter import *
root=Tk()
root.title("Events in Tkinter")
root.geometry("644x334")
def parimal(event):## here we have to pass event and this is compuslory
    print(f"You clicked on the button at {event.x},{event.y}")

widget= Button(root,text="Click me please")
widget.pack()

# events ko bind karna hai
widget.bind('<Button-1>',parimal)
widget.bind('<Double-1>',quit)




root.mainloop()



# 📘 Tkinter Important Events - Notes

# ✅ Keyboard Events
# <Key>              → Any key is pressed
# <KeyPress-a>       → Specific key (like 'a') is pressed
# <Return>           → Enter key is pressed
# <Escape>           → Escape key is pressed

# ✅ Mouse Events
# <Button-1>         → Left mouse button click
# <Button-2>         → Middle mouse button click
# <Button-3>         → Right mouse button click
# <Double-Button-1>  → Double left-click
# <B1-Motion>        → Mouse drag with left button held down
# <Motion>           → Mouse movement (without clicking)
# <Enter>            → Mouse enters widget area
# <Leave>            → Mouse leaves widget area
# <MouseWheel>       → Mouse wheel scroll (Windows only)

# ✅ Focus & Window Events
# <FocusIn>          → Widget gains keyboard focus
# <FocusOut>         → Widget loses keyboard focus
# <Configure>        → Widget is resized or moved
# <Destroy>          → Widget is destroyed
# <Expose>           → Widget is redrawn

# ✅ Example Usage:
"""
def key_pressed(event):
    print("You pressed:", event.char)

root.bind("<Key>", key_pressed)
"""

# 👉 Use root.bind() or widget.bind() to bind events to functions
 

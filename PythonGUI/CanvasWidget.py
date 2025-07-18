#The Canvas widget in Tkinter is used to draw shapes, images, or text in a rectangular area, allowing for custom graphics and visual elements in a GUI.
##A widget in Tkinter is a GUI element like a button, label, entry box, or canvas that allows user interaction and interface design.
from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas Widget")
can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

# The line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

## creating a rectangle specify parameter in this order -- coordinate of top left and coordinate of bottom right
can_widget.create_rectangle(3,5,700,300,fill="blue")

## create an text
can_widget.create_text(200,200,text="python")#x = 200 (horizontal from left) and y = 200 (vertical from top)

## create an oval functions
can_widget.create_oval(344,233,244,355)#create_oval(x1, y1, x2, y2) 
#(x1, y1) is the top-left corner
#(x2, y2) is the bottom-right corner
#Left: 244,Top: 233,Right: 344,Bottom: 355










root.mainloop()
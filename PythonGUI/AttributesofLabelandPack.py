from tkinter import *
root=Tk()
root.geometry("444x233")
root.title("MY GUI WITH PARIMAL")# for changing or making the title 

# Important Label Options
# text - adding the text
# bd - background
# fg - foreground
# font - sets the font
# for writing a fonts with have two options:1 with the help of tuple font=("comicsansms 19 bold") and 2: is with direct pass string font="comicsansms 19 bold" and for weiting a font (fontname fontsize fontstyle)
# padx - x padding
# pady - y padding
# relief - means border kaise dikhta hai || border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label=Label(text='''Shark Tank India is an Indian Hindi-language business reality television \n series that airs on Sony LIV and Sony Entertainment Television. The show is the Indian franchise of \nthe American show Shark Tank. It shows entrepreneurs making business presentations to a panel of \ninvestors or sharks, who decide whether to invest in their company.''',bg="red",fg="white",padx=113,pady=94,font="comicsansms 19 bold",borderwidth=3,relief=SUNKEN)

## Importnat Packs Options
#anchor=northwest, southwest,northeast,southeast
#side-TOP,BOTTOM,LEFT,RIGHT
#fill
#padx
#pady
title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)
root.mainloop()
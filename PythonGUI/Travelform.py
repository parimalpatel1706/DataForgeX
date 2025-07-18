from tkinter import *
root =Tk()
root.geometry("644x344")
def getvals():
    print("It works")
## Heading
Label(root,text="Welcome to Parimal Travels",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

# text for our form
Name = Label(root,text="Name")
Phone = Label(root,text="Phone")
Gender = Label(root,text="Gender")
EmergencyContact = Label(root,text="Emergency Contact")
PaymentMode= Label(root,text="Payment Mode")

# pack text for our form
Name.grid(row=1,column=2)
Phone.grid(row=2,column=2)
Gender.grid(row=3,column=2)
EmergencyContact.grid(row=4,column=2)
PaymentMode.grid(row=5,column=2)

# Tkinter variable for storing entries
Namevalue= StringVar()
Phonevalue= StringVar()
Gendervalue= StringVar()
EmergencyContactvalue= StringVar()
PaymentModevalue= StringVar()
FoodServicesvalue= IntVar()

# Entry for our form
NameEntry= Entry(root,textvariable=Namevalue)
PhoneEntry= Entry(root,textvariable=Phonevalue)
GenderEntry= Entry(root,textvariable=Gendervalue)
EmergencyContactEntry= Entry(root,textvariable=EmergencyContactvalue)
PaymentModeEntry= Entry(root,textvariable=PaymentModevalue)


## packing the entry
NameEntry.grid(row=1,column=3)
PhoneEntry.grid(row=2,column=3)
GenderEntry.grid(row=3,column=3)
EmergencyContactEntry.grid(row=4,column=3)
PaymentModeEntry.grid(row=5,column=3)

## checkbox and Packing it
FoodServicesvalue=Checkbutton(text="Want to prebook your meals?",variable=FoodServicesvalue)
FoodServicesvalue.grid(row=6,column=3)

## Button & Packing it and assigning it a command
Button(text="Submit to Parimal Travels",command=getvals).grid(row=7,column=3)
root.mainloop()
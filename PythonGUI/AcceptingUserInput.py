from tkinter import *

root = Tk()
root.geometry("644x344")

def getvals():
    print("Submitting Form")
    print(f"{Namevalue.get(), Phonevalue.get(), Gendervalue.get(), EmergencyContactvalue.get(), PaymentModevalue.get(), FoodServiceVar.get()}") 
    with open("records.txt", "a") as f:# put the values into a text file
        f.write(f"{Namevalue.get(), Phonevalue.get(), Gendervalue.get(), EmergencyContactvalue.get(), PaymentModevalue.get(), FoodServiceVar.get()}\n")

# Heading
Label(root, text="Welcome to Parimal Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Labels
Label(root, text="Name").grid(row=1, column=2)
Label(root, text="Phone").grid(row=2, column=2)
Label(root, text="Gender").grid(row=3, column=2)
Label(root, text="Emergency Contact").grid(row=4, column=2)
Label(root, text="Payment Mode").grid(row=5, column=2)

# Tkinter variables
Namevalue = StringVar()
Phonevalue = StringVar()
Gendervalue = StringVar()
EmergencyContactvalue = StringVar()
PaymentModevalue = StringVar()
FoodServiceVar = IntVar()  # use different variable for checkbox

# Entry fields
Entry(root, textvariable=Namevalue).grid(row=1, column=3)
Entry(root, textvariable=Phonevalue).grid(row=2, column=3)
Entry(root, textvariable=Gendervalue).grid(row=3, column=3)
Entry(root, textvariable=EmergencyContactvalue).grid(row=4, column=3)
Entry(root, textvariable=PaymentModevalue).grid(row=5, column=3)

# Checkbox
Checkbutton(text="Want to prebook your meals?", variable=FoodServiceVar).grid(row=6, column=3)

# Submit Button
Button(text="Submit to Parimal Travels", command=getvals).grid(row=7, column=3)

root.mainloop()

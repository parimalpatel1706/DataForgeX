import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # cm to meter
        bmi = weight / (height ** 2)
        result = f"Your BMI is: {bmi:.2f}\n"

        if bmi < 18.5:
            result += "Category: Underweight"
        elif 18.5 <= bmi < 24.9:
            result += "Category: Normal weight"
        elif 25 <= bmi < 29.9:
            result += "Category: Overweight"
        else:
            result += "Category: Obese"

        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.configure(bg="#1091ED")

tk.Label(root, text="Enter your weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Enter your height (cm):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

root.mainloop()

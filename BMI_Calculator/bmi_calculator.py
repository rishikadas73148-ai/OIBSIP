import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # BMI formula
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Category + Color
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(text=f"BMI: {bmi} ({category})", fg=color)

    except:
        result_label.config(text="Enter valid values", fg="white")

# Create window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")
window.config(bg="#1e1e1e")

# Input fields
tk.Label(window, text="Enter Weight (kg)", bg="#1e1e1e", fg="white").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack(pady=5)

tk.Label(window, text="Enter Height (m)", bg="#1e1e1e", fg="white").pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack(pady=5)

# Button
tk.Button(window, text="Calculate BMI",
          command=calculate_bmi,
          bg="green", fg="white").pack(pady=10)

# Result
result_label = tk.Label(window, text="", bg="#1e1e1e", fg="white", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
window.mainloop()

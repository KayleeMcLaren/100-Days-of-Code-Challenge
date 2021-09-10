
from tkinter import *


def converter():
    miles = float(user_input.get())
    m_to_km = miles * 1.609
    result_label.config(text=f"{m_to_km}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Input
user_input = Entry(width=7)
user_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# is equal to Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

# Result Label
result_label = Label(text=0)
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

# Km Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Calculate Button
calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

window.mainloop()

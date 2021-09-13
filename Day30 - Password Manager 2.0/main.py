
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
"""A function to generate a password from a random number of letters, numbers, and symbols which are joined together in the password_list variable
and then shuffled. The password is displayed to the user in the password_input Entry widget. Add pyperclip is used to copy the password, so that it
is ready to be pasted by the user."""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
"""A function to save the password either created by the user or generated randomly after pressing the "Generate Password" button. It checks whether the user has left
 any fields empty and displays an appropriate message to the user. It also handles a FileNotFound exception when the user tries to open the data.json file before it has
 been created, and then once it has been created, it saves the user's login details to that file. The website_input and password_input Entry widgets are then cleared."""
  
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            

# ---------------------------- SEARCH ------------------------------- #


def search():
"""A function which allows the user to search the data.json file for login details by searching for the name of a website. It handles a FileNotFound exception when 
the user tries to search for a website before a data.json file has been created. It checks to see if the name of the website entered by the user is in the data,json file 
and then displays the corresponding login information. It the website is not in the data.json file, it displays an appropriate message."""
  
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
            email_result = data[website]["email"]
            password_result = data[website]["password"]
            messagebox.showinfo(title=f"Search Result for {website}: ", message=f"Username/Email:  {email_result } \nPassword: {password_result}")
        else:
            messagebox.showinfo(title=f"Error", message=f"No Data for {website}")
            

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# Website label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

# Website entry
website_input = Entry(width=30)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email/Username label
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

# Email entry
email_input = Entry(width=30)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, "mclaren.kaylee@gmail.com")

# Password label
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Password entry
password_input = Entry(width=30)
password_input.grid(column=1, row=3)

# Generate Password button
generate_password_button = Button(text="Generate Password", width=15, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=5, row=3)

# Add button
add_button = Button(text="Add", width=15, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Search button
search_button = Button(text="Search", width=15, highlightthickness=0, command=search)
search_button.grid(column=5, row=1)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

window.mainloop()

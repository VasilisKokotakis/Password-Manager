from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password, insert it into the entry box, and copy it to clipboard."""
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    # Randomly choose characters
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Create final string
    password = "".join(password_list)

    # Insert and copy
    password_entry.delete(0, END)  # Clear before inserting
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save website, email, and password data into data.json."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
        return

    try:
        with open("data.json", "r") as data_file:
            # Load existing data
            data = json.load(data_file)

    except FileNotFoundError:
        # If file doesn't exist, create a new one
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    except json.JSONDecodeError:
        # If file exists but is empty or invalid JSON
        data = new_data
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    else:
        # Update existing data
        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    finally:
        # Clear input fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Search for saved login details for a given website."""
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data file is empty or corrupted.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)  # Convenience: copy password when found
        else:
            messagebox.showinfo(title="Error", message=f"No details for '{website}' found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "your_email@gmail.com")  # Default email

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
Button(text="Search", command=find_password).grid(column=2, row=1, sticky="EW")
Button(text="Generate Password", command=generate_password).grid(column=2, row=3, sticky="EW")
Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

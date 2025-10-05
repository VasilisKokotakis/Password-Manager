from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password, insert it into the entry box, and copy it to clipboard."""
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save website, email, and password data into data.json."""
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
        return

    new_data = {website: {"email": email, "password": password}}

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- POPUP (SEARCH RESULT) ------------------------------- #
def open_search_popup(website, email, password):
    """Open a Toplevel popup showing email and password with a Copy Password button."""
    popup = ttk.Toplevel(app)
    popup.title(f"Details — {website}")
    popup.resizable(False, False)

    # Center popup relative to main window
    popup.update_idletasks()
    w = 360
    h = 150
    # main window position and size
    mw = app.winfo_width()
    mh = app.winfo_height()
    mx = app.winfo_rootx()
    my = app.winfo_rooty()
    # calc centered pos
    px = mx + (mw - w) // 2
    py = my + (mh - h) // 2
    popup.geometry(f"{w}x{h}+{px}+{py}")

    container = ttk.Frame(popup, padding=12)
    container.pack(fill=BOTH, expand=True)

    ttk.Label(container, text="Email / Username:", bootstyle="secondary").grid(column=0, row=0, sticky="W")
    ttk.Label(container, text=email).grid(column=0, row=1, sticky="W", pady=(0, 8))

    ttk.Label(container, text="Password:", bootstyle="secondary").grid(column=0, row=2, sticky="W")
    pw_label = ttk.Label(container, text=password)
    pw_label.grid(column=0, row=3, sticky="W", pady=(0, 10))

    # Buttons frame
    btn_frame = ttk.Frame(container)
    btn_frame.grid(column=0, row=4, sticky="EW")
    btn_frame.columnconfigure((0,1), weight=1)

    def copy_password():
        pyperclip.copy(password)
        # small confirmation
        messagebox.showinfo(title="Copied", message="Password copied to clipboard.")

    ttk.Button(btn_frame, text="Copy Password", command=copy_password, bootstyle="primary").grid(column=0, row=0, sticky="EW", padx=(0,6))
    ttk.Button(btn_frame, text="Close", command=popup.destroy, bootstyle="secondary").grid(column=1, row=0, sticky="EW", padx=(6,0))


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Search for saved login details for a given website and show them in a popup."""
    website = website_entry.get().strip()
    if website == "":
        messagebox.showinfo(title="Error", message="Please enter a website to search.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
        return
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data file is empty or corrupted.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        # open popup with details and copy button
        open_search_popup(website, email, password)
    else:
        messagebox.showinfo(title="Error", message=f"No details for '{website}' found.")


# ---------------------------- UI SETUP ------------------------------- #
app = ttk.Window(themename="flatly")
app.title("Password Manager")
app.geometry("450x400")
app.resizable(False, False)
app.configure(padx=40, pady=30)

# Logo
canvas = Canvas(app, width=160, height=160, highlightthickness=0)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(80, 80, image=logo_img)
except Exception:
    # if logo missing or invalid, draw simple placeholder
    canvas.create_rectangle(10, 10, 150, 150, outline="#888")
    canvas.create_text(80, 80, text="LOGO", font=("Segoe UI", 12))
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 10))

# Labels
ttk.Label(app, text="Website:", bootstyle="secondary").grid(column=0, row=1, sticky="W", padx=(0,8))
ttk.Label(app, text="Email/Username:", bootstyle="secondary").grid(column=0, row=2, sticky="W", padx=(0,8))
ttk.Label(app, text="Password:", bootstyle="secondary").grid(column=0, row=3, sticky="W", padx=(0,8))

# Entries
website_entry = ttk.Entry(app)
website_entry.grid(column=1, row=1, sticky="EW", padx=5)
website_entry.focus()

email_entry = ttk.Entry(app)
email_entry.grid(column=1, row=2, sticky="EW", padx=5)
email_entry.insert(0, "your_email@gmail.com")

password_entry = ttk.Entry(app)
password_entry.grid(column=1, row=3, sticky="EW", padx=5)

# Buttons
ttk.Button(app, text="Search", command=find_password, bootstyle="info").grid(column=2, row=1, sticky="EW", padx=5)
ttk.Button(app, text="Generate", command=generate_password, bootstyle="warning").grid(column=2, row=3, sticky="EW", padx=5)
ttk.Button(app, text="Add", command=save, bootstyle="success").grid(column=1, row=4, columnspan=2, pady=15, sticky="EW")

# column weights for nice stretching
app.columnconfigure(1, weight=1)

app.mainloop()

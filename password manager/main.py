from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rls = [choice(letters) for _ in range(randint(8, 10))]
    rns = [choice(numbers) for _ in range(randint(3, 5))]
    rss = [choice(symbols) for _ in range(randint(3, 5))]
    password_list = rls + rns + rss
    shuffle(password_list)
    genpw = "".join(password_list)
    password_entry.insert(0, genpw)
    messagebox.showinfo(title="Copied to clipboard", message="Password copied to clipboard.")
    copy(genpw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    ws = website_entry.get()
    user = email_entry.get()
    pw = password_entry.get()

    if len(ws) < 1:
        messagebox.showerror(title="Missing Website", message='Empty "Website" field.')
    elif len(pw) < 1:
        messagebox.showerror(title="Missing Password", message='Empty "Password" field.')
    else:
        msg = messagebox.askyesno(title=ws,
                                  message=f"These are the details entered: \nEmail: {user} \nPassword: {pw}\n Is "
                                          f"it ok to save?")
        if msg:
            with open("data.txt", mode="a") as pws:
                pws.write(f"Website: {ws}  |  Username/Email: {user}  |  Password: {pw}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window creation
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas creation
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

# Creating GUI elements
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_password, width=36)
website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
password_entry = Entry(width=21)

# Pack GUI elements
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "username@email.com")
password_entry.grid(column=1, row=3, sticky="EW")
generate_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

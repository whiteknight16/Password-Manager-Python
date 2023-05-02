from tkinter import *
from tkinter import messagebox
import password_generator
import json
import pyperclip
# PASSWORD GENERATOR


def generate_password():
    password_write.delete(0, END)
    password = password_generator.generate_password()
    password_write.insert(0, password)
    pyperclip.copy(password)
# SAVE PASSWORD


def savePassword():
    new_data = {
        website_write.get(): {
            "email": email_write.get(),
            "password": password_write.get()
        }
    }
    if (len(website_write.get()) == 0 or len(password_write.get()) == 0 or len(email_write.get()) == 0):
        messagebox.showerror(
            title="OOPS!", message="Please don't leave any field empty")

    elif (messagebox.askokcancel(title="Website", message=f"These are the details entered:\nEmail:{email_write.get()}\nPassword:{password_write.get()}\n Is it Ok to save?")):
        try:
            with open("./data.json", "r") as savefile:
                data = json.load(savefile)
                data.update(new_data)
        except FileNotFoundError:
            with open("./data.json", "w") as savefile:
                json.dump(new_data, savefile, indent=4)

        else:
            with open("./data.json", "w") as savefile:
                json.dump(data, savefile, indent=4)
        finally:
            website_write.delete(0, END)
            password_write.delete(0, END)

# UI SETUP


# Setting Up DisplayS
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Setting up image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Setting up Labels
website = Label(text="Website: ")
email = Label(text="Email/Username: ")
password = Label(text="Password: ")
website.grid(row=1, column=0)
email.grid(row=2, column=0)
password.grid(row=3, column=0)

# Setting up buttons
generate = Button(text="Generate Password", command=generate_password)
add = Button(text="Add", width=36, command=savePassword)
generate.grid(row=3, column=2)
add.grid(row=4, column=1, columnspan=2)

# Setting up write boxes
website_write = Entry(width=35)
website_write.focus()
email_write = Entry(width=35)
email_write.insert(0, "harshpandey189@gmail.com")
password_write = Entry(width=25)
website_write.grid(row=1, column=1, columnspan=2)
email_write.grid(row=2, column=1, columnspan=2)
password_write.grid(row=3, column=1, sticky="E")


window.mainloop()

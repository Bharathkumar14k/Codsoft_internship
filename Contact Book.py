import tkinter as tk
from tkinter import messagebox

# Create a tk window
window = tk.Tk()
window.geometry("800x500")
window.title("Contact Book")
window.config(bg="black")

# Create a list to store contact information
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get()
    email = email_entry.get()
    if name != "":
        contacts.append((name, phone, email))
        messagebox.showinfo("Save", "Contact saved successfully")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        update_listbox()

# Function to remove a selected contact
def remove_contact():
    selected = contacts_listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        update_listbox()
        messagebox.showinfo("Deleted", "Contact deleted successfully")

# Function to display contact details
def display_contacts():
    for contact in contacts:
        messagebox.showinfo("Details", f"Name: {contact[0]}\nPhone: {contact[1]}\nEmail: {contact[2]}")

# Function to update the contact listbox
def update_listbox():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact[0])

# Heading phone book label
heading_label = tk.Label(window,
                       text="Name:",
                       font=("Arial", 17, "bold"),
                       foreground="white",
                       bg="black")
heading_label.place(x=80, y=70)

# Creating labels and entry fields for name, phone, and email
name_label = tk.Label(window,
                     text="Name: ",
                     font=("Arial", 17, "bold"),
                     foreground="white",
                     bg="black")
name_label.place(x=80, y=70)

name_entry = tk.Entry(window,
                     font=("Arial", 17, "bold"),
                     width=20)
name_entry.place(x=200, y=70)

phone_label = tk.Label(window,
                      text="Phone: ",
                      font=("Arial", 17, "bold"),
                      foreground="white",
                      bg="black")
phone_label.place(x=80, y=120)

phone_entry = tk.Entry(window,
                      font=("Arial", 17, "bold"),
                      width=20)
phone_entry.place(x=200, y=120)

email_label = tk.Label(window,
                      text="Email: ",
                      font=("Arial", 17, "bold"),
                      foreground="white",
                      bg="black")
email_label.place(x=80, y=170)

email_entry = tk.Entry(window,
                      font=("Arial", 17, "bold"),
                      width=20)
email_entry.place(x=200, y=170)

# Create buttons to add a new contact, remove selected contact, and display contact details
add_button = tk.Button(window,
                     text="ADD CONTACT",
                     command=add_contact,
                     font=("Tahoma", 13, "bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activebackground="white",
                     background="green",
                     activeforeground="dark green")
add_button.place(x=50, y=280)

remove_button = tk.Button(window,
                     text="REMOVE CONTACT",
                     command=remove_contact,
                     font=("Tahoma", 13, "bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activebackground="white",
                     background="red",
                     activeforeground="dark red")
remove_button.place(x=50, y=330)

display_button = tk.Button(window,
                     text="DISPLAY CONTACT",
                     command=display_contacts,
                     font=("Tahoma", 13, "bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activebackground="white",
                     background="light blue",
                     activeforeground="dark blue")
display_button.place(x=50, y=380)

conhead_label = tk.Label(window,
                       text="CONTACT LIST",
                       font=("Arial", 20, "bold"),
                       foreground="white",
                       bg="black")
conhead_label.place(x=510, y=230)

# Create listbox to display contacts
contacts_listbox = tk.Listbox(window,
                            font=("Arial", 12),
                            width=40)
contacts_listbox.place(x=400, y=280)

window.mainloop()

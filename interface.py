import tkinter as tk
from tkinter import ttk, messagebox
from database import get_passwords, create_table, add_password


def submit_form():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if username and email and password:
        add_password(username, email, password)
        messagebox.showinfo("Success", "Password added successfully!")
        update_display()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


def sort_by_date():
    data = display_tree.get_children()
    data = sorted(data, key=lambda x: display_tree.item(x)['values'][4], reverse=True)
    for i in range(len(data)):
        display_tree.move(data[i], '', i)


def sort_by_email():
    data = display_tree.get_children()
    data = sorted(data, key=lambda x: display_tree.item(x)['values'][2])
    for i in range(len(data)):
        display_tree.move(data[i], '', i)


def update_display():
    for row in display_tree.get_children():
        display_tree.delete(row)
    data = get_passwords()
    for item in data:
        display_tree.insert('', 'end', values=item)


def create_gui():
    global username_entry, email_entry, password_entry, display_tree

    create_table()

    root = tk.Tk()
    root.title("Password Manager")
    root.configure(background="#4c485c")

    sort_menu = tk.Menu(root)
    root.config(menu=sort_menu)

    sort_submenu = tk.Menu(sort_menu, tearoff=0)
    sort_menu.add_cascade(label="Sort", menu=sort_submenu)
    sort_submenu.add_command(label="By Date Added", command=sort_by_date)
    sort_submenu.add_command(label="By Email", command=sort_by_email)

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
    username_entry = tk.Entry(input_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
    email_entry = tk.Entry(input_frame)
    email_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
    password_entry = tk.Entry(input_frame, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    submit_button = tk.Button(input_frame, text="Add", command=submit_form)
    submit_button.grid(row=3, columnspan=2, pady=5)

    display_frame = tk.Frame(root)
    display_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    display_tree = ttk.Treeview(display_frame, columns=("ID", "Username", "Email", "Password", "Date Added"),
                                show="headings")
    display_tree.pack(expand=True, fill=tk.BOTH)

    display_tree.heading("ID", text="ID")
    display_tree.heading("Username", text="Username")
    display_tree.heading("Email", text="Email")
    display_tree.heading("Password", text="Password")
    display_tree.heading("Date Added", text="Date Added")

    display_tree.column("ID", width=50)
    display_tree.column("Username", width=150)
    display_tree.column("Email", width=150)
    display_tree.column("Password", width=150)
    display_tree.column("Date Added", width=150)

    update_display()

    root.mainloop()


if __name__ == "__main__":
    create_gui()

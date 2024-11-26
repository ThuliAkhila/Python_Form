import tkinter as tk
from tkinter import messagebox

# Function to handle registration
def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        messagebox.showinfo("Success", "Registered successfully!")
        # Clear the fields after registration
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_confirm_password.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Registration Form")
window.geometry("300x250")

# Labels and entries
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

label_confirm_password = tk.Label(window, text="Confirm Password:")
label_confirm_password.pack(pady=5)
entry_confirm_password = tk.Entry(window, show="*")
entry_confirm_password.pack(pady=5)

# Register button
btn_register = tk.Button(window, text="Register", command=register)
btn_register.pack(pady=20)

# Run the GUI loop
window.mainloop()

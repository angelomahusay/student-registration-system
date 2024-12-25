from PyQt5.QtWidgets import QApplication, QMessageBox
import tkinter as tk
from tkinter import PhotoImage
import pymysql
import subprocess

admin_win = tk.Tk()
admin_win.title("Student Registration System Admin")
admin_win.configure(bg="lightgrey")


screen_width = admin_win.winfo_screenwidth()
screen_height = admin_win.winfo_screenheight()
width = 500
height = 400
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
admin_win.geometry(f"{width}x{height}+{x}+{y}")


title_label = tk.Label(
    admin_win,
    text="Student Registration System",
    font=("Arial", 24, "bold"),
    bg="#8B2500",
    fg="white",
    pady=10,
)
title_label.pack(side=tk.TOP, fill=tk.X)

logo_image = PhotoImage(
    file="./images/logo.png", width=60, height=50
)
logo_label = tk.Label(
    title_label,
    image=logo_image,
    bg="#8B2500",
)
logo_label.place(x=8, y=0)


login_frame = tk.Frame(admin_win, bg="lightgrey", bd=10, relief=tk.GROOVE)
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=250)


username_label = tk.Label(
    login_frame,
    text="Username",
    font=("Arial", 14, "bold"),
    bg="lightgrey",
    fg="#1E1E1E",
)
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

username_var = tk.StringVar()
username_entry = tk.Entry(
    login_frame,
    textvariable=username_var,
    font=("Arial", 14),
    bd=5,
    relief=tk.GROOVE,
)
username_entry.grid(row=0, column=1, padx=10, pady=10)


password_label = tk.Label(
    login_frame,
    text="Password",
    font=("Arial", 14, "bold"),
    bg="lightgrey",
    fg="#1E1E1E",
)
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

password_var = tk.StringVar()
password_entry = tk.Entry(
    login_frame,
    textvariable=password_var,
    font=("Arial", 14),
    bd=5,
    relief=tk.GROOVE,
    show="*",
)
password_entry.grid(row=1, column=1, padx=10, pady=10)



def show_message(title, message, icon_type):
    app = QApplication([])
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)


    if icon_type == "error":
        msg.setIcon(QMessageBox.Critical)
    elif icon_type == "info":
        msg.setIcon(QMessageBox.Information)
    elif icon_type == "warning":
        msg.setIcon(QMessageBox.Warning)
    elif icon_type == "success":
        msg.setIcon(QMessageBox.Information)
        msg.setText("Success: " + message)
    elif icon_type == "question":
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


    result = msg.exec_()


    if icon_type == "question":
        return result


def admin_login():
    """Validate admin credentials using the database."""
    username = username_var.get().strip()
    password = password_var.get().strip()

    if username == "" or password == "":
        show_message("Error", "Please enter both username and password.", "error")
        return

    try:
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="sms1"
        )
        curr = conn.cursor()

        query = "SELECT * FROM admin_users WHERE username=%s AND password=%s"
        curr.execute(query, (username, password))
        result = curr.fetchone()

        if result:
            show_message("Login Success", "Welcome Admin!", "info")
            admin_win.destroy()
            subprocess.Popen(["python3", "./main.py"])
        else:
            show_message("Login Failed", "Invalid Username or Password", "error")

        conn.close()
    except Exception as e:
        show_message("Error", f"An error occurred: {e}", "error")


login_button = tk.Button(
    login_frame,
    text="Log In",
    font=("Arial", 14, "bold"),
    bg="#8B2500",
    fg="black",
    bd=5,
    relief=tk.GROOVE,
    command=admin_login,
)
login_button.grid(row=2, column=0, columnspan=2, pady=20, padx=(80, 0))

admin_win.mainloop()

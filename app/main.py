import tkinter as tk
from tkinter import ttk
from PyQt5.QtWidgets import QApplication, QMessageBox
from tkinter import PhotoImage
import subprocess
import pymysql

win = tk.Tk()
win.geometry("2560x1600+0+0")
win.title("Student Registration System")


screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
width = 2560  # fullscreen 2560 default 1350
height = 1600  # default 700 #fullscreen 1600

width = min(width, screen_width)
height = min(height, screen_height)

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
win.geometry(f"{width}x{height}+{x}+{y}")
win.configure(bg="lightgrey")


title_label = tk.Label(
    win,
    text="Student Registration System",
    font=("Arial", 30, "bold"),
    border=13,
    relief=tk.GROOVE,
    bg="#8B2500",
)
title_label.pack(side=tk.TOP, fill=tk.X)

logo_image = PhotoImage(file="./images/logo.png", width=60, height=36)
logo_label = tk.Label(
    title_label,
    image=logo_image,
    bg="#8B2500",
)
logo_label.place(x=8, y=0)


def logout():
    """Logs out the admin user."""
    result = show_message(
        "Confirm Logout", "Are you sure you want to log out?", "question"
    )

    if result == QMessageBox.Yes:
        win.destroy()
        subprocess.Popen(["python3", "./admin_login.py"])


logout_btn = tk.Button(
    title_label,
    text="Log Out",
    font=("Arial", 12, "bold"),
    bg="#FF6347",
    fg="black",
    bd=2,
    relief=tk.RAISED,
    command=logout,
)
# default x=1220
logout_btn.place(x=1327, y=6)

# Detail frame
detail_frame = tk.LabelFrame(
    win,
    text="Enter Details",
    font=("Arial", 19, "bold"),
    fg="#802D11",
    pady=5,
    bd=13,
    relief=tk.GROOVE,
    bg="lightgrey",
)
# default x=20
detail_frame.place(x=90, y=100, width=420, height=575)

# Data frame x=475
data_frame = tk.Frame(win, bd=13, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=540, y=100, width=810, height=575)

# ==========================Variables ===========================#

rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
parent = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()
navigate_var = tk.StringVar()


rollno_lbl = tk.Label(
    detail_frame, text="Roll Number", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(
    detail_frame, text="Name", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=name)
name_ent.grid(row=1, column=1, padx=2, pady=2)

class_lbl = tk.Label(
    detail_frame, text="Class", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
class_lbl.grid(row=2, column=0, padx=2, pady=2)

class_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=class_var)
class_ent.grid(row=2, column=1, padx=2, pady=2)

section_lbl = tk.Label(
    detail_frame, text="Section", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
section_lbl.grid(row=3, column=0, padx=2, pady=2)

section_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=section)
section_ent.grid(row=3, column=1, padx=2, pady=2)

contact_lbl = tk.Label(
    detail_frame, text="Contact", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
contact_lbl.grid(row=4, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=contact)
contact_ent.grid(row=4, column=1, padx=2, pady=2)

parent_lbl = tk.Label(
    detail_frame,
    text="Parent/Guardian",
    font=("Arial", 15),
    bg="lightgrey",
    fg="#1E1E1E",
)
parent_lbl.grid(row=5, column=0, padx=2, pady=2)

parent_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=parent)
parent_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = tk.Label(
    detail_frame, text="Address", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
address_lbl.grid(row=6, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=address)
address_ent.grid(row=6, column=1, padx=2, pady=2, columnspan=3)

gender_lbl = tk.Label(
    detail_frame, text="Gender", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(
    detail_frame, font=("Arial", 15), state="readonly", textvariable=gender
)
gender_ent["values"] = ("Male", "Female", "Others")
gender_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = tk.Label(
    detail_frame, text="Date of Birth", font=("Arial", 15), bg="lightgrey", fg="#1E1E1E"
)
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=dob)
dob_ent.grid(row=8, column=1, padx=2, pady=2, columnspan=3)


# ==========================Input Field Validation========================#
def validate_contact(contact):
    """Ensures contact is exactly 10 characters long."""
    if len(contact) == 10:
        return True
    else:
        return False


# ===============================Functions==================#
def fetch_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows) != 0:
        student_listbox.delete(*student_listbox.get_children())
        for row in rows:
            student_listbox.insert("", tk.END, values=row)
        conn.commit()
    conn.close()


def add_func():
    if rollno.get() == "" or name.get() == "" or class_var.get() == "":
        show_message("Error!", "Please fill all the required fields!", "error")
    elif not validate_contact(contact.get()):
        show_message("Error!", "Contact must be exactly 10 digits long!", "error")
    else:
        try:
            conn = pymysql.connect(
                host="localhost", user="root", passwd="", database="sms1"
            )
            curr = conn.cursor()
            curr.execute(
                "INSERT INTO data (rollno, name, class, section, contact, parent, address, gender, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    rollno.get(),
                    name.get(),
                    class_var.get(),
                    section.get(),
                    contact.get(),
                    parent.get(),
                    address.get(),
                    gender.get(),
                    dob.get(),
                ),
            )
            conn.commit()
            conn.close()
            fetch_data()
            clear()
            show_message("Success", "Record added successfully!", "success")
        except Exception as e:
            show_message("Error", f"An error occurred: {e}", "error")


def get_cursor(event):
    """'Kani nga function moy mo fetch data sa gi select nga row"""
    cursor_row = student_listbox.focus()
    content = student_listbox.item(cursor_row)
    row = content["values"]
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    contact.set(row[4])
    parent.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])


def clear():
    """Kani nga function ang mo clear sa entry boxes"""
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    parent.set("")
    address.set("")
    gender.set("")
    dob.set("")


def update_func():
    """Function to update the selected record, including changing the roll number."""
    if rollno.get() == "":
        show_message("Error", "Roll Number is required for updating!", "error")
        return
    if not validate_contact(contact.get()):
        show_message("Error", "Contact must be exactly 10 characters long!", "error")
        return

    try:
        cursor_row = student_listbox.focus()
        if not cursor_row:
            show_message("Error", "Please select a record to update!", "error")
            return

        content = student_listbox.item(cursor_row)
        original_rollno = content["values"][0]

        conn = pymysql.connect(
            host="localhost", user="root", password="", database="sms1"
        )
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE data 
            SET rollno=%s, name=%s, class=%s, section=%s, contact=%s, parent=%s, address=%s, gender=%s, dob=%s 
            WHERE rollno=%s
            """,
            (
                rollno.get(),
                name.get(),
                class_var.get(),
                section.get(),
                contact.get(),
                parent.get(),
                address.get(),
                gender.get(),
                dob.get(),
                original_rollno,
            ),
        )
        conn.commit()
        conn.close()

        fetch_data()
        clear()
        show_message("Success", "Record updated successfully!", "success")
    except Exception as e:
        show_message("Error", f"An error occurred: {e}", "error")


def delete_func():
    if rollno.get() == "":
        show_message("Error", "Please select a record to delete!", "error")
    else:
        confirm = show_message(
            "Confirm Delete",
            f"Are you sure you want to delete the record for Roll Number {rollno.get()}?",
            "question",
        )
        if confirm == QMessageBox.Yes:
            try:
                conn = pymysql.connect(
                    host="localhost", user="root", password="", database="sms1"
                )
                curr = conn.cursor()
                curr.execute("DELETE FROM data WHERE rollno=%s", (rollno.get(),))
                conn.commit()
                conn.close()
                fetch_data()
                clear()
                show_message(
                    "Success", "Record has been deleted successfully!", "success"
                )
            except Exception as e:
                show_message("Error", f"An error occurred: {e}", "error")


def search_records():
    """Search records based on the selected field and navigate_input value."""
    search_field = search_in.get()
    search_value = navigate_input.get().strip()

    if search_field == "":
        show_message("Error", "Please select a field to search.", "error")
        return
    if search_value == "":
        show_message("Error", "Please enter a value to search.", "error")
        return

    try:
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="sms1"
        )
        curr = conn.cursor()

        field_mapping = {
            "Name": "name",
            "Roll No.": "rollno",
            "Contact": "contact",
            "Parent/Guardian": "parent",
            "Class": "class",
            "Section": "section",
            "Date of Birth": "dob",
        }

        if search_field in field_mapping:
            query_field = field_mapping[search_field]
            query = f"SELECT * FROM data WHERE {query_field} LIKE %s"
            curr.execute(query, (f"%{search_value}%",))

            rows = curr.fetchall()
            if len(rows) != 0:
                student_listbox.delete(*student_listbox.get_children())
                for row in rows:
                    student_listbox.insert("", tk.END, values=row)
                show_message(
                    "Success", f"Found {len(rows)} matching record(s).", "info"
                )
            else:
                show_message("No Results", "No matching records found.", "info")
        else:
            show_message("Error", "Invalid search field selected.", "error")

        conn.close()
    except Exception as e:
        show_message("Error", f"An error occurred: {e}", "error")


def navigate_to_record():
    """Navigate to a specific record in the table based on navigate_input value."""
    value = navigate_input.get().strip()
    if value == "":
        show_message("Error", "Please enter a value to navigate.", "error")
        return

    found = False
    for child in student_listbox.get_children():
        row = student_listbox.item(child)["values"]
        if value in map(str, row):
            student_listbox.selection_set(child)
            student_listbox.focus(child)
            student_listbox.see(child)
            found = True
            break

    if not found:
        show_message("Not Found", "No matching record found.", "info")


def show_all_records():
    """Show all records from the database."""
    try:
        fetch_data()
        show_message("Success", "All records displayed.", "info")
    except Exception as e:
        show_message("Error", f"An error occurred: {e}", "error")


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


btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=20, y=390, width=352, height=120)

add_btn = tk.Button(
    btn_frame,
    bg="lightgrey",
    text="Add",
    bd=7,
    font=("Arial, 13"),
    width=13,
    command=add_func,
)
add_btn.grid(row=0, column=0, padx=2, pady=2)


update_btn = tk.Button(
    btn_frame,
    bg="lightgrey",
    text="Update",
    bd=7,
    font=("Arial, 13"),
    width=13,
    command=update_func,
)
update_btn.grid(row=0, column=1, pady=2, sticky=tk.E)


delete_btn = tk.Button(
    btn_frame,
    bg="lightgrey",
    text="Delete",
    bd=7,
    font=("Arial, 13"),
    width=13,
    command=delete_func,
)
delete_btn.grid(row=1, column=0, padx=2, pady=2)


clear_btn = tk.Button(
    btn_frame,
    bg="lightgrey",
    text="Clear",
    bd=7,
    font=("Arial, 13"),
    width=13,
    command=clear,
)
clear_btn.grid(row=1, column=1, pady=2, sticky=tk.E)


search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(
    search_frame, text="Search By ", bg="lightgrey", font=("Arial", 14), fg="#1E1E1E"
)
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(
    search_frame, font=("Arial"), state="readonly", textvariable=search_by
)
search_in["values"] = (
    "Name",
    "Roll No.",
    "Contact",
    "Parent/Guardian",
    "Class",
    "Section",
    "Date of Birth",
)


search_in.grid(row=0, column=1, padx=12, pady=2)

navigate_input = tk.Entry(
    search_frame,
    font=("Arial", 14),
    width=15,
    bg="#59565E",
    textvariable=navigate_var,
)
navigate_input.grid(row=0, column=2, padx=12, pady=2)

search_btn = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 13),
    bd=9,
    width=14,
    bg="lightgrey",
    command=search_records,
)
search_btn.grid(row=0, column=3, padx=12, pady=2)

showall_btn = tk.Button(
    search_frame,
    text="Show All",
    font=("Arial", 13),
    bd=9,
    width=5,
    bg="lightgrey",
    command=show_all_records,
)
showall_btn.grid(row=0, column=4, padx=12, pady=2)


main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

"""Name, class, section, contact, father's name, gender, D.O.B, Address"""
student_listbox = ttk.Treeview(
    main_frame,
    columns=(
        "Roll No.",
        "Name",
        "Class",
        "Section",
        "Contact",
        "Parent/Guardian",
        "Address",
        "Gender",
        "Date of Birth",
    ),
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set,
)

y_scroll.config(command=student_listbox.yview)
x_scroll.config(command=student_listbox.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_listbox.heading("Roll No.", text="Roll No.")
student_listbox.heading("Name", text="Name")
student_listbox.heading("Class", text="Class")
student_listbox.heading("Section", text="Section")
student_listbox.heading("Contact", text="Contact")
student_listbox.heading("Parent/Guardian", text="Parent/Guardian")
student_listbox.heading("Address", text="Address")
student_listbox.heading("Gender", text="Gender")
student_listbox.heading("Date of Birth", text="Date of Birth")

student_listbox["show"] = "headings"

student_listbox.column("Roll No.", width=100)
student_listbox.column("Name", width=100)
student_listbox.column("Class", width=100)
student_listbox.column("Section", width=100)
student_listbox.column("Contact", width=100)
student_listbox.column("Parent/Guardian", width=100)
student_listbox.column("Address", width=100)
student_listbox.column("Gender", width=100)
student_listbox.column("Date of Birth", width=100)

student_listbox.pack(fill=tk.BOTH, expand=True)

fetch_data()

student_listbox.bind("<ButtonRelease-1>", get_cursor)
win.mainloop()

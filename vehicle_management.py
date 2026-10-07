import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector



# DATABASE CONNECTION


def connect_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="moon143",
            database="vehicle_management"
        )
        return conn

    except mysql.connector.Error as err:
        messagebox.showerror(
            "Database Error",
            f"Could not connect to MySQL.\n\n{err}"
        )
        return None



# MAIN WINDOW


root = tk.Tk()

root.title("Vehicle Maintenance Record System")
root.geometry("1100x700")
root.resizable(False, False)
root.configure(bg="#F8F6F2")



# PAGE FUNCTIONS


def hide_all_pages():
    home_frame.place_forget()
    login_frame.place_forget()
    dashboard_frame.place_forget()
    vehicle_frame.place_forget()
    maintenance_frame.place_forget()


def show_home():
    hide_all_pages()

    home_frame.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )


def show_login():
    hide_all_pages()

    login_frame.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    username_entry.focus()


def show_dashboard():
    hide_all_pages()

    dashboard_frame.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )


def logout():
    show_home()


def open_vehicle_page():
    hide_all_pages()

    vehicle_frame.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )

    show_all_vehicles()


def open_maintenance_page():
    hide_all_pages()

    maintenance_frame.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )

    show_all_maintenance()



# HOME PAGE


home_frame = tk.Frame(
    root,
    bg="#F8F6F2"
)


home_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
)


tk.Label(
    home_frame,
    text="VEHICLE MAINTENANCE\nRECORD SYSTEM",
    font=("Arial", 26, "bold"),
    bg="#F8F6F2",
    fg="#444444",
    justify="center"
).pack(pady=120)


tk.Label(
    home_frame,
    text="Manage vehicle details and maintenance records easily",
    font=("Arial", 13),
    bg="#F8F6F2",
    fg="#666666"
).pack(pady=10)


tk.Button(
    home_frame,
    text="Login",
    command=show_login,
    font=("Arial", 13, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=20,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(pady=40)



# LOGIN PAGE


login_frame = tk.Frame(
    root,
    bg="#F8F6F2"
)


tk.Label(
    login_frame,
    text="LOGIN",
    font=("Arial", 24, "bold"),
    bg="#F8F6F2",
    fg="#444444"
).pack(pady=80)


login_box = tk.Frame(
    login_frame,
    bg="#FFFFFF",
    bd=1,
    relief="solid"
)

login_box.pack(
    ipadx=50,
    ipady=35
)


tk.Label(
    login_box,
    text="Username",
    font=("Arial", 12),
    bg="#FFFFFF",
    fg="#444444"
).grid(
    row=0,
    column=0,
    padx=15,
    pady=15
)


username_entry = tk.Entry(
    login_box,
    font=("Arial", 12),
    width=25
)

username_entry.grid(
    row=0,
    column=1,
    padx=15,
    pady=15
)


tk.Label(
    login_box,
    text="Password",
    font=("Arial", 12),
    bg="#FFFFFF",
    fg="#444444"
).grid(
    row=1,
    column=0,
    padx=15,
    pady=15
)


password_entry = tk.Entry(
    login_box,
    font=("Arial", 12),
    width=25,
    show="*"
)

password_entry.grid(
    row=1,
    column=1,
    padx=15,
    pady=15
)



# LOGIN FUNCTION


def login():

    username = username_entry.get().strip()
    password = password_entry.get().strip()


    if username == "" or password == "":
        messagebox.showwarning(
            "Login",
            "Please enter username and password."
        )
        return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()

        query = """
            SELECT user_id, username
            FROM users
            WHERE username = %s AND password = %s
        """

        cursor.execute(
            query,
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()


        if user:

            messagebox.showinfo(
                "Login Successful",
                "Login successful!"
            )

            show_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )


    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            str(err)
        )



# LOGIN BUTTONS


login_buttons = tk.Frame(
    login_box,
    bg="#FFFFFF"
)

login_buttons.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=25
)


tk.Button(
    login_buttons,
    text="Login",
    command=login,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=10
)


tk.Button(
    login_buttons,
    text="Back",
    command=show_home,
    font=("Arial", 11, "bold"),
    bg="#E9E2F5",
    fg="#444444",
    width=12,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=10
)



# DASHBOARD PAGE


dashboard_frame = tk.Frame(
    root,
    bg="#F8F6F2"
)



# DASHBOARD HEADER


dashboard_header = tk.Frame(
    dashboard_frame,
    bg="#F8F6F2"
)

dashboard_header.pack(
    fill="x",
    padx=30,
    pady=25
)


# BACK BUTTON

tk.Button(
    dashboard_header,
    text="← Back",
    command=show_login,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left"
)


# LOGOUT BUTTON

tk.Button(
    dashboard_header,
    text="Logout",
    command=logout,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(
    side="right"
)


tk.Label(
    dashboard_frame,
    text="DASHBOARD",
    font=("Arial", 25, "bold"),
    bg="#F8F6F2",
    fg="#444444"
).pack(pady=50)


tk.Label(
    dashboard_frame,
    text="Select an option",
    font=("Arial", 13),
    bg="#F8F6F2",
    fg="#666666"
).pack(pady=5)



# DASHBOARD BUTTONS


dashboard_buttons = tk.Frame(
    dashboard_frame,
    bg="#F8F6F2"
)

dashboard_buttons.pack(
    pady=60
)


tk.Button(
    dashboard_buttons,
    text="Vehicle Management",
    command=open_vehicle_page,
    font=("Arial", 13, "bold"),
    bg="#E9E2F5",
    fg="#444444",
    width=24,
    height=3,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=20
)


tk.Button(
    dashboard_buttons,
    text="Maintenance Records",
    command=open_maintenance_page,
    font=("Arial", 13, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=24,
    height=3,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=20
)



# VEHICLE MANAGEMENT PAGE


vehicle_frame = tk.Frame(
    root,
    bg="#F8F6F2"
)



# VEHICLE HEADER


vehicle_header = tk.Frame(
    vehicle_frame,
    bg="#F8F6F2"
)

vehicle_header.pack(
    fill="x",
    padx=30,
    pady=20
)


# BACK TO DASHBOARD

tk.Button(
    vehicle_header,
    text="← Back",
    command=show_dashboard,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left"
)


# LOGOUT

tk.Button(
    vehicle_header,
    text="Logout",
    command=logout,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(
    side="right"
)


tk.Label(
    vehicle_frame,
    text="VEHICLE MANAGEMENT",
    font=("Arial", 22, "bold"),
    bg="#F8F6F2",
    fg="#444444"
).pack(pady=5)



# VEHICLE FORM


vehicle_form = tk.Frame(
    vehicle_frame,
    bg="#FFFFFF",
    bd=1,
    relief="solid"
)

vehicle_form.pack(
    padx=30,
    pady=10,
    fill="x"
)


# Vehicle Number

tk.Label(
    vehicle_form,
    text="Vehicle Number",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8
)


vehicle_number_entry = tk.Entry(
    vehicle_form,
    width=20,
    font=("Arial", 11)
)

vehicle_number_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# Owner Name

tk.Label(
    vehicle_form,
    text="Owner Name",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=8
)


owner_name_entry = tk.Entry(
    vehicle_form,
    width=20,
    font=("Arial", 11)
)

owner_name_entry.grid(
    row=0,
    column=3,
    padx=10,
    pady=8
)


# Vehicle Type

tk.Label(
    vehicle_form,
    text="Vehicle Type",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8
)


vehicle_type_combo = ttk.Combobox(
    vehicle_form,
    values=[
        "Car",
        "Bike",
        "Truck",
        "Bus",
        "Other"
    ],
    width=18,
    state="readonly"
)

vehicle_type_combo.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# Brand

tk.Label(
    vehicle_form,
    text="Brand",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=1,
    column=2,
    padx=10,
    pady=8
)


brand_entry = tk.Entry(
    vehicle_form,
    width=20,
    font=("Arial", 11)
)

brand_entry.grid(
    row=1,
    column=3,
    padx=10,
    pady=8
)


# Model

tk.Label(
    vehicle_form,
    text="Model",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8
)


model_entry = tk.Entry(
    vehicle_form,
    width=20,
    font=("Arial", 11)
)

model_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


# Year

tk.Label(
    vehicle_form,
    text="Year",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=2,
    column=2,
    padx=10,
    pady=8
)


year_entry = tk.Entry(
    vehicle_form,
    width=20,
    font=("Arial", 11)
)

year_entry.grid(
    row=2,
    column=3,
    padx=10,
    pady=8
)


# Contact

tk.Label(
    vehicle_form,
    text="Contact Number",
    font=("Arial", 11),
    bg="#FFFFFF"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8
)


contact_entry = tk.Entry(
    vehicle_form,
    width=20,
    font=("Arial", 11)
)

contact_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)



# VEHICLE FUNCTIONS


def clear_vehicle_fields():

    vehicle_number_entry.delete(0, tk.END)
    owner_name_entry.delete(0, tk.END)
    vehicle_type_combo.set("")
    brand_entry.delete(0, tk.END)
    model_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

    vehicle_table.selection_remove(
        vehicle_table.selection()
    )


def add_vehicle():

    vehicle_number = vehicle_number_entry.get().strip()
    owner_name = owner_name_entry.get().strip()
    vehicle_type = vehicle_type_combo.get().strip()
    brand = brand_entry.get().strip()
    model = model_entry.get().strip()
    year = year_entry.get().strip()
    contact = contact_entry.get().strip()


    if vehicle_number == "" or owner_name == "" or vehicle_type == "":
        messagebox.showwarning(
            "Validation",
            "Please fill all required fields."
        )
        return


    if year != "" and not year.isdigit():
        messagebox.showwarning(
            "Validation",
            "Year must contain numbers only."
        )
        return


    if contact != "" and not contact.isdigit():
        messagebox.showwarning(
            "Validation",
            "Contact number must contain numbers only."
        )
        return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()

        query = """
            INSERT INTO vehicles
            (
                vehicle_number,
                owner_name,
                vehicle_type,
                brand,
                model,
                year,
                contact
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """


        cursor.execute(
            query,
            (
                vehicle_number,
                owner_name,
                vehicle_type,
                brand,
                model,
                int(year) if year else None,
                contact
            )
        )


        conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo(
            "Success",
            "Vehicle added successfully."
        )


        clear_vehicle_fields()
        show_all_vehicles()


    except mysql.connector.Error as err:

        if err.errno == 1062:

            messagebox.showerror(
                "Error",
                "Vehicle number already exists."
            )

        else:

            messagebox.showerror(
                "Database Error",
                str(err)
            )


def show_all_vehicles():

    for item in vehicle_table.get_children():
        vehicle_table.delete(item)


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                vehicle_id,
                vehicle_number,
                owner_name,
                vehicle_type,
                brand,
                model,
                year,
                contact
            FROM vehicles
            ORDER BY vehicle_id
            """
        )


        records = cursor.fetchall()


        for record in records:

            vehicle_table.insert(
                "",
                tk.END,
                values=record
            )


        cursor.close()
        conn.close()


    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            str(err)
        )


def select_vehicle(event):

    selected = vehicle_table.focus()

    if selected == "":
        return


    values = vehicle_table.item(
        selected,
        "values"
    )


    vehicle_number_entry.delete(0, tk.END)
    vehicle_number_entry.insert(0, values[1])


    owner_name_entry.delete(0, tk.END)
    owner_name_entry.insert(0, values[2])


    vehicle_type_combo.set(values[3])


    brand_entry.delete(0, tk.END)
    brand_entry.insert(0, values[4])


    model_entry.delete(0, tk.END)
    model_entry.insert(0, values[5])


    year_entry.delete(0, tk.END)

    if values[6]:
        year_entry.insert(0, values[6])


    contact_entry.delete(0, tk.END)
    contact_entry.insert(0, values[7])


def update_vehicle():

    selected = vehicle_table.focus()

    if selected == "":
        messagebox.showwarning(
            "Update",
            "Please select a vehicle record."
        )
        return


    values = vehicle_table.item(
        selected,
        "values"
    )


    vehicle_id = values[0]


    vehicle_number = vehicle_number_entry.get().strip()
    owner_name = owner_name_entry.get().strip()
    vehicle_type = vehicle_type_combo.get().strip()
    brand = brand_entry.get().strip()
    model = model_entry.get().strip()
    year = year_entry.get().strip()
    contact = contact_entry.get().strip()


    if vehicle_number == "" or owner_name == "" or vehicle_type == "":
        messagebox.showwarning(
            "Validation",
            "Please fill all required fields."
        )
        return


    if year != "" and not year.isdigit():
        messagebox.showwarning(
            "Validation",
            "Year must contain numbers only."
        )
        return


    if contact != "" and not contact.isdigit():
        messagebox.showwarning(
            "Validation",
            "Contact number must contain numbers only."
        )
        return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()


        query = """
            UPDATE vehicles
            SET
                vehicle_number = %s,
                owner_name = %s,
                vehicle_type = %s,
                brand = %s,
                model = %s,
                year = %s,
                contact = %s
            WHERE vehicle_id = %s
        """


        cursor.execute(
            query,
            (
                vehicle_number,
                owner_name,
                vehicle_type,
                brand,
                model,
                int(year) if year else None,
                contact,
                vehicle_id
            )
        )


        conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo(
            "Success",
            "Vehicle updated successfully."
        )


        clear_vehicle_fields()
        show_all_vehicles()


    except mysql.connector.Error as err:

        if err.errno == 1062:

            messagebox.showerror(
                "Error",
                "Vehicle number already exists."
            )

        else:

            messagebox.showerror(
                "Database Error",
                str(err)
            )


def delete_vehicle():

    selected = vehicle_table.focus()

    if selected == "":
        messagebox.showwarning(
            "Delete",
            "Please select a vehicle record."
        )
        return


    values = vehicle_table.item(
        selected,
        "values"
    )


    vehicle_id = values[0]


    confirm = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this vehicle?"
    )


    if not confirm:
        return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()


        cursor.execute(
            "DELETE FROM vehicles WHERE vehicle_id = %s",
            (vehicle_id,)
        )


        conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo(
            "Success",
            "Vehicle deleted successfully."
        )


        clear_vehicle_fields()
        show_all_vehicles()


    except mysql.connector.Error as err:

        if err.errno == 1451:

            messagebox.showerror(
                "Delete Error",
                "This vehicle has maintenance records.\n"
                "Delete its maintenance records first."
            )

        else:

            messagebox.showerror(
                "Database Error",
                str(err)
            )



# VEHICLE BUTTONS


vehicle_button_frame = tk.Frame(
    vehicle_frame,
    bg="#F8F6F2"
)

vehicle_button_frame.pack(
    pady=10
)


tk.Button(
    vehicle_button_frame,
    text="Add Vehicle",
    command=add_vehicle,
    font=("Arial", 10, "bold"),
    bg="#E9E2F5",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    vehicle_button_frame,
    text="Update",
    command=update_vehicle,
    font=("Arial", 10, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    vehicle_button_frame,
    text="Delete",
    command=delete_vehicle,
    font=("Arial", 10, "bold"),
    bg="#F5E1E1",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    vehicle_button_frame,
    text="Clear",
    command=clear_vehicle_fields,
    font=("Arial", 10, "bold"),
    bg="#F1E8D8",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    vehicle_button_frame,
    text="Show All",
    command=show_all_vehicles,
    font=("Arial", 10, "bold"),
    bg="#DDEEDC",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)



# VEHICLE TABLE


vehicle_table_frame = tk.Frame(
    vehicle_frame,
    bg="#F8F6F2"
)

vehicle_table_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=5
)


vehicle_columns = (
    "ID",
    "Vehicle Number",
    "Owner Name",
    "Vehicle Type",
    "Brand",
    "Model",
    "Year",
    "Contact"
)


vehicle_table = ttk.Treeview(
    vehicle_table_frame,
    columns=vehicle_columns,
    show="headings",
    height=11
)


for column in vehicle_columns:

    vehicle_table.heading(
        column,
        text=column
    )

    vehicle_table.column(
        column,
        width=120,
        anchor="center"
    )


vehicle_table.column(
    "ID",
    width=50
)


vehicle_table.pack(
    side="left",
    fill="both",
    expand=True
)


vehicle_scrollbar = ttk.Scrollbar(
    vehicle_table_frame,
    orient="vertical",
    command=vehicle_table.yview
)

vehicle_scrollbar.pack(
    side="right",
    fill="y"
)


vehicle_table.configure(
    yscrollcommand=vehicle_scrollbar.set
)


vehicle_table.bind(
    "<ButtonRelease-1>",
    select_vehicle
)



# MAINTENANCE PAGE


maintenance_frame = tk.Frame(
    root,
    bg="#F8F6F2"
)



# MAINTENANCE HEADER


maintenance_header = tk.Frame(
    maintenance_frame,
    bg="#F8F6F2"
)

maintenance_header.pack(
    fill="x",
    padx=30,
    pady=20
)


# BACK TO DASHBOARD

tk.Button(
    maintenance_header,
    text="← Back",
    command=show_dashboard,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left"
)


# LOGOUT

tk.Button(
    maintenance_header,
    text="Logout",
    command=logout,
    font=("Arial", 11, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=12,
    height=2,
    #relief="flat",
    cursor="hand2"
).pack(
    side="right"
)


tk.Label(
    maintenance_frame,
    text="MAINTENANCE RECORDS",
    font=("Arial", 22, "bold"),
    bg="#F8F6F2",
    fg="#444444"
).pack(pady=5)



# MAINTENANCE FORM


maintenance_form = tk.Frame(
    maintenance_frame,
    bg="#FFFFFF",
    bd=1,
    relief="solid"
)

maintenance_form.pack(
    padx=30,
    pady=10,
    fill="x"
)


# Vehicle ID

tk.Label(
    maintenance_form,
    text="Vehicle ID",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=0,
    column=0,
    padx=8,
    pady=7
)


vehicle_id_entry = tk.Entry(
    maintenance_form,
    width=15,
    font=("Arial", 10)
)

vehicle_id_entry.grid(
    row=0,
    column=1,
    padx=8,
    pady=7
)


# Service Date

tk.Label(
    maintenance_form,
    text="Service Date",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=0,
    column=2,
    padx=8,
    pady=7
)


service_date_entry = tk.Entry(
    maintenance_form,
    width=15,
    font=("Arial", 10)
)

service_date_entry.grid(
    row=0,
    column=3,
    padx=8,
    pady=7
)


# Service Type

tk.Label(
    maintenance_form,
    text="Service Type",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=0,
    column=4,
    padx=8,
    pady=7
)


service_type_entry = tk.Entry(
    maintenance_form,
    width=18,
    font=("Arial", 10)
)

service_type_entry.grid(
    row=0,
    column=5,
    padx=8,
    pady=7
)


# Description

tk.Label(
    maintenance_form,
    text="Description",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=1,
    column=0,
    padx=8,
    pady=7
)


description_entry = tk.Entry(
    maintenance_form,
    width=15,
    font=("Arial", 10)
)

description_entry.grid(
    row=1,
    column=1,
    padx=8,
    pady=7
)


# Service Cost

tk.Label(
    maintenance_form,
    text="Service Cost",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=1,
    column=2,
    padx=8,
    pady=7
)


service_cost_entry = tk.Entry(
    maintenance_form,
    width=15,
    font=("Arial", 10)
)

service_cost_entry.grid(
    row=1,
    column=3,
    padx=8,
    pady=7
)


# Next Service Date

tk.Label(
    maintenance_form,
    text="Next Service Date",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=1,
    column=4,
    padx=8,
    pady=7
)


next_service_date_entry = tk.Entry(
    maintenance_form,
    width=18,
    font=("Arial", 10)
)

next_service_date_entry.grid(
    row=1,
    column=5,
    padx=8,
    pady=7
)


# Mechanic Name

tk.Label(
    maintenance_form,
    text="Mechanic Name",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=2,
    column=0,
    padx=8,
    pady=7
)


mechanic_name_entry = tk.Entry(
    maintenance_form,
    width=15,
    font=("Arial", 10)
)

mechanic_name_entry.grid(
    row=2,
    column=1,
    padx=8,
    pady=7
)


# Remarks

tk.Label(
    maintenance_form,
    text="Remarks",
    font=("Arial", 10),
    bg="#FFFFFF"
).grid(
    row=2,
    column=2,
    padx=8,
    pady=7
)


remarks_entry = tk.Entry(
    maintenance_form,
    width=15,
    font=("Arial", 10)
)

remarks_entry.grid(
    row=2,
    column=3,
    padx=8,
    pady=7
)



# MAINTENANCE FUNCTIONS


def clear_maintenance_fields():

    vehicle_id_entry.delete(0, tk.END)
    service_date_entry.delete(0, tk.END)
    service_type_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    service_cost_entry.delete(0, tk.END)
    next_service_date_entry.delete(0, tk.END)
    mechanic_name_entry.delete(0, tk.END)
    remarks_entry.delete(0, tk.END)

    maintenance_table.selection_remove(
        maintenance_table.selection()
    )


def add_maintenance():

    vehicle_id = vehicle_id_entry.get().strip()
    service_date = service_date_entry.get().strip()
    service_type = service_type_entry.get().strip()
    description = description_entry.get().strip()
    service_cost = service_cost_entry.get().strip()
    next_service_date = next_service_date_entry.get().strip()
    mechanic_name = mechanic_name_entry.get().strip()
    remarks = remarks_entry.get().strip()


    if vehicle_id == "" or service_date == "" or service_type == "":
        messagebox.showwarning(
            "Validation",
            "Please fill Vehicle ID, Service Date and Service Type."
        )
        return


    if not vehicle_id.isdigit():

        messagebox.showwarning(
            "Validation",
            "Vehicle ID must be a number."
        )

        return


    if service_cost != "":

        try:
            float(service_cost)

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Service cost must be a number."
            )

            return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()


        query = """
            INSERT INTO maintenance
            (
                vehicle_id,
                service_date,
                service_type,
                description,
                service_cost,
                next_service_date,
                mechanic_name,
                remarks
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """


        cursor.execute(
            query,
            (
                int(vehicle_id),
                service_date,
                service_type,
                description,
                float(service_cost) if service_cost else None,
                next_service_date if next_service_date else None,
                mechanic_name,
                remarks
            )
        )


        conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo(
            "Success",
            "Maintenance record added successfully."
        )


        clear_maintenance_fields()
        show_all_maintenance()


    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            str(err)
        )


def show_all_maintenance():

    for item in maintenance_table.get_children():
        maintenance_table.delete(item)


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()


        query = """
            SELECT
                maintenance_id,
                vehicle_id,
                service_date,
                service_type,
                description,
                service_cost,
                next_service_date,
                mechanic_name,
                remarks
            FROM maintenance
            ORDER BY maintenance_id
        """


        cursor.execute(query)

        records = cursor.fetchall()


        for record in records:

            maintenance_table.insert(
                "",
                tk.END,
                values=record
            )


        cursor.close()
        conn.close()


    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            str(err)
        )


def select_maintenance(event):

    selected = maintenance_table.focus()

    if selected == "":
        return


    values = maintenance_table.item(
        selected,
        "values"
    )


    vehicle_id_entry.delete(0, tk.END)
    vehicle_id_entry.insert(0, values[1])


    service_date_entry.delete(0, tk.END)
    service_date_entry.insert(0, values[2])


    service_type_entry.delete(0, tk.END)
    service_type_entry.insert(0, values[3])


    description_entry.delete(0, tk.END)
    description_entry.insert(0, values[4])


    service_cost_entry.delete(0, tk.END)
    service_cost_entry.insert(0, values[5])


    next_service_date_entry.delete(0, tk.END)
    next_service_date_entry.insert(0, values[6])


    mechanic_name_entry.delete(0, tk.END)
    mechanic_name_entry.insert(0, values[7])


    remarks_entry.delete(0, tk.END)
    remarks_entry.insert(0, values[8])


def update_maintenance():

    selected = maintenance_table.focus()

    if selected == "":
        messagebox.showwarning(
            "Update",
            "Please select a maintenance record."
        )
        return


    values = maintenance_table.item(
        selected,
        "values"
    )


    maintenance_id = values[0]


    vehicle_id = vehicle_id_entry.get().strip()
    service_date = service_date_entry.get().strip()
    service_type = service_type_entry.get().strip()
    description = description_entry.get().strip()
    service_cost = service_cost_entry.get().strip()
    next_service_date = next_service_date_entry.get().strip()
    mechanic_name = mechanic_name_entry.get().strip()
    remarks = remarks_entry.get().strip()


    if vehicle_id == "" or service_date == "" or service_type == "":
        messagebox.showwarning(
            "Validation",
            "Please fill required fields."
        )
        return


    if not vehicle_id.isdigit():

        messagebox.showwarning(
            "Validation",
            "Vehicle ID must be a number."
        )

        return


    if service_cost != "":

        try:
            float(service_cost)

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Service cost must be a number."
            )

            return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()


        query = """
            UPDATE maintenance
            SET
                vehicle_id = %s,
                service_date = %s,
                service_type = %s,
                description = %s,
                service_cost = %s,
                next_service_date = %s,
                mechanic_name = %s,
                remarks = %s
            WHERE maintenance_id = %s
        """


        cursor.execute(
            query,
            (
                int(vehicle_id),
                service_date,
                service_type,
                description,
                float(service_cost) if service_cost else None,
                next_service_date if next_service_date else None,
                mechanic_name,
                remarks,
                maintenance_id
            )
        )


        conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo(
            "Success",
            "Maintenance record updated successfully."
        )


        clear_maintenance_fields()
        show_all_maintenance()


    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            str(err)
        )


def delete_maintenance():

    selected = maintenance_table.focus()

    if selected == "":
        messagebox.showwarning(
            "Delete",
            "Please select a maintenance record."
        )
        return


    values = maintenance_table.item(
        selected,
        "values"
    )


    maintenance_id = values[0]


    confirm = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this maintenance record?"
    )


    if not confirm:
        return


    conn = connect_database()

    if conn is None:
        return


    try:

        cursor = conn.cursor()


        cursor.execute(
            "DELETE FROM maintenance WHERE maintenance_id = %s",
            (maintenance_id,)
        )


        conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo(
            "Success",
            "Maintenance record deleted successfully."
        )


        clear_maintenance_fields()
        show_all_maintenance()


    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            str(err)
        )



# MAINTENANCE BUTTONS


maintenance_button_frame = tk.Frame(
    maintenance_frame,
    bg="#F8F6F2"
)

maintenance_button_frame.pack(
    pady=10
)


tk.Button(
    maintenance_button_frame,
    text="Add Record",
    command=add_maintenance,
    font=("Arial", 10, "bold"),
    bg="#E9E2F5",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    maintenance_button_frame,
    text="Update",
    command=update_maintenance,
    font=("Arial", 10, "bold"),
    bg="#DCEEF7",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    maintenance_button_frame,
    text="Delete",
    command=delete_maintenance,
    font=("Arial", 10, "bold"),
    bg="#F5E1E1",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    maintenance_button_frame,
    text="Clear",
    command=clear_maintenance_fields,
    font=("Arial", 10, "bold"),
    bg="#F1E8D8",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)


tk.Button(
    maintenance_button_frame,
    text="Show All",
    command=show_all_maintenance,
    font=("Arial", 10, "bold"),
    bg="#DDEEDC",
    fg="#444444",
    width=14,
    #relief="flat",
    cursor="hand2"
).pack(
    side="left",
    padx=5
)



# MAINTENANCE TABLE


maintenance_table_frame = tk.Frame(
    maintenance_frame,
    bg="#F8F6F2"
)

maintenance_table_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=5
)


maintenance_columns = (
    "ID",
    "Vehicle ID",
    "Service Date",
    "Service Type",
    "Description",
    "Service Cost",
    "Next Service",
    "Mechanic",
    "Remarks"
)


maintenance_table = ttk.Treeview(
    maintenance_table_frame,
    columns=maintenance_columns,
    show="headings",
    height=10
)


for column in maintenance_columns:

    maintenance_table.heading(
        column,
        text=column
    )

    maintenance_table.column(
        column,
        width=115,
        anchor="center"
    )


maintenance_table.column(
    "ID",
    width=45
)


maintenance_table.column(
    "Vehicle ID",
    width=70
)


maintenance_table.pack(
    side="left",
    fill="both",
    expand=True
)


maintenance_scrollbar = ttk.Scrollbar(
    maintenance_table_frame,
    orient="vertical",
    command=maintenance_table.yview
)

maintenance_scrollbar.pack(
    side="right",
    fill="y"
)


maintenance_table.configure(
    yscrollcommand=maintenance_scrollbar.set
)


maintenance_table.bind(
    "<ButtonRelease-1>",
    select_maintenance
)




root.mainloop()

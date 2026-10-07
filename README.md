# Vehicle Maintenance Record System

A simple desktop-based **Vehicle Maintenance Record Management System** developed using **Python, Tkinter, and MySQL**.

This project helps manage vehicle information and keep track of their maintenance and service records through a simple graphical user interface.

## Features

### Login
- Username and password authentication
- Simple login page
- Logout functionality

### Dashboard
- Vehicle Management
- Maintenance Records
- Back and Logout navigation

### Vehicle Management
- Add vehicle records
- View all vehicles
- Update vehicle details
- Delete vehicle records
- Clear form fields
- Store vehicle information in MySQL

### Maintenance Management
- Add maintenance records
- View all maintenance records
- Update maintenance details
- Delete maintenance records
- Clear form fields
- Store maintenance information in MySQL

## Technologies Used

- **Python**
- **Tkinter** – GUI
- **MySQL** – Database
- **mysql-connector-python** – Python-MySQL connection

## Database
```text
vehicle_management
```

### Tables

#### vehicles

Stores vehicle details.

```text
vehicle_id
vehicle_number
owner_name
vehicle_type
brand
model
year
contact
```

#### maintenance

Stores vehicle maintenance records.

```text
maintenance_id
vehicle_id
service_date
service_type
description
service_cost
next_service_date
mechanic_name
remarks
```
## Database Setup

Open MySQL and create the database:

```sql
CREATE DATABASE vehicle_management;

USE vehicle_management;
```

Create the users table:

```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);
```

Add a login user:

```sql
INSERT INTO users (username, password)
VALUES ('admin', 'admin123');
```

Create the vehicles table:

```sql
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_number VARCHAR(20) NOT NULL UNIQUE,
    owner_name VARCHAR(100) NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL,
    brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    contact VARCHAR(15)
);
```

Create the maintenance table:

```sql
CREATE TABLE maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    service_date DATE NOT NULL,
    service_type VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    service_cost DECIMAL(10,2),
    next_service_date DATE,
    mechanic_name VARCHAR(100),
    remarks VARCHAR(255),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);
```
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="_",
    database="vehicle_management"
)
```
## Login Details

For the default user created in the database:

```text
Username: admin
Password: admin123
```
## Project Purpose

The main purpose of this project is to practice:

- Python programming
- Tkinter GUI development
- MySQL database management
- CRUD operations
- Python and MySQL connectivity
- Form validation
- Basic desktop application development

# Vehicle-Maintenance-Record-System
This project helps manage vehicle information and keep track of their maintenance and service records through a simple graphical user interface.

Features

Login

Username and password authentication

Simple login page

Logout functionality

Dashboard

Vehicle Management

Maintenance Records

Back and Logout navigation

Vehicle Management

Add vehicle records

View all vehicles

Update vehicle details

Delete vehicle records

Clear form fields

Store vehicle information in MySQL

Maintenance Management

Add maintenance records

View all maintenance records

Update maintenance details

Delete maintenance records

Clear form fields

Store maintenance information in MySQL

Technologies Used

Python

Tkinter – GUI

MySQL – Database

mysql-connector-python – Python-MySQL connection

Database Setup

Open MySQL and create the database:

CREATE DATABASE vehicle_management;

USE vehicle_management;

Create the users table:

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

Add a login user:

INSERT INTO users (username, password)
VALUES ('admin', 'admin123');

Create the vehicles table:

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

Create the maintenance table:

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

MySQL Connection

In vehicle_management.py, update the database password:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="_",
    database="vehicle_management"
)

Replace YOUR_MYSQL_PASSWORD with your own MySQL password.

Do not upload your real database password to GitHub.

How to Run

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder

cd vehicle-maintenance-record-system

3. Install the required package

pip install mysql-connector-python

4. Set up the MySQL database

Run the SQL commands provided above in MySQL.

5. Update the MySQL password

Open:

vehicle_management.py

and enter your local MySQL password.

6. Run the project

python vehicle_management.py

Login Details

For the default user created in the database:

Username: admin
Password: admin123

You can change the login details directly in the MySQL users table.

Project Purpose

The main purpose of this project is to practice:

Python programming

Tkinter GUI development

MySQL database management

CRUD operations

Python and MySQL connectivity

Form validation

Basic desktop application development

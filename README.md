# Restaurant Management System

This repository contains the project files for the Restaurant Management System, a mini-project developed by Sukhumjeet Singh, Tamanna Dash & Tanisha Jain under the guidance of Dr. G. Usha, Associate Professor in the Department of Computing Technologies at SRM Institute of Science and Technology. This project was completed as part of the course 21CSC205P – Database Management Systems in the Computer Science and Engineering program.

## Project Overview

The Restaurant Management System is designed to manage and streamline various aspects of restaurant operations, including customer information, orders, payments, products, and staff details. The project employs a relational database to store and manage data, and it includes a front-end interface to interact with the system.

## Table of Contents

1. [E-R Diagram](#e-r-diagram)
2. [Relational Tables](#relational-tables)
3. [Tables](#tables)
    - [Customer Table](#customer-table)
    - [Order Table](#order-table)
    - [Payment Table](#payment-table)
    - [Product Table](#product-table)
    - [Staff Table](#staff-table)
4. [Front-End Implementation](#front-end-implementation)
    - [Technologies Used](#technologies-used)
    - [User Interface](#user-interface)
    - [Features](#features)
5. [License](#license)
6. [Acknowledgments](#acknowledgments)

## E-R Diagram
![Architecture Diagram](https://github.com/sukhum29/RestaurantSystem/blob/main/Blank%20diagram-6.png?raw=true)

## Tables

### Customer Table

The "Customer" table holds customer information, including unique customer IDs, names, email addresses, passwords, and phone numbers. Each customer entry is identified by "Customer_Id" and may have associated orders and payments.

### Order Table

The "Order" table tracks customer purchases, storing unique order identifiers, staff assigned to orders, customer IDs, order times, and product IDs. Each order is uniquely identified by "Order_Id" and associated with respective customers and products via foreign keys.

### Payment Table

The "Payment" table records transaction details, featuring unique payment identifiers, staff IDs, order IDs, payment methods, and tip amounts. Each payment entry is identified by "Payment_Id" and linked to respective orders and customers.

### Product Table

The "Product" table catalogs product details, including unique product IDs, names, cuisine types, descriptions, and prices. Each product entry is identified by "Product_Id" and may be associated with multiple orders through foreign key relationships.

### Staff Table

The "Staff" table maintains information about employees, encompassing unique staff IDs, names, roles, email addresses, and commission rates. Each staff member is identified by "Staff_Id" and may be associated with orders and payments, contributing to order handling and transaction processing.

## Front-End Implementation

### Technologies Used

- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **JavaScript**: For adding interactivity to the web pages.
- **Bootstrap**: For responsive design and pre-built components.
- **React**: For building a dynamic and modern user interface.

### User Interface

The front-end of the Restaurant Management System includes the following key components:

- **Home Page**: Introduction and navigation to other sections of the application.
- **Customer Management**: Form to add new customers, view customer details, and update customer information.
- **Order Management**: Interface to place new orders, view existing orders, and update order status.
- **Payment Management**: Page to process payments, view payment history, and manage payment methods.
- **Product Catalog**: Display of available products, with options to add new products or update existing product details.
- **Staff Management**: Form to add new staff members, view staff details, and update staff information.

### Features

- **Responsive Design**: The application is designed to be responsive and works well on various devices, including desktops, tablets, and mobile phones.
- **Interactive Forms**: User-friendly forms for entering and updating data.
- **Real-Time Data Display**: Dynamic tables and lists to display customer, order, payment, product, and staff information.
- **Validation and Error Handling**: Proper validation and error handling to ensure data integrity and user feedback.


## Acknowledgments

- Dr. G. Usha, Associate Professor, Department of Computing Technologies, SRM Institute of Science and Technology

---

Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.# RestaurantSystem

# 📦 Vikmo – Sales Order & Inventory Management System

1️⃣ Project Overview

This project is a backend-based Sales Order & Inventory Management System developed using Django and Django REST Framework.

The system is designed for a B2B auto-parts distribution platform where:

Suppliers provide products

Dealers place sales orders

Inventory is updated automatically

APIs allow system integration

The focus of this project is backend logic, REST API development, atomic transactions, and clean architecture.


2️⃣ Technology Stack

Python 3.10+

Django 4.2+

Django REST Framework

SQLite (default database)

PostgreSQL (optional)

Docker & Docker Compose

Postman (API testing)

Git & GitHub

3️⃣ Functional Requirements Implemented

Product Management

Create Product

Update Product

View Product List

Track SKU, price, and stock

Dealer Management

Create Dealer

Update Dealer

View Dealer List

Sales Order Management

Create Sales Order

Add multiple Order Items

Auto-calculate total amount

Maintain order status

Inventory Management

Inventory linked one-to-one with Product

Stock automatically reduces when order is placed

Validation prevents negative stock

Authentication & Authorization

Django built-in authentication

Role-based access using Django permissions

4️⃣ Database Schema Overview
Models Used
Product

SKU (unique)

Name

Price

Stock quantity

Category

Supplier

Dealer

Name

Contact details

Unique dealer identifier

Order

Unique order number

Linked Dealer

Status

Total amount

Created timestamp

OrderItem

Linked Order

Linked Product

Quantity

Price at order time

Line total

Inventory

One-to-one with Product

Maintains real-time stock

5️⃣ API Endpoints

All APIs are built using Django REST Framework.

Example endpoints:

GET /api/products/

POST /api/products/

GET /api/dealers/

POST /api/orders/

GET /api/orders/{id}/

Detailed API documentation available in:

README_API.md

6️⃣ Atomic Transactions Handling

Order creation and inventory deduction are handled using database transactions.

If stock is insufficient, order creation fails.

Ensures data consistency and integrity.

7️⃣ Assumptions Made

Inventory is maintained per product.

Order price is stored at order time (price history preserved).

Only authenticated users can access APIs.

Stock updates happen only during confirmed order creation.

8️⃣ Setup Instructions
Clone Repository
git clone https://github.com/NithinYD/sales-order-inventory-lite.git
cd sales-order-inventory-lite
Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
Install Dependencies
pip install -r requirements.txt
Run Migrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser
Run Server
python manage.py runserver

9️⃣ API Testing

Postman collection included:

vikmo_postman_collection.json

Steps:

Open Postman

Import collection file

Test all endpoints

Verify responses

🔟 Submission Checklist

✔ Source code included
✔ Migrations included
✔ API documentation included
✔ Postman collection included
✔ No hardcoded credentials
✔ Clean project structure

👨‍💻 Candidate Information

Name: Nithin Y D
Email: nithincoorg535@gmail.com
Phone: +91 9148380171

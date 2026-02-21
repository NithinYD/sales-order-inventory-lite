# Vikmo Sales Order & Inventory Management System

## Features Implemented
- Product, Dealer, Inventory, Order, OrderItem models
- RESTful API endpoints for all entities
- Stock validation and deduction logic
- Order status transitions (Draft → Confirmed → Delivered)
- Error handling for invalid transitions and insufficient stock
- Atomic transactions for stock changes
- Price preservation at order time

## Tech Stack
- Python 3.10+
- Django 4.2+
- Django REST Framework
- SQLite (default)

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run server:
   ```bash
   python manage.py runserver
   ```

## API Documentation
See README_API.md for endpoint details and example requests.

## Database Schema Diagram
- Product: SKU, pricing, category, supplier, warehouse, stock, etc.
- Inventory: One-to-one with Product, tracks quantity
- Dealer: Unique, contact info
- Order: Unique number, dealer, status, total, timestamps
- OrderItem: Links order to product, quantity, price, line total

## Assumptions
- Inventory is managed per product
- Orders and stock changes are atomic
- Price at order time is preserved

## Sample Data & Seed Scripts
- Add products, dealers, and inventory via admin or API

## Postman Collection
- See README_API.md for curl examples

## Submission Checklist
- [x] Code and migrations included
- [x] API docs and README
- [x] No hardcoded credentials
- [x] Sample data via admin/API

---
For any questions, see the code or contact the maintainer.

# Vikmo API Testing (curl examples)

# 1. List Products
curl -X GET http://localhost:8000/api/products/

# 2. Create Product
curl -X POST http://localhost:8000/api/products/ -H "Content-Type: application/json" -d '{"product_name": "Brake Pad", "selling_price": 500, "purchase_price": 400, "tax_rate": 18.0, "category": 1, "warehouse": 1, "supplier": 1, "stock": 100}'

# 3. List Dealers
curl -X GET http://localhost:8000/api/dealers/

# 4. Create Dealer
curl -X POST http://localhost:8000/api/dealers/ -H "Content-Type: application/json" -d '{"name": "ABC Motors", "phone_number": "1234567890", "email": "abc@example.com"}'

# 5. List Orders
curl -X GET http://localhost:8000/api/orders/

# 6. Create Order
curl -X POST http://localhost:8000/api/orders/ -H "Content-Type: application/json" -d '{"dealer": 1, "items": [{"product": 1, "quantity": 10, "unit_price": 500}]}'

# 7. Confirm Order
curl -X POST http://localhost:8000/api/orders/1/confirm/

# 8. Deliver Order
curl -X POST http://localhost:8000/api/orders/1/deliver/

# 9. List Inventory
curl -X GET http://localhost:8000/api/inventory/

# 10. Manual Inventory Adjustment (Admin Only)
curl -X PUT http://localhost:8000/api/inventory/1/ -H "Content-Type: application/json" -d '{"quantity": 120}'

# Error Handling Example
# Try confirming an order with insufficient stock
curl -X POST http://localhost:8000/api/orders/2/confirm/

# Invalid Status Transition Example
curl -X POST http://localhost:8000/api/orders/1/deliver/
# (if not confirmed, should return error)

---
# Replace IDs as needed based on your data.
# Use these commands in your terminal to test the API endpoints.

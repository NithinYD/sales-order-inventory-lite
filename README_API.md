# Vikmo Sales Order & Inventory Management API Documentation

## Overview
This API allows management of products, dealers, inventory, and sales orders. It enforces business rules for stock validation, order status, and inventory deduction.

### Base URL
`/api/`

## Endpoints

### Products
- `GET /api/products/` — List all products
- `POST /api/products/` — Create new product
- `GET /api/products/{id}/` — Get product details
- `PUT /api/products/{id}/` — Update product
- `DELETE /api/products/{id}/` — Delete product

### Dealers
- `GET /api/dealers/` — List all dealers
- `POST /api/dealers/` — Create new dealer
- `GET /api/dealers/{id}/` — Get dealer details
- `PUT /api/dealers/{id}/` — Update dealer

### Inventory (Admin Only)
- `GET /api/inventory/` — List all inventory levels
- `PUT /api/inventory/{product_id}/` — Manual stock adjustment

### Orders
- `GET /api/orders/` — List all orders
- `POST /api/orders/` — Create new draft order
- `GET /api/orders/{id}/` — Get order with items
- `PUT /api/orders/{id}/` — Update draft order
- `POST /api/orders/{id}/confirm/` — Confirm order (validates stock)
- `POST /api/orders/{id}/deliver/` — Mark as delivered

### Order Items
- `GET /api/order-items/` — List all order items
- `POST /api/order-items/` — Create order item

## Example Requests

### Create Product
```bash
curl -X POST /api/products/ -H "Content-Type: application/json" -d '{"product_name": "Brake Pad", "selling_price": 500, ...}'
```

### Create Dealer
```bash
curl -X POST /api/dealers/ -H "Content-Type: application/json" -d '{"name": "ABC Motors", ...}'
```

### Create Order
```bash
curl -X POST /api/orders/ -H "Content-Type: application/json" -d '{"dealer": 1, "items": [{"product": 1, "quantity": 10, "unit_price": 500}]}'
```

### Confirm Order
```bash
curl -X POST /api/orders/{id}/confirm/
```

### Deliver Order
```bash
curl -X POST /api/orders/{id}/deliver/
```

## Error Handling
- Insufficient stock: `{ "error": "Insufficient stock for some products.", "details": [{ "product": "Brake Pad", "available": 5, "requested": 10 }] }`
- Invalid status transition: `{ "error": "Only draft orders can be confirmed." }`

## Assumptions
- Inventory is managed per product.
- Orders and stock changes are atomic.
- Price at order time is preserved.

---
For more details, see the code and README.

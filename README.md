# Django Inventory Management System

A complete **Inventory Management System** built with **Django** and **PostgreSQL**. This project helps businesses manage **stock, sales, purchase, and reporting** efficiently. Perfect for **students, developers, and small businesses** looking for a free open-source solution.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-Django-092E20?logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/License-GPLv3-yellow?logo=gnu" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/github/issues/shahzaib-1-no/inventory-management?color=orange&logo=github" />
  <img src="https://img.shields.io/github/stars/shahzaib-1-no/inventory-management?logo=github" />
  <img src="https://img.shields.io/github/forks/shahzaib-1-no/inventory-management?logo=github" />
  <img src="https://img.shields.io/github/last-commit/shahzaib-1-no/inventory-management?logo=git" />
  <img src="https://img.shields.io/github/repo-size/shahzaib-1-no/inventory-management?logo=github" />
</p>

<p align="center">
  <img src="https://github.com/shahzaib-1-no/inventory-management/actions/workflows/django.yml/badge.svg" />
  <a href="https://codecov.io/gh/shahzaib-1-no/inventory-management">
    <img src="https://codecov.io/gh/shahzaib-1-no/inventory-management/branch/main/graph/badge.svg" />
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" />
  </a>
  <img src="https://img.shields.io/badge/lint-Flake8-blue" />
  <img src="https://img.shields.io/badge/lint-Pylint-yellow" />
  <a href="https://snyk.io/test/github/shahzaib-1-no/inventory-management">
    <img src="https://snyk.io/test/github/shahzaib-1-no/inventory-management/badge.svg" />
  </a>
  <img src="https://img.shields.io/badge/security-Bandit-red" />
  <img src="https://img.shields.io/github/contributors/shahzaib-1-no/inventory-management" />
</p>

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Use Cases](#-use-cases)
- [⚙️ Installation Guide](#️-installation-guide)
- [⚙️ Dummy Data Commands (Optional)](#-dummy-data-commands-optional)
- [📸 Screenshots](#-screenshots)
- [📜 Changelog](#-changelog)
- [📄 License](#-license)
- [🤝 Contributing](#-contributing)
- [🔒 Security](#-security)
- [⭐ Support](#-support)
- [👨‍💻 Author](#-author)

---

## 🚀 Features

- 📦 **Product Management** – Add, update, and track inventory in real-time _(🚧 Planned Feature)_
- 🏢 **Warehouse Management** – Manage storage locations and stock distribution _(🚧 Planned Feature)_
- 🛒 **Purchase Management** – Manage supplier purchases, purchase orders, and expenses _(🚧 Planned Feature)_
- 🤝 **Supplier Management** – Maintain supplier profiles, contact details, and transaction history _(🚧 Planned Feature)_
- 📊 **Reports & Analytics** – Generate daily, monthly, and custom reports using Chart.js _(🚧 Planned Feature)_
- 👤 **User Management** – Manage users, roles, and permissions (RBAC integration)
- 🔐 **Secure Authentication** – Django’s built-in auth system with login/logout and role-based access
- 📁 **Role-Based Access Control (RBAC)** – Fine-grained permission handling for each module
- ⚙️ **Dynamic DataTables Integration** – Server-side pagination, sorting, and searching
- 🚨 **SweetAlert2 Integration** – Elegant alerts for confirmations and success/error messages
- 🧾 **Export & Reporting** – Export data to Excel or PDF for business analytics _(🚧 Planned Feature)_
- 🧱 **Modular Architecture** – Organized Django apps for Users, Roles, Products, and Inventory
- 🌐 **Dockerized Setup** – Pre-configured Docker environment for local and production use
- 🧩 **Responsive Dashboard** – Clean, mobile-friendly UI built with Bootstrap 5

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3.9+) with Django ORM
- **Database:** PostgreSQL
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript (ES6)
- **Libraries & Tools:**

  - DataTables → For server-side data tables
  - SweetAlert2 → For confirmation dialogs and alerts
  - Django Environ → For environment variable management

- **Authentication & Authorization:** Django Auth System + Built-in RBAC
- **Containerization:** Docker & Docker Compose
- **Code Quality:** Black, Flake8, isort
- **Version Control:** Git & GitHub

---

## 📈 Use Cases

- Small shops & businesses to manage stock and sales
- Students learning Django + PostgreSQL projects
- Developers building POS or ERP-like systems
- Open-source learning reference

---

## ⚙️ Installation Guide

1. **Clone the repository**

   ```bash
   git clone https://github.com/shahzaib-1-no/inventory-management.git
   cd inventory-management
   ```

2. **Create virtual environment & activate**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **⚙️ Set up the database (PostgreSQL) and rename the `.env.example` file to `.env`.**
   Make sure to **fill in all required environment variables** before running the project.
   🔸 _This step is mandatory — the project won’t run without proper configuration._
   (See example file → [.env.example](./.env.example))

   ```bash
   # 🔐 Django Secret Key (replace with your own)
   # To generate a new key, run:
   # python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

   SECRET_KEY=your-secret-key-here

   # 🗄️ Database Configuration
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432

   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start server**

   ```bash
   python manage.py runserver
   ```

---

## ⚙️ Dummy Data Commands (Optional)

These commands help you **quickly generate sample data** for testing or demo purposes.
Each command supports an optional `--total` argument to specify the number of records to create (default is **10**).

---

### 🧩 Seed Roles & Permissions

Populates the database with default **roles** (groups) and **permissions** for testing access control.

```bash
python manage.py seed_group --total 10
```

**Default:** 10 groups
**Optional:** `--total` to specify how many groups to create

---

### 👥 Seed Users

Generates dummy **user accounts** linked with random roles.
Useful for testing authentication, role-based access, or dashboards.

```bash
python manage.py seed_user --total 10
```

**Default:** 10 users
**Optional:** `--total` for a custom number

---

### 🏷️ Seed Categories

Creates fake **product categories** to organize your data and make testing product listings easier.

```bash
python manage.py seed_category --total 10
```

**Default:** 10 categories

---

### 🏢 Seed Warehouses

Adds **dummy warehouse records** to simulate stock management or logistics scenarios.

```bash
python manage.py seed_warehouse --total 10
```

**Default:** 10 warehouses

---

### 🚚 Seed Suppliers

Generates **fake supplier entries** with random company names and contact details.
Ideal for supply chain or procurement module testing.

```bash
python manage.py seed_supplier --total 10
```

**Default:** 10 suppliers

---

### 📦 Seed Products

Creates **sample product records** linked with categories, suppliers, and warehouses.
Useful for testing inventory, pricing, or order management.

```bash
python manage.py seed_product --total 10
```

**Default:** 10 products

---

## 📸 Screenshots

(Add screenshots or GIFs of your project UI here for better impact on portfolio & ranking)

---

## 📜 Changelog

- **v1.1.0** – Added Category, Inventory, Warehouse, and Supplier management modules with CRUD functionality.
- **v1.0.0** – Introduced RBAC (Role-Based Access Control), User Management, Roles & Permissions CRUD, SweetAlert2 integration, and AJAX-based DataTables.
- **v0.1.0** – Initial project setup with Docker, PostgreSQL, Authentication system, base templates, and static file configuration.

👉 See full changelog in [CHANGELOG.md](./CHANGELOG.md)

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.
You must give appropriate credit by mentioning the author **[Shahzaib Ali](https://github.com/shahzaib-1-no)** whenever using this project.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, submit issues, or create pull requests.

---

## 🔒 Security

If you discover any security issues, please report them via email instead of creating a public issue.

---

## ⭐ Support

If you like this project, please **star the repository** on GitHub. It helps others find it and supports the project growth.

---

## 🔹 Author

👨‍💻 Created & maintained by [Shahzaib Ali](https://github.com/shahzaib-1-no)
📬 For collaboration or freelance work: **[sa4715228@gmail.com](mailto:sa4715228@gmail.com)**

---

# Vikmo Sales Order & Inventory Management System

## Project Overview
A B2B SaaS platform for auto parts distribution, connecting suppliers and dealers. Features sales order management, inventory tracking, and RESTful APIs.

## Tech Stack
- Python 3.10+
- Django 4.2+
- Django REST Framework
- SQLite (default, can use PostgreSQL)

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements/base.txt
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

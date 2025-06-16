# 🏢 Company Management System (Django + DRF)

A full-featured Django REST API-based employee management system with **role-based authentication** and **token-based login/logout**, supporting Admin, HOD, and Employee access levels.

---

## 🚀 Features

- 🔐 **Token-based Authentication** using Django REST Framework
- 👥 **Role-based Access Control**
  - **Admin**: Full access to all resources
  - **HOD**: Access to their department’s data and projects
  - **Employee**: Access to their own profile and assigned projects
- 📄 Employee profile API with nested data (department, role, reporting manager, etc.)
- 🧩 Clean separation between authentication and business logic
- ✅ Login/Logout with Token creation and revocation
- 🔧 Fully integrated with DRF `viewsets` and permissions

---

## 📦 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (or MySQL/PostgreSQL, configurable)
- Token Authentication (`rest_framework.authtoken`)

---

## 🔧 Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/employee-management-django.git
cd employee-management-django

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver

RBACPro - Role-Based Access Control Web Application
Project Overview

RBACPro is a full-featured web application built using Flask, SQLite, and Bootstrap, designed to demonstrate Role-Based Access Control (RBAC) for user management and resource access. The application supports three roles: Admin, Manager, and User, with different permissions for each.

Admin: Full control, can manage users, assign roles, and CRUD resources.

Manager: Can create, edit, and view resources.

User: Can view resources only.

The project also includes a modern admin dashboard interface, tables with search/sort capabilities, and role-based resource access.

Features
Authentication & Authorization

User registration and login with password hashing (bcrypt).

Role-based access control using decorators.

Session management via Flask-Login.

Resource Management

Admin/Manager: Create, edit, delete resources.

User: View resources only.

Timestamps for resource creation.

User Management

Admin dashboard to list users.

Change roles or delete users.

UI / Frontend

Responsive dashboard with Bootstrap 5.

Sidebar menu with icons and active highlights.

Tables for users and resources with search, sort, and pagination.

Project Structure
RBACPro/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models (User, Role, Resource)
│   ├── auth.py              # Authentication routes (login, register)
│   ├── routes.py            # Main routes (dashboard, resource CRUD)
│   ├── decorators.py        # Role-based access decorators
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── admin_dashboard.html
│   │   ├── admin_users.html
│   │   ├── manager_dashboard.html
│   │   ├── create_resource.html
│   │   └── edit_resource.html
│   └── static/
│       ├── css/style.css
│       └── js/script.js
├── instance/
│   └── rbacpro.db           # SQLite database
├── run.py                   # Entry point
├── requirements.txt         # Python dependencies
└── config.py                # Configuration

Technologies Used

Backend: Python, Flask, SQLAlchemy

Frontend: HTML, CSS, Bootstrap 5, JavaScript

Database: SQLite

Authentication: Flask-Login, Bcrypt for password hashing

Version Control: Git & GitHub

Installation & Setup

Clone the repository

git clone https://github.com/your-username/RBACPro.git
cd RBACPro


Create a virtual environment

python -m venv venv


Activate the virtual environment

Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the app

python run.py


Access the application
Open your browser at http://127.0.0.1:5000

Usage

Register a new user and select a role (Admin, Manager, User).

Log in with your credentials.

Based on your role:

Admin: Manage users, create/edit/delete resources.

Manager: Create/edit resources.

User: View resources.

Navigate dashboards from the sidebar menu.

Role Permissions
Role	Access
Admin	Manage users, create/edit/delete resources
Manager	Create/edit resources
User	View resources only
Screenshots

(Optional: Add screenshots of dashboard, login, resource tables, etc.)

Future Enhancements

Add Audit Logs for user actions.

Implement email verification during registration.

Add export/import resources (CSV, Excel).

Implement REST API endpoints for resource access.

License

This project is open-source under the MIT License.

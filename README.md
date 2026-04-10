# Django Blog Assignment

This repository contains a Django blog application with:

- User registration and login/logout
- Blog create, edit, delete, and list views
- Category and tag support
- Image and file upload for blog posts
- CSV upload for bulk blog creation
- Basic REST API endpoints for listing and creating blogs

## Tech Stack

- Python
- Django 5.2.13
- Django REST Framework 3.17.1
- SQLite (default database)

## Project Layout

- `myproject/manage.py` - Django management entry point
- `myproject/myproject/settings.py` - project settings
- `myproject/blog/` - main app (models, views, forms, templates, api)
- `myproject/db.sqlite3` - SQLite database
- `blog.csv` - sample CSV file for upload feature

## Prerequisites

- Python 3.10+ (recommended)
- pip

## How To Run

1. Open terminal at the repository root (`django-assignment`).
2. Create a virtual environment:

```powershell
python -m venv .venv
```

3. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```powershell
pip install -r requirements.txt
```

5. Move into the Django project directory:

```powershell
cd myproject
```

6. Apply migrations:

```powershell
python manage.py migrate
```

7. Start the development server:

```powershell
python manage.py runserver
```

8. Open in browser:

- Home page: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Main Routes

- `/` - blog list
- `/add/` - add blog (login required)
- `/edit/<id>/` - edit blog (owner only)
- `/delete/<id>/` - delete blog (owner only)
- `/register/` - user registration
- `/accounts/login/` - login
- `/upload_csv/` - CSV upload (login required)
- `/api/blogs/` - list blogs API
- `/api/add-blog/` - create blog API

## Notes

- Media uploads are stored in `myproject/media/`.
- Static files are served by Django in development mode.
- Email settings are configured for SMTP in project settings.
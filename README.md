# Django Assignment

This repository contains a multi-module Django project that combines:

- Blog management (CRUD, categories, tags, image/file upload)
- User authentication (register, login, logout)
- Lead management (CRM-style tracking)
- Generic file upload and categorization
- CSV/Excel upload and database import
- Dashboard analytics for users and admins
- Basic REST API endpoints for blogs

## Tech Stack

- Python
- Django 5.2.13
- Django REST Framework 3.17.1
- SQLite (default database)
- Pandas + OpenPyXL (CSV/XLSX parsing)
- Pillow (image upload support)

## Project Structure

- myproject/manage.py: Django management entry point
- myproject/myproject/settings.py: global settings
- myproject/myproject/urls.py: root URL routing
- myproject/blog/: blog app (web + API)
- myproject/leads/: lead management app
- myproject/files/: file management app
- myproject/excel/: CSV/Excel import app
- myproject/dashboard/: metrics dashboard app
- myproject/media/: uploaded files and images
- REVISION_GUIDE.md: complete revision notes for interview/exam prep

## Requirements

- Python 3.10+
- pip

Install dependencies from repository root:

1. Create virtual environment:
	python -m venv venv
2. Activate (PowerShell):
	.\venv\Scripts\Activate.ps1
3. Install packages:
	pip install -r requirements.txt

Main dependencies:

- Django==5.2.13
- djangorestframework==3.17.1
- pillow==12.2.0
- pandas
- openpyxl

## Run The Project

From repository root:

1. cd myproject
2. python manage.py migrate
3. python manage.py runserver

Open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## URL Map

Root routes:

- / -> blog app
- /accounts/ -> Django auth routes
- /leads/ -> leads app
- /files/ -> files app
- /excel/ -> excel app
- /dashboard/ -> dashboard app
- /admin/ -> admin panel

Blog routes:

- / -> blog list with search/filter/pagination
- /add/ -> add blog
- /edit/<id>/ -> edit blog (owner only)
- /delete/<id>/ -> delete blog (owner only)
- /register/ -> registration
- /upload_csv/ -> CSV upload for blog creation
- /api/blogs/ -> list blog API
- /api/add-blog/ -> create blog API

## Key Features By App

blog:

- Category and tag support
- Image and file uploads per post
- Search by title/description
- Category filter and pagination
- Owner-based edit/delete authorization
- Registration flow with welcome email

leads:

- Add/edit/delete leads
- Status tracking: new/contacted/closed
- Per-user lead access

files:

- Upload files with category
- Per-user file listing and filtering

excel:

- Upload CSV or Excel files
- Parse rows into DataRecord table using Pandas
- Per-user data listing

dashboard:

- Admin sees global totals
- Normal users see their own totals only

## Authentication And Access

- Login is required for most create/update/delete actions.
- Login route: /accounts/login/
- Owner checks are enforced in blog and leads operations.

## Media And Static

- Uploaded content is stored in myproject/media/.
- Media is served in development via URL config.

## Study Notes

For full revision notes (models, flow, common viva questions), see:

- REVISION_GUIDE.md
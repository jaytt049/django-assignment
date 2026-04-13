# Django Assignment Revision Guide

This file is a quick revision companion for the full project.

## 1) Project Snapshot

- Framework: Django 5.2.13
- Database: SQLite
- APIs: Django REST Framework
- File handling: Pillow (images), Pandas/OpenPyXL (CSV/Excel)
- Main apps:
  - blog
  - leads
  - files
  - excel
  - dashboard

## 2) Folder-Level Architecture

- myproject/myproject/: global Django settings, root urls, wsgi/asgi.
- myproject/blog/: blog CRUD, registration, CSV import, API endpoints.
- myproject/leads/: lead management CRUD with per-user ownership.
- myproject/files/: categorized file upload/list for logged-in users.
- myproject/excel/: CSV/XLSX upload and row parsing into database.
- myproject/dashboard/: aggregate metrics page for users/admin.
- myproject/media/: uploaded assets (blog images/files, excel, files app).

## 3) URL Routing Map

Root router in myproject/myproject/urls.py:

- /admin/ -> Django admin
- / -> blog app urls
- /accounts/ -> Django built-in auth urls
- /leads/ -> leads urls
- /files/ -> files urls
- /excel/ -> excel urls
- /dashboard/ -> dashboard urls

Blog routes:

- / -> blog list
- /add/ -> add blog
- /edit/<id>/ -> edit blog (owner only)
- /delete/<id>/ -> delete blog (owner only)
- /register/ -> user signup
- /upload_csv/ -> upload CSV for blog creation
- /api/blogs/ -> API list blogs
- /api/add-blog/ -> API create blog

Leads routes:

- /leads/ -> list leads
- /leads/add/ -> create lead
- /leads/edit/<id>/ -> edit lead
- /leads/delete/<id>/ -> delete lead

Files routes:

- /files/ -> list uploaded files
- /files/upload/ -> upload a file

Excel routes:

- /excel/ -> data list page
- /excel/upload/ -> upload CSV/XLSX
- /excel/data/ -> data list page

Dashboard route:

- /dashboard/ -> analytics summary

## 4) Data Models You Should Remember

blog app:

- Category(name)
- Tag(name)
- Profile(user one-to-one, bio)
- Blog(user FK, title, description, date, category FK, tags M2M, image, file)

leads app:

- Lead(name, email, phone, status[new/contacted/closed], created_by, created_at)

files app:

- FileCategory(name)
- File(title, file, category FK, uploaded_by, uploaded_at)

excel app:

- UploadedFile(file, uploaded_by, uploaded_at)
- DataRecord(name, email, age, uploaded_file FK)

## 5) Core Business Logic (High Value for Revision)

- Blog search/filter: query by title/description, optional category filter, pagination (3 per page).
- Blog authorization: only owner can edit/delete their post.
- CSV to Blog import: reads CSV rows and creates Blog rows with current user.
- Registration: creates user and sends welcome email.
- Leads and Files security: queries scoped to current logged-in user.
- Excel upload parsing:
  - uploads file
  - reads using Pandas (read_csv or read_excel)
  - creates DataRecord entries row-by-row
- Dashboard role split:
  - superuser sees global totals
  - normal user sees only personal totals

## 6) Forms and Serializers

- BlogForm includes title/description/category/tags/image/file.
- RegisterForm extends UserCreationForm.
- CSVUploadForm uses FileField.
- LeadForm, FileForm, UploadFileForm are ModelForms.
- BlogSerializer uses all Blog model fields.

## 7) Authentication and Permissions

- Django auth routes included under /accounts/.
- LOGIN_URL is /accounts/login/.
- Most create/update/delete flows are protected with @login_required.
- Ownership checks are explicitly used in blog and leads operations.

## 8) Important Settings to Revise

- INSTALLED_APPS includes rest_framework and all custom apps.
- MEDIA_URL and MEDIA_ROOT are configured for uploaded files.
- Static/media served in development via root urls.py.
- SMTP email settings exist in settings.py (used in register flow).

## 9) Common Viva / Interview Questions

1. Why use commit=False in ModelForm save?
   - To attach user/owner fields before writing to database.

2. Why use get_object_or_404?
   - To safely fetch object or return 404 if not found.

3. Why use Q objects?
   - To perform OR-based filtering logic in queries.

4. Why use paginator?
   - To reduce page load size and improve UX/performance.

5. Why use @login_required?
   - To restrict protected routes to authenticated users.

6. Difference between ModelForm and Serializer?
   - ModelForm targets HTML forms/templates, Serializer targets API payload validation/representation.

## 10) Quick Run Checklist

1. Create and activate virtual environment.
2. Install dependencies from requirements.txt.
3. cd myproject
4. python manage.py migrate
5. python manage.py runserver
6. Open:
   - /
   - /accounts/login/
   - /leads/
   - /files/
   - /excel/
   - /dashboard/

## 11) Suggested Improvement Areas (for extra preparation)

- Move sensitive values in settings.py to environment variables.
- Add model-level/test coverage for permission checks.
- Add robust CSV/Excel validation with user feedback for bad rows.
- Add API authentication and status codes for DRF endpoints.
- Add custom managers/querysets for reusable user-scoped filtering.
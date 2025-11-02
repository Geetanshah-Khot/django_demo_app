# Django Demo App with PostgreSQL

A simple web application built using **Django + Django REST Framework + PostgreSQL**, demonstrating CRUD APIs, API integration, and data visualization.

---

## 🚀 Features

- **CRUD Operations** for managing tasks  
  (Endpoints under `/api/tasks/`)
- **External API Integration** using a joke API  
  (`/api/joke/`)
- **Data Visualization** with Matplotlib  
  (`/api/report/` bar chart)

---

## 🧰 Tech Stack

- Python 3.11+  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- Matplotlib  
- Requests

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/django_demo_app.git
   cd django_demo_app
2. Create and activate a virtual environment:
  ```bash
  
   python -m venv venv
   venv\Scripts\activate     # Windows or
   source venv/bin/activate  # macOS/Linux
  ```

3. Install dependencies:
  ```pip install -r requirements.txt```

4. Configure PostgreSQL in demo_app/settings.py:
  ```
   DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.postgresql",
         "NAME": "demo_db",
         "USER": "postgres",
         "PASSWORD": "yourpassword",
         "HOST": "localhost",
         "PORT": "5432",
     }
   }
  ```

5. Run migrations:
  ```
   python manage.py makemigrations
   python manage.py migrate
  ```

6. Start the server:
  ```
   python manage.py runserver
  ```

7. Open in browser:

   API Root: http://127.0.0.1:8000/api/

   Report: http://127.0.0.1:8000/api/report/

   Jokes API: http://127.0.0.1:8000/api/joke/

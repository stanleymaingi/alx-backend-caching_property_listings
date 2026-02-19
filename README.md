# 🏠 ALX Backend Caching – Property Listings

## 📌 Project Overview

This project sets up a Django backend for a Property Listing application using:

- Django
- PostgreSQL (Dockerized)
- Redis (Dockerized)
- Docker Compose

The system demonstrates database configuration, caching with Redis, and containerized services.

---

# 🚀 1. Prerequisites

Make sure the following are installed on your machine:

- Python 3.10+
- pip
- Docker Desktop
- Git

---

# 🐍 2. Create and Setup Virtual Environment

## Step 1: Navigate to your project directory

```bash
cd Desktop
```

## Step 2: Create virtual environment

```bash
python -m venv venv
```

## Step 3: Activate virtual environment

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

# 📦 3. Install Required Packages

```bash
pip install django psycopg2-binary django-redis
```

Verify installation:

```bash
python -m django --version
```

---

# 🏗 4. Create Django Project

```bash
python -m django startproject alx_backend_caching_property_listings
cd alx_backend_caching_property_listings
```

Create the app:

```bash
python manage.py startapp properties
```

---

# 🗄 5. Create Property Model

Edit:

`properties/models.py`

```python
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

# 🐳 6. Setup Docker (PostgreSQL & Redis)

## Install Docker Desktop

Download from:

https://www.docker.com/products/docker-desktop/

Restart your computer after installation.

Verify Docker:

```bash
docker --version
```

---

## Create `docker-compose.yml`

In project root:

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:latest
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: property_db
      POSTGRES_USER: property_user
      POSTGRES_PASSWORD: property_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:latest
    container_name: redis_cache
    restart: always
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

# ⚙️ 7. Configure Django Settings

Edit:

`alx_backend_caching_property_listings/settings.py`

---

## Add Installed Apps

```python
INSTALLED_APPS = [
    ...
    'properties',
]
```

---

## Configure PostgreSQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'property_db',
        'USER': 'property_user',
        'PASSWORD': 'property_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Configure Redis Cache

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

---

## Fix Auto Field Warning

Add:

```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

# ▶️ 8. Start Docker Services

From project root:

```bash
docker compose up -d
```

Confirm containers are running:

```bash
docker ps
```

---

# 🛠 9. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 👤 10. Create Superuser

```bash
python manage.py createsuperuser
```

---

# 🌐 11. Run Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/admin
```

---

# 📂 Project Structure

```
alx_backend_caching_property_listings/
│
├── alx_backend_caching_property_listings/
│   ├── settings.py
│   └── ...
│
├── properties/
│   ├── models.py
│   └── ...
│
├── docker-compose.yml
├── manage.py
└── README.md
```

---

# 🧪 Testing Redis Connection (Optional)

Open Django shell:

```bash
python manage.py shell
```

Test cache:

```python
from django.core.cache import cache
cache.set("test_key", "Hello Redis", 30)
cache.get("test_key")
```

If it returns `"Hello Redis"` then Redis is working.

---

# 🛑 Stop Docker Services

```bash
docker compose down
```

---

# ✅ Completed Setup

You now have:

- Django backend
- Dockerized PostgreSQL
- Dockerized Redis
- Redis cache configured
- Property model migrated

# Backstone Capstone: Blogging PlatformAPI
Alx curriculum for learning backend development
# Django Backend Development with ALX Africa

Welcome to my Django backend development journey! This project is part of the **ALX Africa curriculum** to gain hands-on experience in web development with Django, Django restframe, Git, and Deployment on PythonAnywhere.

---

## Table of Contents
1. [About the Project](#about-the-project)
2. [Learning Objectives](#learning-objectives)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Features](#features)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

---

## About the Project

This repository contains projects and exercises to build a strong foundation in Django. By the end of the curriculum, I have built a fully functional backend with a database, RESTful APIs, and robust user authentication.

---

## Learning Objectives

- Understand the Django framework and its components.
- Create and manage Django apps.
- Implement models, views, and templates in Django.
- Work with Django ORM for database operations.
- Develop REST APIs using Django REST Framework (DRF).
- Set up user authentication and authorization.
- Deploy Django applications to production.

---

## Technologies Used

- **Programming Language**: Python 3.11+
- **Framework**: Django 4.x
- **Database**: SQLite (default), PostgreSQL (optional)
- **Tools**: Git, VS Code, Postman
- **Deployment**: PythonAnywhere

---

## Setup and Installation

### Prerequisites
- Python 3.11+
- Git
- Virtual Environment (`venv` or `pipenv`)

### Installation Steps
1. Clone the repository:
   
   git clone https://github.com/Babatunde-Odunlami/BloggingPlatformAPI/Blog_Capstone.git
   


# BlogProject

## Overview
The **BlogProject** is a Django-based application that provides a RESTful API for managing blog posts, comments, categories, and users. The project leverages Django REST Framework for API functionality, SQLite as the database, and includes features like user authentication, pagination, and filtering.

---

## Features

- **User Management**:
  - Create, retrieve, update, and delete user accounts.
  - Authentication using BasicAuth, TokenAuth, and SessionAuth.

- **Post Management**:
  - Create, retrieve, update, and delete blog posts.
  - Filter posts by category, author, title, and creation date.
  - Paginated responses for better scalability.

- **Comment Management**:
  - Add comments to posts.
  - Retrieve, update, and delete comments.

- **Category Management**:
  - Categorize posts.
  - Retrieve, update, and delete categories.

- **Authentication and Authorization**:
  - Login and logout functionality.
  - Permissions to restrict access to authenticated users for sensitive operations.

---

## Requirements

The dependencies for this project are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

Key Dependencies:
- Django==5.1.4
- djangorestframework==3.14.0
- python-dotenv==1.0.0
- django-filter==23.2

---

## Project Structure

```
BlogProject/
│
├── Blog/
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates for authentication
│   │   └── Blog/
│   │       ├── login.html
│   │       └── logout.html
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App-specific routes
│   ├── views.py             # API views
│   └── tests.py             # Test cases
│
├── BlogProject/
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root routes
│   ├── wsgi.py              # WSGI configuration
│   ├── asgi.py              # ASGI configuration
│
├── db.sqlite3               # SQLite database file
├── .env                     # Environment variables
├── .gitignore               # Git ignore rules
├── requirements.txt         # Project dependencies
└── manage.py                # Django management script
```

---

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Babatunde-Odunlami/BloggingPlatformAPI/
   cd ./Blog_Capstone/BlogProject
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the root directory and add:

   ```env
   SECRET_KEY='your_secret_key'
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1, localhost
   ```

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

---

## Deployment

### Deploying to PythonAnywhere

1. **Upload Project Files**:
   - Log in to PythonAnywhere.
   - Upload the project files via the file manager or using `scp`.

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv ~/venv
   source ~/venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure the Web App**:
   - Go to the Web tab in PythonAnywhere.
   - Configure the working directory and WSGI file.
   - Set environment variables in the PythonAnywhere dashboard.

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Reload the Web App**:
   - In the Web tab, click "Reload" to deploy your app.

---

## API Endpoints

### Authentication
- `POST /api-token-auth/`: Obtain an authentication token.

### Users
- `GET /users/`: List all users.
- `POST /users/`: Create a new user.
- `GET /users/<id>/`: Retrieve a user.

### Posts
- `GET /posts/`: List all posts (supports filters and pagination).
- `POST /posts/`: Create a new post.
- `GET /posts/<id>/`: Retrieve a post.

### Comments
- `GET comments/`: List all comments.
- `POST /posts/<pk>/comments/`: Add a comment.

### Categories
- `GET /categories/`: List all categories.
- `POST /categories/`: Create a new category.

---

## Testing

Run the following command to execute test cases:

```bash
python manage.py test
```

---

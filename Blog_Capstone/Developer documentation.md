# Developer Documentation for BlogProject

## Table of Contents

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Project Structure](#project-structure)
4. [Environment Setup](#environment-setup)
5. [Running the Project Locally](#running-the-project-locally)
6. [Key Features](#key-features)
7. [Endpoints](#endpoints)
8. [Authentication and Authorization](#authentication-and-authorization)
9. [Deployment Instructions](#deployment-instructions)
10. [Code Style and Best Practices](#code-style-and-best-practices)
11. [Contribution Guidelines](#contribution-guidelines)
12. [FAQs](#faqs)

---

## Overview

**Blog Platform API** is a Django-based blogging application that allows users to create, view, update, and delete posts and comments. It includes user authentication, pagination, and category management. The project is built using Django Rest Framework (DRF) for API development.

## System Requirements

- Python 3.8 or higher
- Django 5.1
- SQLite (default database)
- Pipenv or any virtual environment manager
- Git (for version control)

## Project Structure

```plaintext
BlogProject/
    Blog/
        migrations/
        templates/Blog/
            login.html
            logout.html
        admin.py
        apps.py
        models.py
        serializers.py
        views.py
        urls.py
    BlogProject/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    static/
    manage.py
```

## Environment Setup

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/Babatunde-Odunlami/BloggingPlatformAPI/
   cd  ./Blog_Capstone/BlogProject
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables:
   ```plaintext
   SECRET_KEY='your-secret-key'
   DEBUG=True
   ```

## Running the Project Locally

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Run the development server:
   ```bash
   python manage.py runserver
   ```

3. Access the app at `https://tundebedev.pythonanywhere.com/users/`.

## Key Features

- **Authentication**: Login and logout with session-based or token-based authentication.
- **Posts and Comments**: Create, read, update, and delete blog posts and comments.
- **Pagination**: Paginated responses for large datasets.
- **Category Management**: Categorize posts.

## Endpoints

### Authentication

- `POST /api/token/`: Obtain JWT tokens.
- `POST /api/token/refresh/`: Refresh JWT tokens.

### Users

- `GET /users/`: List all users (paginated).
- `POST /users/`: Create a new user.
- `GET /users/<id>/`: Retrieve user details.
- `PUT /users/<id>/`: Update user details.
- `DELETE /users/<id>/`: Delete a user.

### Posts

- `GET /posts/`: List all posts (paginated).
- `POST /posts/`: Create a new post.
- `GET /posts/<id>/`: Retrieve post details.
- `PUT /posts/<id>/`: Update a post.
- `DELETE /posts/<id>/`: Delete a post.

### Comments

- `GET /posts/<id>/comments/`: List comments for a post.
- `POST /posts/<id>/comments/`: Add a comment to a post.
- `GET /comments/<id>/`: Retrieve a comment.
- `PUT /comments/<id>/`: Update a comment.
- `DELETE /comments/<id>/`: Delete a comment.

### Categories

- `GET /categories/`: List all categories.
- `POST /categories/`: Create a new category.
- `GET /categories/<id>/`: Retrieve category details.
- `PUT /categories/<id>/`: Update a category.
- `DELETE /categories/<id>/`: Delete a category.

## Authentication and Authorization

- Use Django Rest Framework’s authentication classes.
- Unauthenticated users can view posts and comments but cannot create, update, or delete them.
- Authenticated users can create, update, and delete their posts and comments.
- Unauthenticated site visitor can create a user account

## Deployment Instructions

### Steps

1. Push the project to a GitHub repository.
2. Create a PythonAnywhere account and set up a web app.
3. Upload the project or clone it from the repository.
4. Configure the virtual environment on PythonAnywhere.
5. Apply database migrations on the live server:
   ```bash
   python manage.py migrate
   ```
6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
7. Configure the `.env` file for production settings.
8. Restart the PythonAnywhere web app.

## Code Style and Best Practices

- Follow PEP 8 guidelines.
- Use descriptive commit messages.
- Write modular and reusable code.
- Add comments and docstrings for clarity.

## Contribution Guidelines

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add detailed description of changes"
   ```
4. Push the branch and create a pull request.

## FAQs

### 1. How do I reset the admin password?
Run the following command and follow the prompts:
```bash
python manage.py createsuperuser
```

### 2. How can I add more authentication methods?
Add the desired authentication classes in `settings.py` under `REST_FRAMEWORK`.

---

For further assistance, refer to the [official Django documentation](https://docs.djangoproject.com/).


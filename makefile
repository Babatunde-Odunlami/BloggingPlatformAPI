# Makefile for Django project tasks

# Define your virtual environment and Python interpreter (adjust as needed)
VENV := /.virtualenvs
PYTHON := $(VENV)/django_environment/bin/python3

# Django management command
DJANGO := $(PYTHON) manage.py

# Create a new Django app
startapp:
	$(DJANGO) startapp $(app_name)

# Run the Django development server on port 5000
runserver:
	$(DJANGO) runserver 5000

# Make migrations
makemigrations:
	$(DJANGO) makemigrations

# Apply migrations to the database
migrate:
	$(DJANGO) migrate

# Clean up the virtual environment
clean:
	rm -rf $(VENV)

# Install dependencies
install:
	pip install -r requirements.txt

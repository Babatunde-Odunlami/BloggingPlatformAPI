# API Authentication Setup

This document describes how to set up and test the authentication system for the API.

## Authentication Types
The API uses the following authentication methods:
TokenAuthentication is the most important, Basic and Session not needed for this task.
so add the following to the RESTFRAME in the settings.py file
        **'rest_framework.authentication.BasicAuthentication',**  # For basic auth
        **'rest_framework.authentication.SessionAuthentication',**  # For session auth
        **'rest_framework.authentication.TokenAuthentication',**  # For token-based auth

## Setting Up Token Authentication
1. Add **'rest_framework.authtoken'** to your `INSTALLED_APPS` in `settings.py`.
2. Run migrations to update the database with the command below
    **python3 manage.py migrate**
3. Tokens will be automatically created for users on registration. For existing users, generate tokens using:
    **python manage.py drf_create_token <username>**
    example python manage.py drf_create_token TundeTestuser 
    response: **Generated token 99d176d6b974f557f29a4be04d8fe96ac6158e16 for user TundeTestuser**

## Testing the Authentication
### Basic Authentication
To test using Basic Authentication, using curl

curl -X GET http://127.0.0.1:5000/login/ \
-u username:password


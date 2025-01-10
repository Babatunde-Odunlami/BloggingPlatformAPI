from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings        # remember to define AUTH_USER_MODEL in settings.py


#user model to register new users
class Username(AbstractUser):
    """user details for registeration with additional fields"""
    email = models.EmailField(unique=True, null=False, blank=False)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# Post model to allow users to make posts .
class Post(models.Model):
    """post model connected to a user"""
    title = models.CharField(max_length=80, blank=False) 
    description = models.TextField(max_length = 250)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    

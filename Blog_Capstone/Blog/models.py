from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.conf import settings


# Create your models here.

#custom user model
class CustomUser(AbstractUser):
    """additional fields for user model"""
    phone_number = models.CharField(max_length = 11, null =True, blank=True, unique=True)
    is_staff = models.BooleanField(default =False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('view users', 'can view all users')
        ]

    def __str__(self):
        return self.username

# create category model with choices
class Category(models.Model):
    """category model"""
    CATEGORY_CHOICES = [
        ('AUTOMOTIVE', 'automotive'), 
        ('ELECTRONICS', 'electronics'),
        ('FASHION', 'fashion'), 
        ('HOME', 'home'), 
        ('SPORTS', 'sports'),
        ('BOOKS', 'books'), 
        ('MUSIC', 'music'), 
        ('TOYS', 'toys'),
        ('GENERAL', 'general'), 
        ('GAMES', 'games'), 
        ('HEALTH', 'health'),
        ('LIFESTYLE', 'lifestyle'), 
        ('OTHERS', 'others'),
    ]
    name = models.CharField(
        max_length=12,
        choices=CATEGORY_CHOICES,
        default='OTHERS'
    )

    def __str__(self):
        return self.name
    
# user post model with permission
class Post(models.Model):
    """post model"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= 'posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at'] #the -created means descending order
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        permissions = [
            ('can_create', 'can create post'),
            ('can_view', 'can view post'),
            ('can_edit', 'can edit post'),
            ('can_delete', 'can delete post'),
            ('can_like', 'can like post'),
            ('can_comment', 'can comment post'),
        ]

    def __str__(self):
        return self.title
        

# comment model 
class Comment(models.Model):
    """comment model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= 'comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    text = models.TextField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.user.username} on {self.post.title}'


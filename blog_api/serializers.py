from rest_framework import serializers
from .models import Post, Username

#create serializers for models here

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_at', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
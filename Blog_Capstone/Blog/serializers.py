
from rest_framework import serializers
from .models import CustomUser, Post, Comment, Category


#create CustomUser serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

#create CustomUser serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_staff', 
                  'is_active', 'first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        return user
        
class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only = True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'created_at', 
                  'updated_at', 'likes']

    def create(self, validated_data):
        category = validated_data.pop('category')
        category, created = Category.objects.get_or_create(name = category)
        validated_data['category'] = category
        return Post.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        category = validated_data.pop('category', None)
        if category:
            category, created = Category.objects.get_or_create(name = category)
            instance.category = category
        return super().update(instance, validated_data)
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_at']
    

from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post, CustomUser, Comment, Category
from .serializers import PostSerializer, CustomUserSerializer, CommentSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.permissions import BasePermission,SAFE_METHODS

#only one approach is required
#create view to handle your endpoints logic: this approach requires manaually creating all related urls for each view
class IsAuthenticatedForWrite(BasePermission):
    """
    Custom permission to ensure that only authenticated users can
    perform any write operation (POST, PUT, DELETE).
    """

    def has_permission(self, request, view):
        # Allow unauthenticated users to perform a POST request to create a user
        if request.method == 'POST':
            return True  # No authentication required for creating a user (public access)
        # Require authentication for all other methods (PUT, GET, DELETE)
        return request.user and request.user.is_authenticated
    
#create class-based-views for CustomUser 
class CustomUserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedForWrite]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    model = CustomUser

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    model = CustomUser

#create class-based-views for Post
class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    model = Post

    def get_queryset (self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        author = self.request.query_params.get('author')
        created_at = self.request.query_params.get('created_at')
        title = self.request.query_params.get('title')

        if category:
            queryset = queryset.filter(category__name__icontains =category)
        if author:
            queryset = queryset.filter(author__username__icontains = author)
        if title:
            queryset = queryset.filter(category__name__icontains =title)
        if created_at:
            queryset = queryset.order_by('created_at')
        return queryset
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    model = Post

#create class-based-views for Comment
class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    model = Comment

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]   # Apply IsAuthenticated permission
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    model = Comment

#create class-based-views for Comment
class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    model = Category

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    model = Category


"""
# create viewset for auto views creation: this approach has the CRUD operations compressed
# each url is auto created with the router

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Post, Comment
from .serializers import CustomUserSerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]    # Apply IsAuthenticated permission

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]    # Apply IsAuthenticated permission

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]    # Apply IsAuthenticated permission

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Fetch all categories from the database
    serializer_class = CategorySerializer  # Use the CategorySerializer to transform the model data
    permission_classes = [IsAuthenticated]  # Optional: Restrict access to authenticated users

    # You can add custom logic if needed, e.g., filtering, ordering, etc.
"""
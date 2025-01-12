from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post, Username
from .serializers import PostSerializer, UserSerializer


#create views to handle your endpoints logic


#create class-based-views for User and Post
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#Username model serializers
class UserList(generics.ListCreateAPIView):
    queryset = Username.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Username.objects.all()
    serializer_class = UserSerializer



from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator #disable csrf token for curl

User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch') # necessary for my curl command to work
class RegisterUser(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = 'register.html'  # You can keep this, though it's not needed for API
    success_url = reverse_lazy('login')  # Redirect after successful registration
    
    @csrf_exempt  # Disable CSRF protection for this view
    def form_valid(self, form):
        # Hash password before saving
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Ensure the password is hashed
        user.save()
        
        # Return success message in JSON response
        return JsonResponse({'message': 'User registered successfully'}, status=201)

    @csrf_exempt  # Disable CSRF protection for this view
    def form_invalid(self, form):
        # Return error message in JSON if form is invalid
        return JsonResponse({'error': 'All fields are required.'}, status=400)
    
    @csrf_exempt  # Disable CSRF protection for this view
    def post(self, request, *args, **kwargs):
        # Parse the incoming JSON request
        data = json.loads(request.body)
        
        # Manually validate required fields
        required_fields = ['username', 'email', 'password', 'first_name', 'last_name']
        if not all(data.get(field) for field in required_fields):
            return JsonResponse({'error': 'All fields are required.'}, status=400)
        
        # Manually set the form data and validate
        form = self.get_form()
        form = form.__class__(data)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

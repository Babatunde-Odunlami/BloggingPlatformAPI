from django.urls import path 
from .views import PostList, PostDetail, UserList, UserDetail, RegisterUser
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('blog/posts/', PostList.as_view(), name='post-list'),
    path('blog/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('blog/users/', UserList.as_view(), name='user-list'),
    path('blog/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(template_name= 'login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(next_page='loginpage'), name='logout'),
    path('blog/register/', RegisterUser.as_view(), name='register'),
]




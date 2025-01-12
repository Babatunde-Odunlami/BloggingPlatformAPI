
from django.urls import path,include
from .views import CustomUserList, CustomUserDetail, PostList, PostDetail, CommentList, CommentDetail, CategoryList, CategoryDetail
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView #JWT tokens
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('users/', CustomUserList.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:pk>/comments/', CommentList.as_view(), name='comment'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('categorys/', CategoryList.as_view(), name='category-list'),
    path('categorys/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    #jwt tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('login/', include('django.contrib.auth.urls')),  # This will include the login view
]





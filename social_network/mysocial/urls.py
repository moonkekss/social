from django.urls import path
from .views import register, user_login, home, profile, create_post

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('create_post/', create_post, name='create_post'),
]
from django.urls import path
from .views import home, profile, create_post

urlpatterns = [
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('create_post/', create_post, name='create_post'),
]
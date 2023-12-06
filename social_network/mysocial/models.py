from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    email = models.EmailField(unique = True)
    
    def __str__(self) -> str:
        return self.username 
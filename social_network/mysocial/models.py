from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(AbstractUser):
    email = models.EmailField(unique = True)
    
    def __str__(self) -> str:
        return self.username 
    
class Profile(models.Model):

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="profile_photos/", 
        blank=True, 
        null=True
    )

    def __str__(self) -> str:
        return self.user.username
    
class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="post_photos/",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.user.username} - {self.created_at}'
    
@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=UserProfile)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
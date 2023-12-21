from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField( max_length=100)
    bio=models.TextField(default=' ')
    image=models.ImageField(upload_to="user_images",default="default.jpg")
    verified = models.BooleanField(default=False)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)   

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Profile(models.Model):
    #listed fields below
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=40, blank=True)
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username

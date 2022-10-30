from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=256, blank=True, default='')
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

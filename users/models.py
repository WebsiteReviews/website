from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    about_user = models.TextField(default='')
    user_country = models.CharField(max_length=128, default='')
    user_city = models.CharField(max_length=128, default='')
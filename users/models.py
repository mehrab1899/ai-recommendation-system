from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Use EmailField for better validation
    password = models.CharField(max_length=255)
    
    username = None  # Remove username field from AbstractUser

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = ['name']  # Optional,
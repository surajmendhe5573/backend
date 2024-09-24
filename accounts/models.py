# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class RoleMaster(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    role_description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.role_name

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)  # e.g., Male, Female, Other
    role = models.ForeignKey(RoleMaster, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'gender']

    def __str__(self):
        return self.email

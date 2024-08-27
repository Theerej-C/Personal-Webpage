from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AbstractMyUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255,unique=True)
    phone_number = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'  # or 'username' if you prefer
    REQUIRED_FIELDS = ['email'] 
    class Meta:
        abstract = True
class CustomUser(AbstractMyUser):
    pass    
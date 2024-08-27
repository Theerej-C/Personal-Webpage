from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password=None):
        user = self.create_user(
            username,
            email,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class AbstractMyUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    objects = MyUserManager()
    USERNAME_FIELD = 'username'  # or 'username' if you prefer
    REQUIRED_FIELDS = ['email'] 
    class Meta:
        abstract = True


class CustomUser(AbstractMyUser):
    pass    
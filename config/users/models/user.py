from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from polymorphic.models import PolymorphicModel, PolymorphicManager
from django.utils import timezone



class CustomUserManger(PolymorphicManager, BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set!')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError('Superuser must have is_staff as True!')
        if extra_fields.get("is_superuser") is not True:
            raise ValueError('Superuser must have is_superuser as True!')

        return self.create_user(username, password)

class User(PolymorphicModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'username'
    objects = CustomUserManger()

    def __str__(self):
        return self.username



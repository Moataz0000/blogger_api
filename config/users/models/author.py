from .user import User
from django.db import models


class Author(User):
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=18)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author/images', blank=True, null=True)


    def __str__(self):
        return self.username
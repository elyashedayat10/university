from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=125)
    family = models.CharField(max_length=125)
    national_code = models.CharField(max_length=10, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['name','family']

    def __str__(self):
        return f'{self.name}-{self.family}'

    @property
    def is_staff(self):
        return self.is_admin

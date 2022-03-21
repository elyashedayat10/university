from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()


class Master(models.Model):
    name = models.CharField(max_length=125)
    family = models.CharField(max_length=125)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    father_name = models.CharField(max_length=125)
    national_code = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=11)
    father_phone_number = models.CharField(max_length=11)
    mother_phone_number = models.CharField(max_length=11)
    second_number = models.CharField(max_length=11, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True, null=True, related_name='student')

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        return super(Student, self).save()

    def __str__(self):
        return self.full_name

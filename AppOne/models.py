from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STUDENT="STUDENT",'student'
        STAFF="STAFF",'staff'


    role = models.CharField(max_length=50,choices=Role.choices)

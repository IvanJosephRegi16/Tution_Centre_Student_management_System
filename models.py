from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STUDENT="STUDENT",'student'
        STAFF="STAFF",'staff'


    role = models.CharField(max_length=50,choices=Role.choices)

# your_app/models.py
from django.db import models

# AppOne/models.py
from django.db import models

class Student(models.Model):
    
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    address = models.TextField()
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    session_year = models.CharField(max_length=4)
    phone_no = models.CharField(max_length=15)  # Adjust max_length based on your needs
    guardian_name = models.CharField(max_length=100)
    guardian_phone_no = models.CharField(max_length=15)  # Adjust max_length based on your needs
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    password = models.CharField(max_length=255,null=True)  # You may want to adjust max_length based on your needs


    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # Convert self.password to a string if it's an integer
        password_str = str(self.password)

        # Create a User instance with the same email and hashed password
        user, created = User.objects.get_or_create(
            username=self.email,
            email=self.email,
            defaults={'role': User.Role.STUDENT}
        )

        # Set the password using make_password to hash it
        user.password = make_password(password_str)
        user.save()

        # Call the save method of the parent class to save the Student instance
        super().save(*args, **kwargs)
        
        
from django.db import models

class Studentdetails(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
# models.py
from django.db import models

class MyClass(models.Model):
    class_name = models.CharField(max_length=255)
    # Add more fields as needed



# models.py

from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.subject_name

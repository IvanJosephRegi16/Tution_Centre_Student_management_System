from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



from django.utils.crypto import get_random_string
import datetime

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STUDENT="STUDENT",'student'
        STAFF="STAFF",'staff'


    role = models.CharField(max_length=50,choices=Role.choices)


# models.py
from django.db import models

SESSION_CHOICES = [
    ('Morning', 'Morning (06:00 - 08:00 AM)'),
    ('Evening', 'Evening (06:00 - 08:00 PM)'),
]

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    class_name = models.ForeignKey('MyClass', on_delete=models.CASCADE, null=True)
    session = models.CharField(max_length=7, choices=SESSION_CHOICES, null=True)


    def __str__(self):
        return f"{self.subject_name} ({self.get_session_display()})"




def get_session_time(session):
    if session == 'Morning':
        return '06:00 - 08:00 AM'
    elif session == 'Evening':
        return '06:00 - 08:00 PM'
    return ''



class StudentNew(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    
    
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    class_no = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)  # Date of birth field added
    email = models.EmailField(max_length=255, unique=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name='students')
    session = models.CharField(max_length=20, choices=SESSION_CHOICES, null=True)
    session_time = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    
    
    def save(self, *args, **kwargs):
        # Update session_time based on the session
        self.session_time = get_session_time(self.session)
        super(StudentNew, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.session} ({self.session_time})"
    
    
    
    
from django.db import models

class MyClass(models.Model):
    class_name = models.CharField(max_length=255, unique=True)
    # Add any additional fields as needed

    def __str__(self):
        return self.class_name    
    
    
    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    class_name = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True)  # Foreign key to MyClass
    subjects = models.ManyToManyField(Subject, related_name='staff')  # Many-to-Many relationship with Subject

    def __str__(self):
        return self.user.username
        


class Studentdetails(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name














    
    
    


class ExcelData(models.Model):
    # Define your fields here, for example:
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)  # Email field added
    password = models.CharField(max_length=128)  # Password field added
    
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.user.password = make_password(get_random_string())
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.user.username
    
    






class Timetable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_number = models.IntegerField(default=6)
    

    def __str__(self):
        return f"Class {self.class_number} - {self.day} - {self.subject}"
    
    
    
from django.db import models
from django.contrib.auth import get_user_model

class LeaveRequest(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)  # Changed to a ForeignKey
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"{self.student.username} - {self.subject}"

    
    
class SessionTime(models.Model):
    session_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.session_name} ({self.start_time} - {self.end_time})"



class Note(models.Model):
    class_name = models.ForeignKey(MyClass, on_delete=models.CASCADE, related_name='notes')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes', null=True)
    chapter = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='class_notes/')

    def __str__(self):
        return f"{self.class_name.class_name} - {self.subject.subject_name} - {self.chapter} - {self.topic}"
    
    
    
    
    
    
class StaffLeaveRequest(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='leave_requests')
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='leave_requests')
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    
    @property
    def staff_class_name(self):
        return self.staff.class_name.class_name if self.staff.class_name else "No Class Assigned"

    def __str__(self):
        return f"{self.staff.user.username} - {self.subject.subject_name} - {self.status}"
    
    
    
    
    
class Attendance(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    date = models.DateField()
    first_hour = models.BooleanField(default=False)
    second_hour = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - Date: {self.date} - 1st Hour: {'Present' if self.first_hour else 'Absent'} - 2nd Hour: {'Present' if self.second_hour else 'Absent'}"


# models.py

from django.db import models
from django.conf import settings

class GoogleMeetLink(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=255)






# models.py
from django.db import models

class Marks(models.Model):
    student = models.ForeignKey('StudentNew', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    month = models.CharField(max_length=9, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December'),], blank=True)  # Add your month choices here
    total_marks = models.IntegerField(default=50)
    scored_marks = models.IntegerField()
    grade = models.CharField(max_length=2, blank=True)
    percentage = models.FloatField(blank=True)

    def save(self, *args, **kwargs):
        # Calculate the percentage and assign a grade
        self.percentage = (self.scored_marks / self.total_marks) * 100 if self.total_marks else 0

        # Assign grade based on scored marks
        if self.scored_marks >= 45:
            self.grade = 'S'
        elif self.scored_marks >= 40:
            self.grade = 'A+'
        elif self.scored_marks >= 35:
            self.grade = 'A'
        elif self.scored_marks >= 30:
            self.grade = 'B+'
        elif self.scored_marks >= 25:
            self.grade = 'B'
        elif self.scored_marks >= 20:
            self.grade = 'C'
        else:
            self.grade = 'F'

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"{self.student.user.username} - {self.subject.subject_name} - {self.month} - Grade: {self.grade}"



# models.py
class StudentFeedback(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    feedback = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student.user.username} on {self.staff.user.username}"



from django.db import models

class FeedbackQuestion(models.Model):
    question_text = models.CharField(max_length=255)  # Define the question_text attribute

    def __str__(self):
        return self.question_text


class FeedbackStudent(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    weak_feedback = models.TextField()
    strong_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student.username} on {self.subject.subject_name}"

class SelectedOption(models.Model):
    feedback_student = models.ForeignKey(FeedbackStudent, on_delete=models.CASCADE)
    feedback_question = models.ForeignKey(FeedbackQuestion, on_delete=models.CASCADE)
    option = models.CharField(max_length=20)  # Store the selected option

    def __str__(self):
        return f"Feedback: {self.feedback_student}, Question: {self.feedback_question}, Option: {self.option}"
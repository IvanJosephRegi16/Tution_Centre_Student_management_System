from calendar import month
import datetime
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate ,login as auth_login,logout,get_user_model, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.shortcuts import render
from mysqlx import Session
from .models import SESSION_CHOICES, Marks, MyClass, StaffLeaveRequest, StudentFeedback, User, Subject, Timetable , Studentdetails, StudentNew
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
import random
import string
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
import pandas as pd
from django.views import View
from django.core.mail import send_mail
from .forms import TimetableForm
from django.contrib.auth.hashers import make_password
from django.conf import settings

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Timetable
from .forms import ClassForm
from .models import MyClass, Subject
from .forms import SubjectForm
from django.contrib.auth import login

from .models import User, StudentNew, MyClass

from AppOne.models import SessionTime
from .models import StudentNew, Staff


from .forms import NoteForm
from .models import Note
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required

from .forms import FeedbackForm
from .models import FeedbackQuestion







# Create your views here.

def home(request):
    return render (request,"index.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def myhome(request):
    return render (request,"index2.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url='login')
def student_view(request):
    context = {'username': request.user.username}
    return render(request, "student.html",context)


def add_subject(request):
    return render(request,"add_subject.html")

def view_subjects(request):
    return render(request,"view_subjects.html")



def course(request):
    return render(request,"course.html")



def detail(request):
    return render(request,"detail.html",)

def feature(request):
    return render(request,"feature.html",)

def team(request):
    return render(request,"team.html",)

def testimonial(request):
    return render(request,"testimonial.html",)

def contact(request):
    return render(request,"contact.html",)
# this is users signup 



def signup(request):
   if request.method=="POST":
            first_name=request.POST['fname']
            last_name=request.POST['lname']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
        
            confirm_password=request.POST['confirm_password']
            if password!=confirm_password:
                    messages.warning(request,"password is not matching")
                    return render(request,'signup.html')
            try:
                      if User.objects.get(username=username):
                             messages.warning(request,"Username is already taken")
                             return render(request,'signup.html')
                      if User.objects.get(email=email):
                             messages.warning(request,"email ID is already taken")
                             return render(request,'signup.html')
            except Exception as identifiers:
                      pass
           # print(first_name,last_name,username,email,password)
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,role='STUDENT')
              #make the user inactive user.is_active=False
            user.save()
            messages.success(request,"Registration Successfull..!")
            
            # return HttpResponse("Registration Successfull ")    
            
            
   return render(request,'signup.html')
            
            

def user_login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('generate_user')
            
            elif user.role == User.Role.STUDENT:
                return redirect('student')
            elif user.role == User.Role.STAFF:
                return redirect('staffpage')
            else:
                return redirect('home')
        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')


def logoutPage(request):
    # Clear the session on logout
    logout(request)
    
    # Redirect to the login page
    return redirect('login')

def StaffReg(request):
    return render (request,"thrpreg.html")


def permission_denied(request):
    return render(request, 'permission_denied.html')


# oct 1 updations TherapHome


def StaffpHome(request):
    return render(request,"demo.html")

# views.py


def generate_password():
    # Generate a random password
    length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if the email is unique
        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return redirect('generate_user')

        # Generate a password
        password = generate_password()

        # Create the user
        user = get_user_model().objects.create_user(username=email, email=email, password=password)

        # Send email to the user
        subject = 'Your Account Information'
        message = f'Your account has been created.\n\nEmail: {email}\nPassword: {password}'
        from_email = 'admin@example.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, 'User created successfully and email sent.')
        return redirect('generate_user')

    # Fetch counts for students and staff
    student_count = StudentNew.objects.count()  # Use the correct model for students
    staff_count = Staff.objects.count()         # Use the correct model for staff

    # Pass these counts to the context
    context = {'student_count': student_count, 'staff_count': staff_count}
    return render(request, 'generate_user.html', context)

# views.py

User = get_user_model()


def slogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('myhome')
            
            elif user.role == User.Role.STUDENT:
                return redirect('student_dashboard')
            
            else:
                return redirect('home')
        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid email or password')

    return render(request, 'slogin.html')




def all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})



def submit_student_details(request):
    if request.method == 'POST':
        # Retrieve data from the submitted form
        username = request.POST.get('username')
        email = request.POST.get('email')
      

        # Retrieve the user instance and link it to the Student model
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        course = request.POST.get('course')
        gender = request.POST.get('gender')
        phone_no = request.POST.get('phone_no')
        guardian_name = request.POST.get('guardian_name')
        guardian_phone_no = request.POST.get('guardian_phone_no')
        session_year = request.POST.get('session_year')
        profile_pic = request.FILES.get('profile_pic')

        # Create a new Student instance and save it to the database
        student = StudentNew(
            
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=address,
            course=course,
            gender=gender,
            phone_no=phone_no,
            guardian_name=guardian_name,
            guardian_phone_no=guardian_phone_no,
            session_year=session_year,
            profile_pic=profile_pic
        )
        student.save()

        # Redirect to a success page or any other page you want
        return HttpResponse("Successfully registered!")

    return HttpResponse("Invalid request method.")




def view_student_details(request):
    students = StudentNew.objects.all()
    return render(request, 'view_student_details.html', {'students': students})

def leave_application(request):
    if request.method == 'POST':
        # Retrieve data from the leave application form
        reason = request.POST.get('reason')

        # Process the leave application logic (save to database, send notifications, etc.)
        # ...

        return HttpResponse("Leave application submitted successfully!")
    else:
        return render(request, 'leave_application.html')
    


# Inside submit_leave_application view



def send_email_to_admins(reason, student_email):
    try:
        # Specify the subject, message, sender (student's email), and recipient (admin email address)
        subject = 'Leave Application Submitted'
        message = f'A leave application has been submitted with the following reason:\n\n{reason}'
        
        from_email = student_email  # Use the student's email as the sender
        recipient_list = ['fedrickdenny@gmail.com']  # Add your admin email addresses

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

    except Exception as e:
        # Handle email sending failure (log the error, display a message to the user, etc.)
        print(f"Failed to send email: {e}")

def get_student_email(user):
    try:
        # Assuming the user object has a related Student model and the email is stored in the Student model
        return user.student.email  # Adjust this based on your actual model structure

    except AttributeError:
        # Handle the case where the user doesn't have a related student or the email is not available
        return None





def add_student(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        class_name = request.POST.get('class_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        # Create a new student
        student = Studentdetails(name=name, class_name=class_name, address=address, phone_number=phone_number)
        student.save()

        return redirect('home')  # Redirect to the home page or any other page you want
    else:
        return render(request, 'add_student.html')
# views.py





def class_details(request, class_number):
    students = StudentNew.objects.filter(course=class_number)
    context = {'students': students, 'class_no': class_number}
    return render(request, 'class_details.html', context)





def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the desired page after saving
            return redirect('generate_user')
        else:
            # If the form is not valid, 'classes' needs to be included again before rendering
            classes = MyClass.objects.all()
            return render(request, 'add_subject.html', {'form': form, 'classes': classes})
    else:
        form = SubjectForm()
        classes = MyClass.objects.all()  # Get all class objects from the database
    # The context with 'classes' is outside the 'if' to ensure it's always available
    return render(request, 'add_subject.html', {'form': form, 'classes': classes})


def view_subjects(request):
    # Create a dictionary to hold the class names and their subjects
    class_subjects = {}

    # Retrieve all classes and their related subjects
    classes = MyClass.objects.all().prefetch_related('subject_set')

    for cls in classes:
        # Use the class name as the key and the list of subjects as the value
        class_subjects[cls.class_name] = cls.subject_set.all()

    return render(request, 'view_subjects.html', {'class_subjects': class_subjects})




def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')  # Redirect to the view_subjects page after editing
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'edit_subject.html', {'form': form})




def delete_subject(request, subject_id):
    if request.method == 'POST':  # Ensure this is a POST request
        subject = get_object_or_404(Subject, id=subject_id)
        subject.delete()
        return HttpResponseRedirect(reverse('view_subjects'))  # Redirect to the subjects list

    




def update_students(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file, engine='openpyxl')

        for index, row in df.iterrows():
            student, created = StudentNew.objects.update_or_create(
                email=row['email'],
                defaults={
                    'first_name': row['first_name'],
                    'course': row['course'],
                    'session_year': row['session_year'],
                    'password': row['password'],
                }
            )

        return redirect('register_student')  # Redirect to a success page or another view

    return render(request, 'update_students.html')


























def send_email_to_admins(reason, student_email):
    subject = 'Leave Application Submitted'
    message = f'A leave application has been submitted with the following reason:\n\n{reason}'
    from_email = student_email  # Use the student's email as the sender
    recipient_list = ['admin@example.com']  # Add your admin email addresses

    # Send the email
    send_mail(subject, message, from_email, recipient_list)




from django.shortcuts import render, redirect

from .forms import TimetableForm

from django.shortcuts import render, redirect
from .models import Timetable
from .forms import TimetableForm

def manage_timetable(request):
    timetables = Timetable.objects.select_related('subject').all()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    class_numbers = range(6, 11)  # Classes 6 to 10

    class_timetables = {}
    for class_number in class_numbers:
        class_name = f'Class {class_number}'
        class_timetables[class_name] = {day: [] for day in days}

        for day in days:
            periods = timetables.filter(class_number=class_number, day=day)
            class_timetables[class_name][day] = [(period.id, period.subject.subject_name) for period in periods]

    context = {
        'class_timetables': class_timetables,
        'days': days,
    }
    return render(request, 'manage_timetable.html', context)







def add_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_timetable')
    else:
        form = TimetableForm()
    return render(request, 'add_timetable.html', {'form': form})







def delete_timetable_entry(request, timetable_id):
    if request.method == 'POST':
        timetable_entry = get_object_or_404(Timetable, id=timetable_id)
        timetable_entry.delete()
        return redirect('manage_timetable')
    else:
        # This else statement is not strictly necessary because this view should only ever be POSTed to.
        return redirect('manage_timetable')



User = get_user_model()
def register_student(request):
    if request.method == 'POST':
        # Extracting form data
        username = request.POST['User_name']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_no = request.POST['phone_no']
        class_no = request.POST['course']
        selected_subject_ids = request.POST.getlist('subjects') 
        session = request.POST['session']
        gender = request.POST['gender']
        dob = request.POST['dob']
        
        # Convert dob to date object
        try:
            dob = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
        except ValueError as e:
            messages.error(request, f'Invalid date format: {e}')
            return render(request, 'index2.html', {'session_choices': SESSION_CHOICES})

        # Create User and StudentNew instances
        try:
            # Check if a user with this username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'index2.html', {'session_choices': SESSION_CHOICES})

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                role=User.Role.STUDENT
            )
        except Exception as e:
            messages.error(request, f'Error creating user: {e}')
            return render(request, 'index2.html', {'session_choices': SESSION_CHOICES})

        # Since user is now guaranteed to be defined, we can create StudentNew
        student = StudentNew(
            user=user,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_no,
            class_no=class_no,
            gender=gender,
            date_of_birth=dob,
            email=email,  # Save the email to the student
            session=session  # Save the session to the student
        )
        student.save()
        # Set the subjects for the student
        student.subjects.set(Subject.objects.filter(id__in=selected_subject_ids))

        # Send email with account details
        subject = 'Your Account Details'
        message = f'Username: {username}\nPassword: {password}\nEmail: {email}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        # Display success message and log the user in
        messages.success(request, 'Registration successful. Account details have been sent to your email.')
        login(request, user)
        return redirect('generate_user')

    else:
        # This is the GET request to display the form
        classes = MyClass.objects.all()
        subjects = Subject.objects.all()
        context = {
            'classes': classes,
            'subjects': subjects,
            'session_choices': SESSION_CHOICES,
        }
        return render(request, 'index2.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User, Staff

def create_staff(request):
    if request.method == 'POST':
        # Manually get form data
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        class_name_id = request.POST.get('class_name')
        selected_subject_ids = request.POST.getlist('subjects')
        
        
        
        class_name_instance = MyClass.objects.get(id=class_name_id)
        subject_instances = Subject.objects.filter(id__in=selected_subject_ids)

        
        # Create User instance
        user = User(
            username=username, 
            first_name=first_name, 
            last_name=last_name,
            email=email,
            password=make_password(password),  # Hash the password
            role=User.Role.STAFF
        )
        user.save()

        # Create Staff instance
        staff = Staff(
            user=user,  
            first_name=first_name, 
            last_name=last_name,
            phone_number=phone_number,
            gender=gender,
            date_of_birth=date_of_birth,
            class_name=class_name_instance
            
        )
        staff.save()
        
        staff.subjects.set(subject_instances)

        # Redirect to a new URL
        return redirect('generate_user')
    else:
        classes = MyClass.objects.all()
        subjects = Subject.objects.all()
        return render(request, 'staff_form.html', {'classes': classes, 'subjects': subjects})
        


from .models import Staff, StaffLeaveRequest
from .models import Attendance
# ... other imports ...

@login_required(login_url='login')
def staff_page(request):
    staff_member = get_object_or_404(Staff, user=request.user)

    # Retrieve the class and subjects for this staff member
    class_name = staff_member.class_name.class_name if staff_member.class_name else "No Class Assigned"
    subject_names = [subject.subject_name for subject in staff_member.subjects.all()]

    # Get staff's leave requests
    leave_requests = StaffLeaveRequest.objects.filter(staff=staff_member).order_by('-date')
    attendance_records = Attendance.objects.filter(subject__in=staff_member.subjects.all()).order_by('-date')

    context = {
        'username': request.user.username,
        'welcome_message': f'Welcome to the Staff Page, {request.user.first_name} {request.user.last_name}!',
        'class_name': class_name,
        'subject_names': subject_names,
        'leave_requests': leave_requests,  # Add the leave requests to the context
        'attendance_records': attendance_records,
    }
    return render(request, 'staff_page.html', context)


    


import openpyxl
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import ExcelUploadForm
from .models import Staff
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings

# Function to handle Excel date format and convert it to a date object
def parse_date(dob_str):
    if isinstance(dob_str, datetime.datetime):
        # If the value is already a datetime object, just return the date part
        return dob_str.date()
    elif isinstance(dob_str, str):
        try:
            # If the value is a string, parse it to a date object
            return datetime.datetime.strptime(dob_str, '%m/%d/%Y').date()
        except ValueError as e:
            # Log the error if the date format is incorrect
            return None
    else:
        return None

def upload_excel(request):
    User = get_user_model()  # Make sure to use your custom user model if you have one
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active
            
            for row in sheet.iter_rows(min_row=2, values_only=True):
                username, first_name, last_name, email, phone_number, gender, dob_str = row
                dob = parse_date(dob_str)
                if dob is None:
                    messages.error(request, f"Invalid date format for user {username}.")
                    continue
                
                if User.objects.filter(username=username).exists():
                    messages.error(request, f"User {username} already exists.")
                    continue
                
                random_password = get_random_string(length=10)
                try:
                    user = User.objects.create(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=make_password(random_password)
                    )
                    Staff.objects.create(
                        user=user,
                        first_name=first_name,
                        last_name=last_name,
                        phone_number=phone_number,
                        gender=gender,
                        date_of_birth=dob
                    )
                    
                    # Sending email to the user with account details
                    send_mail(
                        subject='Your Account Information',
                        message=f'Hello {first_name}, your account has been created. Your username is {username} and your password is {random_password}.',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email],
                        fail_silently=False,
                    )
                except Exception as e:
                    messages.error(request, f"An error occurred while creating the user {username}: {str(e)}")
                    continue
                
            messages.success(request, "Excel file processed and emails sent successfully.")
            return redirect('generate_user')  # Replace with the actual URL name
        else:
            messages.error(request, "There was an issue with the form.")
    else:
        form = ExcelUploadForm()
    return render(request, 'create_staff', {'form': form})



# views.py

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class added successfully.')  # Add a success message
            form = ClassForm()  # Reset the form or redirect as needed
            return redirect('generate_user')  # Optionally redirect to the same page to clear POST data
    else:
        form = ClassForm()
    return render(request, 'add_class.html', {'form': form})



def view_class(request):
    classes = MyClass.objects.all()  # Retrieve all MyClass objects
    return render(request, 'view_class.html', {'classes': classes})


def myclass_detail(request, class_id):
    class_instance = get_object_or_404(MyClass, id=class_id)
    # Retrieve students for the morning session
    morning_students = StudentNew.objects.filter(class_no=class_instance.id, session='Morning').order_by('first_name', 'last_name')
    # Retrieve students for the evening session
    evening_students = StudentNew.objects.filter(class_no=class_instance.id, session='Evening').order_by('first_name', 'last_name')
    
    context = {
        'class': class_instance,
        'morning_students': morning_students,
        'evening_students': evening_students,
    }
    
    return render(request, 'myclass_detail.html', context)




from django.http import JsonResponse

def get_subjects_for_class(request, class_id):
    subjects = Subject.objects.filter(class_id=class_id).values('id', 'name')
    return JsonResponse(list(subjects), safe=False)


from .models import SessionTime

def session_view(request):
    sessions = Session.objects.all()  # Fetch all session objects
    return render(request, 'session.html', {'sessions': sessions})




from django.shortcuts import render, get_object_or_404
from .models import StudentNew, Subject, MyClass

def student_subjects(request):
    student = get_object_or_404(StudentNew, user=request.user)
    enrolled_subjects = student.subjects.all()
    
    # Assuming 'class_no' is a field in your StudentNew model that relates to MyClass model
    class_name = MyClass.objects.get(id=student.class_no).class_name if student.class_no else "Not Assigned"
    session = student.session if student.session else "Not Assigned"

    context = {
        'username': request.user.username,
        'enrolled_subjects': enrolled_subjects,
        'class_name': class_name,
        'session': session,
    }
    
    return render(request, "student_subjects.html", context)






from django.shortcuts import render
from .models import StudentNew, Timetable

from django.shortcuts import render, get_object_or_404

# Your import statements...
from .models import StudentNew, Timetable

from django.shortcuts import render
from .models import StudentNew, Timetable

from django.shortcuts import render, get_object_or_404
from .models import StudentNew, Timetable, MyClass
from datetime import time

def student_timetable(request):
    # Ensure the student is logged in
    student = get_object_or_404(StudentNew, user=request.user)

    # Get the subjects for the student
    subjects = student.subjects.all()

    # Now get the timetable entries for those subjects
    # It assumes that there is a day field in your Timetable model
    timetable_entries = Timetable.objects.filter(subject__in=subjects).order_by('day', 'start_time')

    # Organize the timetable entries by day
    timetable_by_day = {}
    for entry in timetable_entries:
        entry_day = entry.day
        if entry_day not in timetable_by_day:
            timetable_by_day[entry_day] = []
        timetable_by_day[entry_day].append(entry)

    context = {
        'timetable_by_day': timetable_by_day,
    }

    return render(request, 'student_timetable.html', context)





from django.shortcuts import render
from .models import Timetable, StudentNew

@login_required
def view_student_timetable(request):
    student = get_object_or_404(StudentNew, user=request.user)
    timetable_entries = Timetable.objects.filter(subject__in=student.subjects.all()).order_by('day')
    
    # Including student's registered session time
    for entry in timetable_entries:
        entry.registered_time = student.session_time  # Assuming session_time is a field in StudentNew

    context = {
        'timetable_entries': timetable_entries,
    }
    
    return render(request, 'view_student_timetable.html', context)


from django.http import JsonResponse

def get_subjects_for_class(request, class_id):
    subjects = Subject.objects.filter(class_no=class_id).values('id', 'subject_name')
    return JsonResponse(list(subjects), safe=False)






    
    
@login_required(login_url='login')
def student_view(request):
    student = get_object_or_404(StudentNew, user=request.user)
    enrolled_subjects = student.subjects.all()
    leave_requests = LeaveRequest.objects.filter(student=student).order_by('-date')

    # Fetch notes that match the student's subjects and class
    notes = Note.objects.filter(
        subject__in=enrolled_subjects,
        class_name=student.class_no  # assuming class_no stores MyClass instance
    ).select_related('subject').order_by('subject_id', 'chapter')  # Order by subject_id then chapter

    context = {
        'username': request.user.username,
        'enrolled_subjects': enrolled_subjects,
        'leave_requests': leave_requests,
        'notes': notes,  # The fetched notes are added to the context
    }
    
    return render(request, "student.html", context)





from django.shortcuts import render, redirect
from .models import LeaveRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def submit_leave_request(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        subject_id = request.POST.get('subject')
        reason = request.POST.get('reason')
        
        # Assuming that the StudentNew model is related to the User model
        # with a OneToOneField called 'user'.
        student_profile = request.user.studentnew  # This is the User instance

        subject = Subject.objects.get(id=subject_id)
        
        # Make sure to assign the User instance to the 'student' field
        LeaveRequest.objects.create(
            student=student_profile,  # Use the User instance here
            date=date,
            subject=subject,
            reason=reason
        )
        messages.success(request, 'Leave request submitted successfully.')
        return redirect('student')  # Make sure this is the correct redirect

    # If the method is not POST, render the form page again
    return render(request, 'student.html')


@login_required
def view_leave_requests(request):
    leave_requests = LeaveRequest.objects.all().select_related('student__user', 'subject')
    return render(request, 'view_leave_requests.html', {'leave_requests': leave_requests})


@login_required
def approve_leave_request(request, leave_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    leave_request.status = 'approved'
    leave_request.save()
    return redirect('view_leave_requests')

@login_required
def reject_leave_request(request, leave_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    leave_request.status = 'rejected'
    leave_request.save()
    return redirect('view_leave_requests')


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def get_subjects_for_day(request):
    day = request.GET.get('day')
    student = request.user.studentnew
    # Assuming there is a 'day' field in your 'Timetable' model that stores the weekday name
    timetables = Timetable.objects.filter(day=day, subject__students=student)
    
    subjects = [{
        'id': timetable.subject.id,
        'subject_name': timetable.subject.subject_name
    } for timetable in timetables]

    return JsonResponse({'subjects': subjects})





def staff_view(request):
    staff_members = User.objects.filter(role=User.Role.STAFF)
    return render(request, 'staff_view.html', {'staff_members': staff_members})







@login_required(login_url='login')
def upload_notes(request):
    try:
        # Attempt to retrieve the staff member instance
        staff_member = Staff.objects.get(user=request.user)
        # Proceed with your original logic
        registered_class = staff_member.class_name
        registered_subject = staff_member.subjects.first()  # Assuming at least one subject is registered

        if request.method == 'POST':
            form = NoteForm(request.POST, request.FILES)
            if form.is_valid():
                note = form.save(commit=False)
                note.class_name = registered_class
                note.subject = registered_subject
                note.save()
                messages.success(request, "Notes uploaded successfully!")
                return redirect('staffpage')  # Use the name of the staff page URL
        else:
            form = NoteForm(initial={'class_name': registered_class, 'subject': registered_subject})

        return render(request, 'upload_notes.html', {
            'form': form,
            'class_name': registered_class,
            'subject': registered_subject,
        })
    except Staff.DoesNotExist:
        # If the staff member does not exist, redirect to an error page or display an error message
        messages.error(request, "You are not registered as staff.")
        return redirect('staffpage')  # Use the name of your error page URL

@login_required(login_url='login')
def subject_notes_view(request, subject_id):
    # Retrieve the subject based on the passed in ID
    subject = get_object_or_404(Subject, id=subject_id)
    
    # Fetch notes for this subject
    notes = Note.objects.filter(subject=subject).order_by('chapter')
    
    context = {
        'subject': subject,
        'notes': notes,
    }
    
    return render(request, "subject_notes.html", context)


from django.utils import timezone


@login_required
def staff_leave_application(request):
    staff_member = get_object_or_404(Staff, user=request.user)
    taught_subjects = staff_member.subjects.all()
    class_name = staff_member.class_name if staff_member.class_name else None

    # Get the distinct days that the staff member has classes
    if class_name:
        available_days = Timetable.objects.filter(
            subject__in=taught_subjects, 
            subject__class_name=class_name
        ).values_list('day', flat=True).distinct()
    else:
        available_days = []

    class_names = {subject.class_name.class_name for subject in taught_subjects if subject.class_name}
    today = timezone.localdate()

    return render(request, 'staff_leave_application.html', {
        'taught_subjects': taught_subjects,
        'class_names': class_names,
        'today': today,
        'available_days': available_days
    })

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Staff, Subject, StaffLeaveRequest, Timetable
from django.contrib.auth.decorators import login_required
from django.http import Http404
import datetime

@login_required
def submit_staff_leave(request):
    if request.method == 'POST':
        staff_member = get_object_or_404(Staff, user=request.user)
        date = request.POST.get('date')
        subject_id = request.POST.get('subject')  # This will get the subject ID from the form
        reason = request.POST.get('reason')

        # Convert the date string to a datetime object
        try:
            leave_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Invalid date format.')
            return redirect('staff_leave_application')

        # Validate that the subject exists
        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            messages.error(request, "The subject does not exist.")
            return redirect('staff_leave_application')

        # Create the StaffLeaveRequest
        leave_request = StaffLeaveRequest(
            staff=staff_member,
            date=leave_date,
            subject=subject,
            reason=reason
        )
        leave_request.save()
        messages.success(request, 'Your leave request has been submitted successfully.')
        return redirect('staffpage')  # Redirect to the staff page after successful submission

    # If GET request or any other method, just render the form
    return render(request, 'staff_leave_application.html')



from django.shortcuts import render, get_object_or_404
from .models import Staff, Timetable

@login_required
def view_staff_timetable(request):
    staff_member = get_object_or_404(Staff, user=request.user)
    subjects_taught = staff_member.subjects.all()

    # Filter timetable entries by subjects taught by the staff member
    timetable_entries = Timetable.objects.filter(subject__in=subjects_taught).order_by('day')

    context = {
        'timetable_entries': timetable_entries,
    }

    return render(request, 'view_staff_timetable.html', context)



@login_required
def view_notes(request):
    staff_member = get_object_or_404(Staff, user=request.user)
    # Fetch only notes uploaded by this staff member
    notes_uploaded_by_staff = Note.objects.filter(subject__staff=staff_member)
    return render(request, 'view_notes.html', {'notes': notes_uploaded_by_staff})




@login_required
def edit_note(request, note_id):
    staff_member = get_object_or_404(Staff, user=request.user)
    note = get_object_or_404(Note, id=note_id, subject__staff=staff_member)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Notes updated successfully!")
            return redirect('view_notes')
    else:
        form = NoteForm(instance=note)
    
    return render(request, 'edit_note.html', {'form': form})



@login_required
def manage_staff_leave_requests(request):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('generate_user.html')

    leave_requests = StaffLeaveRequest.objects.all().order_by('-date')

    return render(request, 'manage_staff_leave_requests.html', {'leave_requests': leave_requests})



from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import StaffLeaveRequest
from django.contrib import messages

@login_required
def approve_leave_request(request, leave_id):
    leave_request = get_object_or_404(StaffLeaveRequest, id=leave_id)
    leave_request.status = 'approved'
    leave_request.save()
    messages.success(request, 'Leave request approved.')
    return redirect('manage_staff_leave_requests')

@login_required
def reject_leave_request(request, leave_id):
    leave_request = get_object_or_404(StaffLeaveRequest, id=leave_id)
    leave_request.status = 'rejected'
    leave_request.save()
    messages.success(request, 'Leave request rejected.')
    return redirect('manage_staff_leave_requests')



from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Attendance, StudentNew, Staff, Timetable
from django.utils.dateparse import parse_date

@login_required(login_url='login')
def attendance_view(request):
    context = {
        'timetables': [],
        'students': [],
        'selected_date': None,
        'no_classes': True,  # Assume no classes until found otherwise
        'message': ''
    }

    staff_member = get_object_or_404(Staff, user=request.user)

    if request.method == 'POST':
        selected_date_str = request.POST.get('date')
        selected_date = parse_date(selected_date_str)
        context['selected_date'] = selected_date_str

        if selected_date:
            day_name = selected_date.strftime('%A')
            timetables = Timetable.objects.filter(day=day_name, subject__staff=staff_member)

            if timetables:
                context['no_classes'] = False
                context['timetables'] = timetables

                if 'mark_attendance' in request.POST:
                    for timetable in timetables:
                        students = StudentNew.objects.filter(subjects=timetable.subject)
                        for student in students:
                            for period in ['first_hour', 'second_hour']:
                                checkbox_value = request.POST.get(f"{period}_{student.pk}") == 'on'  # Changed from student.id to student.pk
                                Attendance.objects.update_or_create(
                                    student=student,
                                    date=selected_date,
                                    subject=timetable.subject,
                                    defaults={
                                        period: checkbox_value
                                    }
                                )
                    messages.success(request, "Attendance marked successfully.")
                    return redirect('attendance_view')
            else:
                context['message'] = "You have no classes on this day."
        else:
            context['message'] = "Please select a date."

    # When the request is GET, just render the form with the context.
    return render(request, 'attendance.html', context)









from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance, StudentNew, Timetable, Staff
from datetime import datetime
from django.contrib import messages

@login_required(login_url='login')
def mark_attendance(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Make sure you are filtering for the correct subjects
        staff_member = get_object_or_404(Staff, user=request.user)
        timetables = Timetable.objects.filter(subject__in=staff_member.subjects.all(), date=date)
        if not timetables:
            messages.error(request, "You have no classes on this date.")
            return redirect('attendance')  # Redirect to a view that handles this case

        # Iterate over each student in the timetable
        for timetable in timetables:
            students = StudentNew.objects.filter(subjects=timetable.subject)
            for student in students:
                first_hour_key = f'first_hour_{student.pk}'
                second_hour_key = f'second_hour_{student.pk}'
                first_hour = request.POST.get(first_hour_key, False)
                second_hour = request.POST.get(second_hour_key, False)

                # Convert checkbox "on" to True
                first_hour = True if first_hour == 'on' else False
                second_hour = True if second_hour == 'on' else False

                attendance, created = Attendance.objects.get_or_create(
                    student=student,
                    date=date,
                    defaults={
                        'first_hour': first_hour,
                        'second_hour': second_hour
                    }
                )

                if not created:
                    # If the record exists, update it
                    attendance.first_hour = first_hour
                    attendance.second_hour = second_hour
                    attendance.save()

        messages.success(request, "Attendance marked successfully.")
        return redirect('view_attendance')

    # If it's a GET request, show the form or attendance records
    return render(request, 'attendance.html')









from django.utils.dateparse import parse_date

@login_required
def view_attendance(request):
    # Assume 'request.user' is the staff member logged in
    staff_member = get_object_or_404(Staff, user=request.user)
    
    # Get only the students that are registered to the subjects the staff member is teaching
    subjects_taught_by_staff = staff_member.subjects.all()
    students = StudentNew.objects.filter(subjects__in=subjects_taught_by_staff).distinct()

    # Initialize the variables for selected date and student
    selected_date = request.GET.get('date', None)
    selected_student_id = request.GET.get('student_id', None)
    
    # Filter the attendance records
    attendance_records = Attendance.objects.none()  # Start with an empty queryset
    if selected_date:
        # If a date is selected, filter by that date
        attendance_records = Attendance.objects.filter(date=selected_date)
        if selected_student_id and selected_student_id != 'all':
            # Further filter by selected student if one is selected
            attendance_records = attendance_records.filter(student__id=selected_student_id)
        elif not selected_student_id or selected_student_id == 'all':
            # If no student is selected or 'All' is selected, show all students for the staff member
            attendance_records = attendance_records.filter(student__in=students)
    else:
        # If no date is selected, prompt the staff to select a date
        messages.info(request, 'Please select a date to view attendance records.')

    # Build the context
    context = {
        'attendance_records': attendance_records,
        'students': students,
        'selected_date': selected_date,
        'selected_student_id': selected_student_id,
    }
    return render(request, 'view_attendance.html', context)


from django.shortcuts import render
from .models import Attendance, StudentNew
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def student_attendance_view(request):
    student = get_object_or_404(StudentNew, user=request.user)
    attendance_records = Attendance.objects.filter(student=student).order_by('-date')

    return render(request, 'student_attendance.html', {
        'attendance_records': attendance_records
    })


# In your views.py
from django.shortcuts import render
from .models import Staff, StudentNew, Subject
from .models import GoogleMeetLink

@login_required
def online_class(request):
    if request.method == 'POST':
        link = request.POST.get('meet_link')
        GoogleMeetLink.objects.update_or_create(staff=request.user, defaults={'link': link})

    context = {}
    return render(request, 'online_class.html', context)


from django.shortcuts import render, get_object_or_404
from .models import StudentNew

@login_required
def student_online_class(request):
    # Ensure that the user is a student and has a related StudentNew record.
    student = get_object_or_404(StudentNew, user=request.user)
    
    # Fetch the subjects for the logged-in student
    subjects = student.subjects.all().order_by('subject_name')
    
    # Now create a list of subject names to pass to the template
    subject_names = [subject.subject_name for subject in subjects]
    
    return render(request, 'student_online_class.html', {'subjects': subjects, 'subject_names': subject_names})



from django.shortcuts import render, get_object_or_404
from .models import Subject, GoogleMeetLink, StudentNew
from django.contrib.auth.decorators import login_required

@login_required
def view_meet_link(request, subject_id):
    # Make sure the student is enrolled in the subject.
    student = get_object_or_404(StudentNew, user=request.user)
    subject = get_object_or_404(Subject, id=subject_id, students=student)

    # Get all GoogleMeetLink objects for the subject.
    meet_links = GoogleMeetLink.objects.filter(subject=subject)

    context = {
        'subject': subject,
        'meet_links': meet_links
    }
    return render(request, 'view_meet_link.html', context)


# AppOne/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Staff, Subject, StudentNew

@login_required(login_url='login')
def view_marks(request):
    staff_member = request.user.staff  # Assuming the User model has a 'staff' attribute
    subject = staff_member.subjects.first()  # Get the first subject taught by the staff member
    students = StudentNew.objects.filter(subjects=subject).distinct()

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    return render(request, 'marks.html', {
        'students': students,
        'subject': subject,  # Pass the single subject to the template
        'months': months,
    })




# You'll also need a view for handling the submission of marks



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Staff, Subject, StudentNew, Marks
from django.db.models import Q
from datetime import datetime

@login_required(login_url='login')
def submit_marks(request):
    # Fetch the staff member based on the current user
    staff_member = get_object_or_404(Staff, user=request.user)
    # Get the subjects associated with this staff member
    subjects = staff_member.subjects.all()

    # Get all students for this staff member's subjects
    students = StudentNew.objects.filter(subjects__in=subjects).distinct()

    # Check if the staff member teaches any subject
    if not subjects:
        messages.error(request, "You are not assigned to any subjects.")
        return redirect('some_error_page')

    # Fetch the first subject for simplicity
    subject = subjects[0]

    if request.method == 'POST':
        # Retrieve the selected student and subject from the form
        student_id = request.POST.get('student_id')
        month = request.POST.get('month')
        selected_student = get_object_or_404(StudentNew, pk=student_id)
        selected_subject_id = request.POST.get('subject_id', subject.id)
        selected_subject = get_object_or_404(Subject, pk=selected_subject_id)
        
        scored_marks = request.POST.get('scored_marks')

        if not scored_marks.isdigit():
            messages.error(request, "Please enter a valid score.")
        else:
            scored_marks = int(scored_marks)
            # Determine the grade based on scored marks
            if scored_marks >= 45:
                grade = 'S'
            elif scored_marks >= 40:
                grade = 'A+'
            elif scored_marks >= 35:
                grade = 'A'
            elif scored_marks >= 30:
                grade = 'B+'
            elif scored_marks >= 25:
                grade = 'B'
            elif scored_marks >= 20:
                grade = 'C'
            else:
                grade = 'F'

            # Calculate the percentage
            total_marks = 50
            percentage = (scored_marks / total_marks) * 100

            # Create and save a new Marks entry
            mark = Marks(
                student=selected_student,
                subject=selected_subject,
                total_marks=total_marks,
                scored_marks=scored_marks,
                grade=grade,
                percentage=percentage,
                month=month  # Save the selected month
            )
            mark.save()
            messages.success(request, 'Marks submitted successfully.')
            return redirect('staffpage')

    # For GET request, pass the necessary context
    context = {
        'students': students,
        'selected_subject': subject,  # You might want to pass a list of subjects if the staff teaches multiple subjects
        'months': list(datetime.strftime("%B") for i in range(1, 13)),
    }
    return render(request, 'submit_marks.html', context)



@login_required(login_url='login')
def academic_marks(request):
    student = get_object_or_404(StudentNew, user=request.user)
    enrolled_subjects = student.subjects.all()
    return render(request, 'academic_marks.html', {'enrolled_subjects': enrolled_subjects})


from django.shortcuts import render, get_object_or_404
from .models import Marks, Subject, StudentNew
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def subject_marks_view(request, subject_id):
    student = get_object_or_404(StudentNew, user=request.user)
    subject = get_object_or_404(Subject, pk=subject_id)

    # Retrieve the month from request GET parameters
    selected_month = request.GET.get('month','all')

    if selected_month == 'all':
        marks_entries = Marks.objects.filter(student=student, subject=subject)
    else:
        marks_entries = Marks.objects.filter(student=student, subject=subject, month=selected_month)
    
    months = Marks.objects.filter(student=student, subject=subject)\
                          .values_list('month', flat=True).distinct()

    return render(request, 'subject_marks.html', {
        'subject': subject,
        'marks_entries': marks_entries,
        'months': months,
        'selected_month': selected_month,
    })



# views.py
# views.py
from django.http import JsonResponse
from .models import Timetable, Staff
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def get_subjects_for_day(request):
    day = request.GET.get('day')
    staff_member = get_object_or_404(Staff, user=request.user)
    
    timetables = Timetable.objects.filter(day=day, subject__staff=staff_member)
    
    subjects = [{'id': timetable.subject.id, 'subject_name': timetable.subject.subject_name} for timetable in timetables]
    return JsonResponse({'subjects': subjects})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Staff, StudentNew, Subject
from .forms import FeedbackForm

@login_required(login_url='login')
def submit_feedback(request):
    student = get_object_or_404(StudentNew, user=request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = student
            feedback.save()
            messages.success(request, 'Feedback submitted successfully.')
            return redirect('student')
    else:
        form = FeedbackForm()
        subject_ids = student.subjects.values_list('id', flat=True)
        subject_queryset = Subject.objects.filter(id__in=subject_ids)
        form.fields['subject'].queryset = subject_queryset  # Update to subject queryset
    return render(request, 'submit_feedback.html', {'form': form})

@login_required(login_url='login')
def view_student_feedback(request):
    if request.user.is_superuser:
        classes = MyClass.objects.all()
        return render(request, 'view_student_feedback.html', {'classes': classes})
    else:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')

# views.py
@login_required(login_url='login')
def view_class_feedback(request, class_id):
    # Get the list of staff associated with the class
    staff_list = Staff.objects.filter(class_name_id=class_id)

    # Get the selected staff ID from the request parameters
    selected_staff_id = request.GET.get('staff', '')  # Default to empty string if not provided

    # Filter the feedbacks based on the selected staff, if a specific staff is selected
    if selected_staff_id:
        feedbacks = StudentFeedback.objects.filter(student__class_no=class_id, staff_id=selected_staff_id)
    else:
        # If 'All Staff' or no staff is selected, show all feedback for the class
        feedbacks = StudentFeedback.objects.filter(student__class_no=class_id)

    context = {
        'feedbacks': feedbacks,
        'staff_list': staff_list,
        'selected_staff_id': selected_staff_id
    }
    return render(request, 'view_class_feedback.html', context)




from django.shortcuts import render, redirect
from django.contrib import messages


def manage_feedback_questions(request):
    questions = FeedbackQuestion.objects.all()
    return render(request, 'manage_feedback_questions.html', {'questions': questions})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FeedbackQuestion

def add_feedback_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        FeedbackQuestion.objects.create(question_text=question_text)  # Use the correct field name
        messages.success(request, 'Question added successfully.')
    return redirect('manage_feedback_questions')



from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FeedbackQuestion

def delete_feedback_question(request, question_id):
    if request.method == 'DELETE':
        try:
            question = FeedbackQuestion.objects.get(pk=question_id)
            question.delete()
            return JsonResponse({'message': 'Question deleted successfully'}, status=204)
        except FeedbackQuestion.DoesNotExist:
            return JsonResponse({'error': 'Question not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Subject, FeedbackQuestion, FeedbackStudent, SelectedOption

@login_required(login_url='login')
def feedback_student(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        weak_feedback = request.POST.get('weak_feedback')
        strong_feedback = request.POST.get('strong_feedback')
        
        if not subject_id:
            messages.error(request, 'Subject is required.')
            return redirect('feedback_student')
        
        feedback_student = FeedbackStudent.objects.create(
            student=request.user,
            subject_id=subject_id,
            weak_feedback=weak_feedback,
            strong_feedback=strong_feedback,
        )
        
        for question in FeedbackQuestion.objects.all():
            option_key = f"feedback_option_{question.id}"
            option_value = request.POST.get(option_key)
            if option_value:
                SelectedOption.objects.create(
                    feedback_student=feedback_student,
                    feedback_question=question,
                    option=option_value
                )

        messages.success(request, 'Feedback submitted successfully.')
        
        return redirect('feedback_student')

    else:
        if hasattr(request.user, 'studentnew'):
            enrolled_subjects = request.user.studentnew.subjects.all()
        else:
            enrolled_subjects = Subject.objects.none()

        feedback_questions = FeedbackQuestion.objects.all()

        context = {
            'enrolled_subjects': enrolled_subjects,
            'questions': feedback_questions,
        }
        return render(request, 'feedback_student.html', context)



from django.shortcuts import render
from .models import MyClass, FeedbackStudent

def view_feedback_students(request):
    classes = MyClass.objects.all()
    return render(request, 'view_feedback_students.html', {'classes': classes})

from django.shortcuts import render
from .models import MyClass, User, FeedbackStudent, SelectedOption

def feedback_details(request, class_id):
    # Retrieve students belonging to the selected class
    students = User.objects.filter(studentnew__class_no=class_id)

    # Filter feedbacks based on the students
    feedbacks = FeedbackStudent.objects.filter(student__in=students)

    # Fetch selected options related to the feedbacks
    selected_options = SelectedOption.objects.filter(feedback_student__in=feedbacks)

    return render(request, 'feedback_details.html', {'feedbacks': feedbacks, 'selected_options': selected_options})







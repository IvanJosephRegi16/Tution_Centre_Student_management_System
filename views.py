from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Subject




# Create your views here.

def home(request):
    return render (request,"index.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def myhome(request):
    return render (request,"index2.html")

def about(request):
    return render(request,"about.html")

def add_subject(request):
    return render(request,"add_subject.html")

def view_subjects(request):
    return render(request,"view_subjects.html")

def view_class(request):
    return render(request,"view_class.html")

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
            
            
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # print(f"Username: {username}, Password: {password}")

        # # Fixed admin credentials
        # admin_username = 'admin'
        # admin_password = 'admin'
        
        # # Check if the user is the admin
        # if username == admin_username and password == admin_password:
        #     # Authenticate the admin user
        #     admin_user = authenticate(request, username=admin_username, password=admin_password)
            
        #     if admin_user is not None:
        #         auth_login(request, admin_user)
        #         messages.success(request, "Admin Login Success!!!")
        #         return redirect('generate_user')  # Redirect to the admin page

        # # Check if the user is a regular user
        # user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     auth_login(request, user)
        #     if user.role == 'STUDENT':
        #         request.session['username'] = username
        #         messages.success(request, "Login Success!!!")
        #         return redirect('myhome')
        #     elif user.role == 'STAFF':
        #         messages.success(request, "Login Success!!!")
        #         return HttpResponse('demo')

        # # If the regular login fails, try slogin
        # slogin_user = authenticate(request, username=username, password=password)

        # if slogin_user is not None:
        #     auth_login(request, slogin_user)
        #     messages.success(request, "Login Success!!!")
        #     return redirect('myhome')
        user=authenticate( username=username, password=password)
        if user is not None:
            auth_login(request,user)
            if user.is_staff==True:
                request.session["user"]='admin'
                return redirect('generate_user')
            elif user.role == 'STUDENT':
                request.session["user"]='student'
                return redirect('myhome')
            # else:
            #     request.session["user"]='staff'
            #     return redirect('myhome')
        
        
        
        else:
            # Invalid username or password for both admin and regular users
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')

def StaffReg(request):
    return render (request,"thrpreg.html")

# oct 1 updations TherapHome


def StaffpHome(request):
    return render(request,"demo.html")

# views.py

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import random
import string

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

    return render(request, 'generate_user.html')

# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def slogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('myhome')
        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid email or password')

    return render(request, 'slogin.html')









from django.shortcuts import render
from .models import User

def all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})

# your_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
# AppOne/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
# AppOne/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User

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
        student = Student(
            
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



# AppOne/views.py
from django.shortcuts import render
from .models import Student

def view_student_details(request):
    students = Student.objects.all()
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
    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Student

def submit_leave_application(request):
    if request.method == 'POST':
        # Retrieve data from the leave application form
        reason = request.POST.get('reason')

        # Process the leave application logic (save to database, send notifications, etc.)
        # ...

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the student's email address from the database
            student_email = get_student_email(request.user)
            
            # Send an email to admins with the leave application reason
            send_email_to_admins(reason, student_email)

            return HttpResponse("Leave application submitted successfully!")
        else:
            # Redirect to a login page or handle the case where the user is not authenticated
            return HttpResponse("User not authenticated. Please log in.")
    else:
        return render(request, 'AppOne/leave_application.html')

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
from django.shortcuts import render, get_object_or_404
from .models import Student

def applied_leave(request, user_id):
    # Retrieve the student instance based on the user_id
    student = get_object_or_404(Student, user__id=user_id)

    return render(request, 'AppOne/applied_leave.html', {'student': student})
from django.shortcuts import render
from .models import Student

def applied_leave_list(request):
    students = Student.objects.all()
    return render(request, 'applied_leave_list.html', {'students': students})


# views.py
from django.shortcuts import render, redirect
from .models import Studentdetails
from django.http import HttpResponse

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
from django.shortcuts import render, redirect
from .models import MyClass

def add_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        # Add more fields as needed

        # Create a new class instance and save it to the database
        MyClass.objects.create(class_name=class_name)

    # Fetch the list of all classes
    classes = MyClass.objects.all()

    return render(request, 'add_class.html', {'classes': classes})
# views.py
from django.shortcuts import render
from .models import Student  # Import your Student model

# views.py
from django.shortcuts import render
from .models import Student

def class_details(request, class_number):
    students = Student.objects.filter(course=class_number)
    context = {'students': students, 'class_number': class_number}
    return render(request, 'class_details.html', context)




def add_subject(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        Subject.objects.create(subject_name=subject_name)
        return redirect('view_subjects')  # Redirect to the view_subjects page after adding a subject
    return render(request, 'add_subject.html')

def view_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'view_subjects.html', {'subjects': subjects})




from django.shortcuts import render, redirect
import pandas as pd
from .models import Student

def update_students(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file, engine='openpyxl')

        for index, row in df.iterrows():
            student, created = Student.objects.update_or_create(
                email=row['email'],
                defaults={
                    'first_name': row['first_name'],
                    'course': row['course'],
                    'session_year': row['session_year'],
                    'password': row['password'],
                }
            )

        return redirect('myhome')  # Redirect to a success page or another view

    return render(request, 'update_students.html')



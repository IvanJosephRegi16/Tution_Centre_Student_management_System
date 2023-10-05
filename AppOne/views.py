from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control




# Create your views here.

def home(request):
    return render (request,"index.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def myhome(request):
    return render (request,"index2.html")

def about(request):
    return render(request,"about.html")

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
            # messages.success(request,"Registration Successfull..!")

            return redirect('login')
   return render(request,'signup.html')
            
# user
def login(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        
        # Use the model class to query the database
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            auth_login(request,user)
            if user.role=='STUDENT':
               request.session['username'] = username
               messages.success(request,"Login Success!!!")
               return redirect('myhome')
            elif user.role=='STAFF':
               messages.success(request,"Login Success!!!")
               return HttpResponse('demo')
            elif user.role=='ADMIN':
               messages.success(request,"Login Success!!!")
               return HttpResponse("Admin login ")
                          
        else:
            messages.error(request,"Some thing went wrong")
            return redirect('login')
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def StaffReg(request):
    return render (request,"thrpreg.html")

# oct 1 updations TherapHome


def StaffpHome(request):
    return render(request,"demo.html")
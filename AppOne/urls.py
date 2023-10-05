from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('myhome',views.myhome,name='myhome'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutPage'),
    path('StaffReg',views.StaffReg,name='StaffReg'),
    path('StaffpHome',views.StaffpHome,name='StaffpHome'),
    path('about/', views.about,name='about'),
    path('course/', views.course,name='course'),
    path('testimonial/', views.testimonial,name='testimonial'),
     
    path('detail/', views.detail,name='detail'),
     
    path('feature/', views.feature,name='feature'),
     
    path('team/', views.team,name='team'),
    
    path('contact/', views.contact,name='contact'),
    
    
    
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')


    
]

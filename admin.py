# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from . models import User

# # Register your models here.


    
# admin.site.register(User)








from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Remove the first registration
# admin.site.register(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role')  # Add other fields as needed

# Register your custom User model with the updated UserAdmin
admin.site.register(User, CustomUserAdmin)

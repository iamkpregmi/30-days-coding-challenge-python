from django.contrib import admin
from .models import User_Register

class User_Register_Admin(admin.ModelAdmin):
    list_display = ("Username","Name","Phone_No","DOB","Gender")

admin.site.register(User_Register,User_Register_Admin)
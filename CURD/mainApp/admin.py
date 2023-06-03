from django.contrib import admin
from .models import Employee

class Employee_Admin(admin.ModelAdmin):
    list_display = ("id","name","email","phone","salary","city")

admin.site.register(Employee,Employee_Admin)
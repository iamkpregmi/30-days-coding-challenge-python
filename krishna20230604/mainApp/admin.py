from django.contrib import admin
from .models import Result

class Result_Admin(admin.ModelAdmin):
    list_display = ("Rollno","Name","Percentage","Result")

admin.site.register(Result,Result_Admin)
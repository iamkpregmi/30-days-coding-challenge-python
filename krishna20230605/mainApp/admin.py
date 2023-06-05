from django.contrib import admin
from .models import Student_Grade_Card

class Student_Grade_Card_Admin(admin.ModelAdmin):
    list_display = ("Roll_No","Name","Physics","Chemistry","Maths","English","Computer_Science")

admin.site.register(Student_Grade_Card,Student_Grade_Card_Admin)

from django.contrib import admin
from .models import userlogin

class userlogin_Admin(admin.ModelAdmin):
    list_display = ("userid","password")

admin.site.register(userlogin,userlogin_Admin)
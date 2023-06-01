from django.contrib import admin
from .models import myfileupload

class myfileuploadAdmin(admin.ModelAdmin):
    list_display = ["title","myfile"]

admin.site.register(myfileupload,myfileuploadAdmin)
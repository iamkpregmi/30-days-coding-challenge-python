from django.contrib import admin
from myblog.models import myblogpost

class myblogpostAdmin(admin.ModelAdmin):
    list_display = ("title","description")

admin.site.register(myblogpost,myblogpostAdmin)
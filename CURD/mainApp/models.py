from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField()
    city = models.CharField(max_length=30, default="", null=True, blank=True)

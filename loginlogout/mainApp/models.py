from django.db import models

class User_Register(models.Model):
    Username = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Phone_No = models.IntegerField()
    DOB = models.DateField()
    Gender = models.CharField(max_length=6)


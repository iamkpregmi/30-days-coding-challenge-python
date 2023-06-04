from django.db import models

class Result(models.Model):
    Rollno = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Percentage = models.DecimalField(max_digits = 5,decimal_places = 2, default=None)
    Result = models.CharField(max_length=4)


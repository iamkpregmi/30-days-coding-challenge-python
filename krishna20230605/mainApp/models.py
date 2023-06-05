from django.db import models

class Student_Grade_Card(models.Model):
    Roll_No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Maths = models.IntegerField()
    English = models.IntegerField()
    Computer_Science = models.IntegerField()

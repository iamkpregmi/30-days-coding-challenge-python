from django.db import models

class userlogin(models.Model):
    userid = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=200)

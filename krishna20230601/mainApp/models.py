from django.db import models

class myfileupload(models.Model):
    title = models.CharField(max_length=100)
    myfile = models.FileField(upload_to="test/",max_length=200,null=True,default=None)

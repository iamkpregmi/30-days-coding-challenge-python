from django.db import models
from tinymce.models import HTMLField

class myblogpost(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()

from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.CharField(max_length=2000)
    short = models.CharField(max_length=15)
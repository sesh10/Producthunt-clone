from django.db import models

# Create your models here.

class Account(models.Model):
    userid = models.CharField(max_length=15)
    profpic = models.ImageField()

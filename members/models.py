from django.db import models
from datetime import date

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    phone = models.IntegerField(default=0)
    joined_date = models.DateField(default=date.today)

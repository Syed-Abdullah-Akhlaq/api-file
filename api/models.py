from django.db import models

# Create your models here.

class Students(models.Model):
    Name = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Age = models.IntegerField()
    Roll_Number =  models.IntegerField()
    School_Name = models.CharField(max_length=100)

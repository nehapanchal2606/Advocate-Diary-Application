from django.db import models

# Create your models here.


class Diary(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    case_number = models.IntegerField()
    case_Date = models.DateField()
    case_des = models.TextField()
    
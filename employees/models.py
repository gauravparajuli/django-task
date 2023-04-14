from django.db import models

# Create your models here.


class Employee(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    dob = models.DateField(null=False)
    salary = models.IntegerField(null=False)

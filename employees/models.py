from datetime import date, timedelta
from django.db import models
import math

# Create your models here


class Employee(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    dob = models.DateField(null=False)
    salary = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def current_age(self):
        age = date.today() - self.dob
        return (age//timedelta(365.25))

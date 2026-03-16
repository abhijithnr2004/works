from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=100)

    department = models.CharField(max_length=100)

    designation = models.CharField(max_length=100)

    salary = models.IntegerField()

    email = models.EmailField()

    date_of_joining = models.DateField()

    owner =  models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.name

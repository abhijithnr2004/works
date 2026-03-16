from django.db import models

from django.contrib.auth.models import User


class Vehicle(models.Model):

    name = models.CharField(max_length=200)

    model = models.PositiveIntegerField()

    brand = models.CharField(max_length=200)

    FUEL_TYPE_OPTIONS = (
        ('petrol', 'Petrol'),
        ('diesel', 'Disel'),
        ('ev', 'Ev'),
    )

    fule_type = models.CharField(max_length=100, choices=FUEL_TYPE_OPTIONS, default='petrol')

    owner_condition = models.PositiveIntegerField()

    color = models.CharField()

    price = models.PositiveIntegerField()

    running_km = models.PositiveIntegerField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class ElectronicProduct(models.Model):

    product_name = models.CharField(max_length=200)

    brand = models.CharField(max_length=150)

    CATEGORY_CHOICES = (
        ("mobile", "Mobile"),
        ("laptop", "Laptop"),
        ("accessory", "Accessory"),
        ("wearable", "Wearable"),
        ("other", "Other"),
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    price = models.PositiveIntegerField()

    warranty_period = models.PositiveIntegerField(help_text="Warranty in months")

    stock_quantity = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product_name



    


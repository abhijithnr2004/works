from django.db import models

# Create your models here.

class Clothing(models.Model):

    name = models.CharField(max_length=200,unique=True)

    brand = models.CharField(max_length=150, blank=True)

    CATEGORY_CHOICES = (
        ("men", "men"),
        ("women", "women"),
        ("kids", "kids")
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default="kids")

    SIZE_CHOICES = (
        ("small", "small"),
        ("medium", "medium"),
        ("large", "large")
    )

    size = models.CharField(max_length=10, choices=SIZE_CHOICES,default="small")

    color = models.CharField(max_length=50)

    price = models.PositiveIntegerField()

    stock = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

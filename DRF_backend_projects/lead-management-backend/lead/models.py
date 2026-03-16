from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):

    SOURCE_CHOICES = (
        ('Website', 'Website'),
        ('Referral', 'Referral'),
        ('Advertisement' , 'Advertisement'),
        ('Other', 'Other')
    )

    STATUS_CHOICES = (
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified' , 'Qualified'),
        ('Lost', 'Lost')
    )

    lead_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    source = models.CharField(max_length=50, choices=SOURCE_CHOICES)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)



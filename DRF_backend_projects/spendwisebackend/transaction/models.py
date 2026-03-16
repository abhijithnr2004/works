from django.db import models
from django.contrib.auth.models import User



class Expense(models.Model):

    title = models.CharField(max_length=200)

    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('groceries', 'Groceries'),
        ('rent', 'Rent'),
        ('transport', 'Transportation'),
        ('fuel', 'Fuel'),
        ('shopping', 'Shopping'),
        ('medical', 'Medical'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
        ('bills', 'Bills'),
        ('investment', 'Investment'),
        ('gift', 'Gifts'),
        ('others', 'Others'),
    ]

    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="food")

    amount = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.title



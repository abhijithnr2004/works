from django.db import models

from django.contrib.auth.models import User

# one-to-many
class Customer(models.Model): 

    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='customers')

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15, blank=True)

    email = models.EmailField(blank=True)

    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name
    
    class Meta:

        ordering = ['-created_at']

class Product(models.Model):

    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')

    name = models.CharField(max_length=200)

    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True)

    def __str__(self):

        return f"{self.name} - ₹{self.unit_price}"
    
class Bill(models.Model):

    STATUS_CHOICES = [

        ('draft', 'Draft'),

        ('issued', 'Issued'),

        ('paid', 'Paid'),

    ]

    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bills')

    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name='bills')

    bill_number = models.CharField(max_length=20, unique=True)

    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
      
        return sum(item.line_total for item in self.items.all())
    
    def __str__(self):

        return f"Bill #{self.bill_number} — {self.customer.name}"
    
class BillItem(models.Model):
    """
    A single line item in a bill (product + quantity + price snapshot).
    
    We store product_name and unit_price as snapshot values rather than
    a ForeignKey to Product. This means old bills remain accurate even
    if a product's price changes in the future.
    """
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE,related_name='items')

    product_name = models.CharField(max_length=200)

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property

    def line_total(self):

        return self.quantity * self.unit_price
    
    def __str__(self):
        
        return f"{self.product_name} × {self.quantity}"
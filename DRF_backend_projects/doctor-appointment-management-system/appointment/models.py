from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):

    DEPARTMENT_CHOICES = [
        ('General', 'General'),
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
    ]

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    appointment_id = models.AutoField(primary_key=True)

    patient_name = models.CharField(max_length=255)

    doctor_name = models.CharField(max_length=255)
    
    department = models.CharField(
        max_length=50, 
        choices=DEPARTMENT_CHOICES, 
        default='General'
    )
    
    appointment_date = models.DateField()

    appointment_time = models.TimeField()
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='Scheduled'
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name} ({self.appointment_date})"
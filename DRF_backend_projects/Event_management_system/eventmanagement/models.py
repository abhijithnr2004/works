from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model) :

    event_name = models.CharField(max_length=100)

    EVENT_TYPE_CHOICES = [
        ("conference","conference"),
        ("workshop","workshop"),
        ("seminar","seminar"),
        ("webinar","webinar"),
        ("meetup","meetup")
    ]

    event_type = models.CharField(max_length=200,choices=EVENT_TYPE_CHOICES,default="conference")

    location = models.CharField(max_length=100)

    event_date = models.DateField()

    event_time = models.TimeField()

    STATUS_CHOICES = [

        ("upcoming","upcoming"),
        ("ongoing","ongoing"),
        ("completed","completed"),
        ("cancelled","cancelled")
    ]

    status = models.CharField(max_length=300,choices=STATUS_CHOICES,default="upcoming")

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    
    created_date = models.DateTimeField(auto_now_add=True)



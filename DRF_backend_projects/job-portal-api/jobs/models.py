from django.db import models


class Job(models.Model):

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    JOB_TYPE_CHOICES = (
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Internship", "Internship"),
        ("Remote", "Remote")
    )

    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    experience = models.PositiveIntegerField()

    salary = models.PositiveIntegerField()

    skills = models.TextField()

    is_remote = models.BooleanField()

    is_active = models.BooleanField()

    posted_date = models.DateTimeField(auto_now_add=True)
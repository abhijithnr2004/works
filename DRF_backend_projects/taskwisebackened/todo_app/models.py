from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):

    title = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    CATEGORY_OPTIONS=(
        ("home","home"),
        ("work","work"),
        ("personal","personal")
    )

    category = models.CharField(max_length=200,choices=CATEGORY_OPTIONS,default="work")

    PRIORITY_OPTIONS=(
        (1,"low"),
        (2,"medium"),
        (3,"high")
    )

    priority = models.CharField(max_length=15,choices=PRIORITY_OPTIONS,default=2)

    completed_status = models.BooleanField(default=False)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :

    phone = models.CharField(max_length=100)

    def __str__(self):

        return self.username

class Query(models.Model) :

    question = models.CharField(max_length=500)

    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="query_images",null=True,blank=True)

    def __str__(self):

        return self.question


class Solution(models.Model) :

    answer = models.TextField()

    question = models.ForeignKey(Query,on_delete=models.CASCADE,related_name="answers")

    answered_by = models.ForeignKey(User,on_delete=models.CASCADE)

    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.answer

class Upvote(models.Model) :

    answer = models.ForeignKey(Solution,on_delete=models.CASCADE,related_name="vote")

    voted_by = models.ForeignKey(User,on_delete=models.CASCADE)

    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta :

        unique_together = ("answer","voted_by")

    





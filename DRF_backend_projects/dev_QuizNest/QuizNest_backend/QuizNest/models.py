from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError

# Create your models here.
class User(AbstractUser) :

    phone = models.CharField(max_length=12)

class Languages(models.Model) :

    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name

class Quiz(models.Model) :

    language = models.ForeignKey(Languages,on_delete=models.CASCADE,related_name="quiz")

    LEVEL_CHOICES = [
        (1,"easy"),
        (2,"medium"),
        (3,"hard")
    ]

    level = models.CharField(max_length=100,choices=LEVEL_CHOICES,default="easy")

    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner")

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.language} - {self.level}"

class Question(models.Model) :

    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="questions")

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Choices(models.Model) :

    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="choices")

    option = models.CharField(max_length=100)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option
    
    def save(self,*args,**kwargs):

        if self.is_correct:

            if self.question.choices.filter(is_correct=True).exclude(pk=self.pk).exists():

                raise ValidationError("There is already an answer for this question")
                
        super().save(*args,**kwargs)
    
class QuizAttempt(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz_attempts")

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")

    score = models.IntegerField(default=0)

    is_completed = models.BooleanField(default=False)

    started_at = models.DateTimeField(auto_now_add=True)

    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):

        return f"{self.created_by.username} - {self.quiz}"

class UserAnswer(models.Model):

    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name="answers")

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    selected_choice = models.ForeignKey(Choices, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attempt.created_by.username} - {self.question.title}"
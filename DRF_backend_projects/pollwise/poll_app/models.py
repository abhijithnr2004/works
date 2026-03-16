from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

# custom User model
# 

class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True)


class Poll(models.Model):

    question = models.TextField()

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):

        return self.question

class Choice(models.Model):

    option = models.CharField(max_length=200)

    poll_object = models.ForeignKey(
                                        Poll,on_delete=models.CASCADE,
                                        related_name="choices"
                                        )
    
    def __str__(self):
        return self.option
    

class Vote(models.Model):

    poll_object = models.ForeignKey(Poll,on_delete=models.CASCADE,related_name="votes")

    choice_object = models.ForeignKey(Choice,on_delete=models.CASCADE,related_name="votes")

    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="votes")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :

        unique_together = ("owner","poll_object")








# poll_instance = Poll.objects.get(id=1)

# choices_objects=Choice.objects.filter(poll_object=poll_instance)

# poll_instance.choices.all() reverse referencing 

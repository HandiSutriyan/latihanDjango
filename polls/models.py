from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    #relation
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null = True
        )
    choices = models.ForeignKey(
        'polls.Choice',
        null=True,
        on_delete=models.CASCADE,
        related_name='choices'
    ) 

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
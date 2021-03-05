from django.db import models
from datetime import date


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    points = models.IntegerField(default=0)


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    true_answer = models.CharField(max_length=30)


class ChoiceAnsw(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=40)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=30)

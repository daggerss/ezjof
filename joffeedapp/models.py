from django.db import models

class JOF(models.Model):

    class Status(models.IntegerChoices):
        isPending = 1
        inProgress = 2
        notTaken = 3
        completed = 4

    status = models.IntegerField(default=Status.isPending,choices=Status.choices)
    isrush = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    date = models.DateField()
    specifications = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')
    spiel = models.CharField(max_length=100, default='')
    objects = models.Manager()

# Create your models here.

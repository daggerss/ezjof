from django.db import models

class JOF(models.Model):
    name = models.CharField(max_length=100, default='')
    blastdate = models.DateField()
    shortdesc = models.CharField(max_length=100, default='')
    jobspecs = models.CharField(max_length=100, default='')
    spiel = models.CharField(max_length=100, default='')
    ispending = models.BooleanField()
    isrush = models.BooleanField()
    isarchive = models.BooleanField()
    objects = models.Manager()

# Create your models here.

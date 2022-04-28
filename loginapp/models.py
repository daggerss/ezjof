from django.db import models

# Create your models here.
class Department(models.Model):
    dname = models.CharField(max_length=100, default='')
    objects = models.Manager()

class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=100,  default='')
    type = models.CharField(max_length=10, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    isHead = models.BooleanField(default=False)
    objects = models.Manager()


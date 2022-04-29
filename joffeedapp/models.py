from asyncio.windows_events import NULL
from django.db import models

from loginapp.models import Account, Department

class JOF(models.Model):

    IS_PENDING = 1
    IN_PROGRESS = 2
    NOT_TAKEN = 3
    IS_COMPLETED = 4

    JOF_STATUS_CHOICES = (
        (IS_PENDING, 'Is Pending'),
        (IN_PROGRESS, 'In Progress'),
        (NOT_TAKEN, 'Not Taken'),
        (IS_COMPLETED, 'Is Completed'),
    )

    MP3 = 1
    MP4 = 2
    PNG = 3
    GIF = 4
    PDF = 5
    DOCX = 6
    OTHER = 7    

    JOF_TYPE_CHOICES = (
        (MP3, 'Music/Audio'),
        (MP4, 'Video'),
        (PNG, 'Picture'),
        (GIF, 'GIF'),
        (PDF, 'PDF'),
        (DOCX, 'Word Document'),
        (OTHER, 'Other'),
    )
    
    status = models.IntegerField(choices=JOF_STATUS_CHOICES, default=NOT_TAKEN)
    isrush = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    date = models.DateField()
    pegs = models.URLField(null=True, blank=True, default='')
    summary = models.CharField(max_length=100, default='')
    type = models.IntegerField(choices=JOF_TYPE_CHOICES, default=OTHER)
    spiel = models.CharField(max_length=100, default='')
    client = models.ForeignKey(Account, related_name='Client', on_delete=models.CASCADE, default=NULL)
    artist = models.ForeignKey(Account, related_name='Artist', on_delete=models.CASCADE, default=NULL, blank=True, null=True)
    department = models.ForeignKey(Department, related_name='Department', on_delete=models.CASCADE, default=NULL)
    objects = models.Manager()  
          


# Create your models here.

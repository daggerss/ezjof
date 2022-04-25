import datetime
#from django.forms.widgets import NumberInput
from django.forms import ModelForm
from .models import *

class JOFForm(ModelForm):
    class Meta:
        model = JOF
        fields=('isrush','name','date','summary','type','pegs' ,'description','spiel') 
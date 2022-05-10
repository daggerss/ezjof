from django.forms import ModelForm, forms
from .models import *

class JOFForm(ModelForm):
    class Meta:
        model = JOF
        fields=('isrush','name','date','summary','type','pegs' ,'description','spiel') 
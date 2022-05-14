from django.forms import ModelForm, forms
from .models import *

class JOFForm(ModelForm):
    class Meta:
        model = JOF
        fields = ('isrush','name','date','summary','type','pegs' ,'description','spiel')

    def __init__(self, *args, **kwargs):
        super(JOFForm, self).__init__(*args, **kwargs)
        self.fields['spiel'].required = False

class DraftForm(ModelForm):
    class Meta:
        model = Draft
        fields = ('file',)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) 

import email
from django import forms
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                            'placeholder' :'Email',
                            'class': 'textfield reg semibold'
                            }),
                            label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                            'placeholder': 'Password',
                            'class': 'textfield reg semibold'
                            }),
                            label=False)
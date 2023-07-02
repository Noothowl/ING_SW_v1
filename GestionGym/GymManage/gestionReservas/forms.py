from django import forms
from .models import *

class addUser(forms.Form):

    name=forms.CharField()
    lastname=forms.CharField()
    password = forms.CharField()
    isAdmin = forms.BooleanField(required=False)

class addReserve(forms.Form):

    usuario=forms.ModelChoiceField(queryset=Users.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

class loginForm(forms.Form):
    usuario=forms.CharField()
    clave=forms.CharField(widget=forms.PasswordInput())

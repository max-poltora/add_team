from django.forms import ModelForm
from django import forms
from .models import Person

class InputForm(ModelForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']
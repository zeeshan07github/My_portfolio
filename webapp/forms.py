from django import forms
from .models import *


class createForm(forms.ModelForm):
    
    class Meta:
        model = posts
        fields = '__all__'
        widgets = {
            'created':forms.DateTimeInput(),
            'tags':forms.CheckboxSelectMultiple(),
        }


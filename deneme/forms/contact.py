from django import forms
from django.forms import fields
from deneme.models import contactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model=contactModel
        fields=('name_lastname','email','message')
    

    

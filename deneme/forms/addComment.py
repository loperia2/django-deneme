from django import forms
from django.forms import fields
from deneme.models import commentModel

class addCommmentForm(forms.ModelForm):
    class Meta:
        model=commentModel
        fields=('comment',)
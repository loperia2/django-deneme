from django.forms import fields
from deneme import models
from django import forms
from deneme.models import articlesModel
class addArticleForm(forms.ModelForm):
    class Meta:
        model = articlesModel
        exclude =('writer','slug')
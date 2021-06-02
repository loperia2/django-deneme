from django import forms
from deneme.models import articlesModel

class editArticleForm(forms.ModelForm):
    class Meta:
        model= articlesModel
        exclude=('writer','slug')
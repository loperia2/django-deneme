from django import forms
from django.core.mail import send_mail
from django.forms import fields
from deneme.models import contactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model=contactModel
        fields=('name_lastname','email','message')
    def send_email(self,msg):
        send_mail(
            subject='New Message',
            message=msg,
            from_email=None,
            fail_silently= False,
            recipient_list=['gney96@gmail.com']
        )

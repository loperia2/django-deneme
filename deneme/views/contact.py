from django.shortcuts import redirect, render
from deneme.forms import ContactForm
from deneme.models import contactModel
from django.views.generic import FormView
from django.core.mail import send_mail

class contactView(FormView):
    template_name='pages/contact.html'
    form_class= ContactForm
    success_url='/email-sent'

    def form_valid(self, form):
        form.save()
        form.send_email(msg=form.cleaned_data.get('message'))
        return super().form_valid(form)
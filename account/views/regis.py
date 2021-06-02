from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import regisForm
from django.contrib.auth import login,authenticate

def regis(request):
    if request.method == 'POST':
       form=regisForm(request.POST)
       if form.is_valid():
           form.save()
           username=''.join(form.cleaned_data.get('username'))
           passwords=''.join(form.cleaned_data.get('password1'))
           print('hey')
           user=authenticate(username=username, password=passwords)
           login(request,user)
           return redirect('homepage')
    else:
        form=regisForm() 
    return render(request,'pages/regis.html', context={
        'form':form
    })

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import editProfileForm
@login_required(login_url='/')
def editProfile(request):
    if request.method == 'POST':
       form=editProfileForm(request.POST, request.FILES, instance=request.user)
       if form.is_valid():
           form.save()
           messages.success(request,'Profile Edited')
    else:
        form=editProfileForm(instance= request.user) 
    return render(request,'pages/editProfile.html', context={
        'form':form
    })

from django.shortcuts import render
from django.http import HttpResponse

def comm(request):
    context={
        
    }
    return render(request,'pages/comm.html', context=context)
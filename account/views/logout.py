from django.contrib.auth import logout
from django.shortcuts import redirect

def makeLogOut(request):
    logout(request)
    return redirect('homepage')
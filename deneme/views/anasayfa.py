from django.shortcuts import render


def anasayfa(request):
    context={
        'name':'vars'
    }
    return render(request, 'pages/mainpage.html',context=context)    
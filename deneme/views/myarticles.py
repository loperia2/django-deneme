from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myarticles(request):
    articles=request.user.articles.all()
    page=request.GET.get('page')
    paginator=Paginator(articles,5)
    return render(request, 'pages/myArticles.html', context={
            'articles':paginator.get_page(page),

    })

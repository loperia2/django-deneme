from django.shortcuts import render
from deneme.models import articlesModel
from django.core.paginator import Paginator
from django.db.models import Q


def anasayfa(request):
    query=request.GET.get('q')
    
    articles = articlesModel.objects.order_by('-id')
    if query:
        articles=articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator= Paginator(articles,2)
    return render(request, 'pages/mainpage.html',context={
        'articles': paginator.get_page(page)
    })    
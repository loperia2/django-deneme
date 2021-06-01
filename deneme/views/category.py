from django.shortcuts import render, get_object_or_404
from deneme.models import articles, articlesModel, categoryModel
from django.core.paginator import Paginator

def category(request,categorySlug):
    category=get_object_or_404(categoryModel, slug=categorySlug)
    articles=category.article.order_by('id')
    page=request.GET.get('page')
    paginator=Paginator(articles,2)
    return render(request,'pages/mainpage.html',context={
        'articles': paginator.get_page(page)
    })

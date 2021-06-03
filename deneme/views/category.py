from django.shortcuts import render, get_object_or_404
from deneme.models import articles, articlesModel, categoryModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class categoryView(ListView):
    model=categoryModel
    template_name='pages/category.html'
    context_object_name= 'articles'
    paginate_by= 2
    
    def get_queryset(self):
        category=get_object_or_404(categoryModel,slug=self.kwargs['categorySlug'])
        return category.article.all().order_by('-id')

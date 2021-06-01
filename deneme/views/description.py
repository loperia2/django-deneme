from django.shortcuts import get_object_or_404, render
from deneme.models import articlesModel
def description(request,descriptionSlug):
    article=get_object_or_404(articlesModel, slug=descriptionSlug)
    comments=article.comments.all()
    return render(request, 'pages/description.html', context={
        
        'article': article,
        'comments': comments

    })

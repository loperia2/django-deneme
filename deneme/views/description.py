from django.shortcuts import get_object_or_404, render
from deneme.models import articlesModel
from deneme.forms import addCommmentForm
def description(request,descriptionSlug):
    article=get_object_or_404(articlesModel, slug=descriptionSlug)
    comments=article.comments.all()
    if request.method == 'POST':
        commentAddForm=addCommmentForm(data=request.POST)
        if commentAddForm.is_valid():
            comment=commentAddForm.save(commit=False)
            comment.writer=request.user
            comment.article=article
            comment.save()
    commentAddForm=addCommmentForm()
    return render(request, 'pages/description.html', context={
        
        'article': article,
        'comments': comments,
        'commentAddForm': commentAddForm

    })

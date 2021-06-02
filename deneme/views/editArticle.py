from django.shortcuts import render,redirect,get_object_or_404
from deneme.forms import editArticleForm
from django.contrib.auth.decorators import login_required
from deneme.models import articlesModel

def editArticle(request,editSlug):
    article=get_object_or_404(articlesModel,slug=editSlug, writer=request.user)
    form=editArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('description', descriptionSlug=article.slug)
    return render(request, 'pages/editArticle.html', context={
        'form':form
    })
        

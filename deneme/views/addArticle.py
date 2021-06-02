from django.shortcuts import redirect, render
from deneme.forms import addArticleForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def addArticle(request):
    form= addArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.writer=request.user
        article.save()
        form.save_m2m()
        return redirect('description', descriptionSlug=article.slug)
    return render(request, 'pages/addArticle.html', context={
        'form':form
    })

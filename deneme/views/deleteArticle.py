from django.contrib.auth.decorators import login_required
from deneme.models import articlesModel
from django.shortcuts import get_object_or_404,redirect

@login_required(login_url='/')
def deleteArticle(request,deleteSlug):
    get_object_or_404(articlesModel, slug=deleteSlug ,writer=request.user).delete()
    return redirect('myarticles')

    

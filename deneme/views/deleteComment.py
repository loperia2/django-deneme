from django.contrib.auth.decorators import login_required
from deneme.models import commentModel
from django.shortcuts import get_object_or_404,redirect, render, redirect

@login_required(login_url='/')
def deleteComment(request,id):
    comment=get_object_or_404(commentModel,id=id)
    if comment.writer == request.user or comment.article.write == request.user :
        comment.delete()
        return redirect('description', descriptionSlug=comment.article.slug)
    else:
        return render('homepage')
    

    

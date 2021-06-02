from django.contrib.auth.decorators import login_required
from deneme.models import commentModel
from django.shortcuts import get_object_or_404,redirect, render, redirect
from django.contrib import messages

@login_required(login_url='/')
def deleteComment(request,id):
    comment=get_object_or_404(commentModel,id=id)
    if comment.writer == request.user or comment.article.write == request.user :
        comment.delete()
        messages.success(request,'Comment Deleted')
        return redirect('description', descriptionSlug=comment.article.slug)
    else:
        return render('homepage')
    

    

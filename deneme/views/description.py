from django.shortcuts import get_object_or_404, redirect, render
from deneme.models import articlesModel, comments
from deneme.forms import addCommmentForm
from django.views import View
from django.contrib import messages

class Description(View):
    http_method_names=['get','post']
    commentAddForm = addCommmentForm
    def get(self,request,descriptionSlug):
        article=get_object_or_404(articlesModel,slug=descriptionSlug)
        comments=article.comments.all()
        return render(request, 'pages/description.html', context={
            'article':article,
            'comments':comments,
            'commentAddForm': self.commentAddForm
        })
    def post(self,request,descriptionSlug):
        article=get_object_or_404(articlesModel,slug=descriptionSlug)
        commentAddForm=self.commentAddForm(request.POST)
        if commentAddForm.is_valid():
            comment=commentAddForm.save(commit=False)
            comment.writer=request.user
            comment.article=article
            comment.save()
            messages.success(request,'Comment Added')
        return redirect('description',descriptionSlug=descriptionSlug)




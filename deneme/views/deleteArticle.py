from django.contrib.auth.decorators import login_required
from deneme.models import articlesModel
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class deleteArticleView(DeleteView):
    template_name='pages/deleteArticleConformation.html'
    success_url=reverse_lazy('myarticles')
    slug_url_kwarg='deleteSlug'
    def get_queryset(self):
        article=articlesModel.objects.filter(slug=self.kwargs['deleteSlug'], writer=self.request.user)
        return article

    

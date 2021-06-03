from django.shortcuts import render,redirect,get_object_or_404
from deneme.forms import editArticleForm
from django.contrib.auth.decorators import login_required
from deneme.models import articlesModel
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
class editArticleView(LoginRequiredMixin, UpdateView):
    login_url=reverse_lazy('login')
    template_name='pages/editArticle.html'
    slug_url_kwarg='editSlug'
    fields= ('title','content','img','categories')
    def get_object(self):
        article=get_object_or_404(
            articlesModel,
            slug=self.kwargs.get('editSlug'),
            writer=self.request.user
        )
        return article
    def get_success_url(self):
        return reverse('description',kwargs={
            'descriptionSlug':self.get_object().slug
        })
        

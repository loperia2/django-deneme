from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import CreateView
from deneme.models import articlesModel
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
class addArticleView(LoginRequiredMixin,CreateView):
    login_url=reverse_lazy('login')
    template_name='pages/addArticle.html'
    model = articlesModel
    fields= ('title','content','img','categories')
    slug_url_kwarg='descriptionSlug'
    def get_success_url(self):
          return reverse('description', kwargs={
              'descriptionSlug': self.object.slug
          })

    def form_valid(self, form):
        article=form.save(commit=False)
        article.writer=self.request.user
        article.save()
        form.save_m2m()
        return redirect('homepage')

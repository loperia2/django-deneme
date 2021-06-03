from deneme.views.anasayfa import anasayfa
from django.urls import path
from deneme.views import deleteComment,contactView,anasayfa,categoryView, deleteComment,myarticles,Description,addArticleView,editArticleView,deleteArticleView
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path('directTo',RedirectView.as_view(
        url='https://www.google.com.tr'
    ),name='direcTo'),
    path('aboutMe',TemplateView.as_view(
        template_name='pages/aboutMe.html'
    ),name="aboutMe"),
    path('',anasayfa, name='homepage'),
    path('contact', contactView.as_view(), name='contact'),
    path('category/<slug:categorySlug>',categoryView.as_view(), name='category'),
    path('myarticles', myarticles , name='myarticles'),
    path('description/<slug:descriptionSlug>', Description.as_view(), name="description"),
    path('addArticle',addArticleView.as_view(), name='addArticle'),
    path('editArticle/<slug:editSlug>',editArticleView.as_view(), name='editArticle'),
    path('deleteArticle/<slug:deleteSlug>',deleteArticleView.as_view(), name='deleteArticle'),
    path('deleteComment/<int:id>',deleteComment, name='deleteComment'),
    path('email-sent',TemplateView.as_view(
        template_name='pages/emailSent.html'
    ),name='contactEmail')
]

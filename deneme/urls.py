from deneme.views.editArticle import editArticle
from deneme.models import articles
from deneme.views.anasayfa import anasayfa
from django.urls import path
from deneme.views import deleteComment,contact,anasayfa,category, deleteComment,myarticles,description,addArticle,editArticle,deleteArticle



urlpatterns = [
    path('',anasayfa, name='homepage'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myarticles', myarticles , name='myarticles'),
    path('description/<slug:descriptionSlug>', description, name="description"),
    path('addArticle',addArticle, name='addArticle'),
    path('editArticle/<slug:editSlug>',editArticle, name='editArticle'),
    path('deleteArticle/<slug:deleteSlug>',deleteArticle, name='deleteArticle'),
    path('deleteComment/<int:id>',deleteComment, name='deleteComment')
]

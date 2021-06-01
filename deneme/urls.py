from deneme.models import articles
from deneme.views.anasayfa import anasayfa
from django.urls import path
from deneme.views import comm,anasayfa,category,myarticles



urlpatterns = [
    path('',anasayfa, name='homepage'),
    path('comm', comm),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myarticles', myarticles , name='myarticles')
]

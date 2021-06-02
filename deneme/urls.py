from deneme.models import articles
from deneme.views.anasayfa import anasayfa
from django.urls import path
from deneme.views import contact,anasayfa,category,myarticles,description



urlpatterns = [
    path('',anasayfa, name='homepage'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myarticles', myarticles , name='myarticles'),
    path('description/<slug:descriptionSlug>', description, name="description")
]

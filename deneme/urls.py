from deneme.views.anasayfa import anasayfa
from django.urls import path
from deneme.views import comm,anasayfa



urlpatterns = [
    path('',anasayfa),
    path('comm', comm)
]

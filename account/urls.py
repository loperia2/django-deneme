from account.views.changePassword import changePassword
from django.urls import path
from account.views import makeLogOut,changePassword,editProfile

urlpatterns=[

    path('logout',makeLogOut,name='logout'),
    path('changePassword',changePassword, name='changePassword'),
    path('editProfile',editProfile,name='editProfile')

]
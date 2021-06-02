from account.views.changePassword import changePassword
from django.urls import path
from account.views import makeLogOut,changePassword,editProfile,regis
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login',auth_views.LoginView.as_view(
        template_name='pages/login.html',

    ),name='login'),
    path('logout',makeLogOut,name='logout'),
    path('changePassword',changePassword, name='changePassword'),
    path('editProfile',editProfile,name='editProfile'),
    path('regis',regis,name='regis')

]
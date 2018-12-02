from django.urls import path
from aplicativo import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Home, name='home'),
    url('login', views.Login, name='login'),
    url('login/auth', views.Auth, name='auth'),
]

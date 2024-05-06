from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('new/', views.home, name='create_user'),
    path('registro/', views.registro, name='registro'),
]
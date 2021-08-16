from . import views
from django.urls import path

urlpatterns = [
    path('',  views.user, name='user'),
    path('login',  views.login, name='login'),
    path('cproduct',  views.cproduct, name='cproduct'),
    path('create',  views.create, name='create'),
]
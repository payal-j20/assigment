from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('validate', views.chk,name='validate'),
    path('myfav', views.fav,name='fav'),
]

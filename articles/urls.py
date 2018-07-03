from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.article_list, name= 'list'),
    path('<slug>/',views.article_deatail,name = 'deatail'),
]

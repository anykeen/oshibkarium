from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    path('cards/<slug:slug>/', views.card, name='card_detail'),
    path('<slug:slug>/', views.page, name='page'),
    path('', views.index, name='index'),
]

from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('pest/<slug:slug>/', views.card, name='card_detail'),
    path('<slug:slug>/', views.page, name='page'),
    path('', views.index, name='index'),
    url(r'', include(('users.urls', 'users'), namespace='users')),
]

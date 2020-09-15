from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('stampalog/', views.cliche, name='cliche'),
    path('api/cliche/pos-vote/', views.pos_vote, name='pos_vote'),
    path('api/cliche/neg-vote/', views.neg_vote, name='neg_vote'),
]

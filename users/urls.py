from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterFormView.as_view(), name="register"),
    path('<slug:username>/', views.user, name='account'),
    path('<slug:username>/edit/', views.edit_profile, name='edit'),
    path('api/user/add-card/', views.card_add, name='card_add'),
    path('api/user/remove-card/', views.card_remove, name='card_remove'),
]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterFormView.as_view(), name="register"),
    path('<slug:username>/', views.user, name='account'),
    path('<slug:username>/edit/', views.edit_profile, name='edit')
]

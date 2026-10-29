from django.urls import path
from . import views

# str, а не slug: Django разрешает в логине точку, @, + и кириллицу,
# а slug их не пропускал — «Мои ошибки» у таких пользователей отдавали 404.
urlpatterns = [
    path('register/', views.UserRegisterFormView.as_view(), name="register"),
    path('<str:username>/', views.user, name='account'),
    path('<str:username>/edit/', views.edit_profile, name='edit'),
]

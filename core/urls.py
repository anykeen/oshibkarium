from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('pest/<slug:slug>/', views.card, name='card_detail'),
    path('<slug:slug>/', views.page, name='page'),
    path('', views.index, name='index'),
    path('api/request-editor/', views.editor_request, name='editor_request'),
    path('api/card/clarity-pos/', views.clarity_pos, name='clarity_pos'),
    path('api/card/clarity-neg/', views.clarity_neg, name='clarity_neg'),
    path('api/user/add-card-current/', user_views.card_add_current, name='card_add_current'),
    path('api/user/add-card-finish/', user_views.card_add_finish, name='card_add_finish'),
    path('api/user/remove-card/', user_views.card_remove, name='card_remove'),
]

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Вариант регистрации на базе класса FormView
class UserRegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "users/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] ) 
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(UserRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserRegisterFormView, self).form_invalid(form)


@login_required
def user(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/account.html', {'user': user})
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, UserFormEdit
from django.core.exceptions import PermissionDenied


class UserRegisterFormView(FormView):
    form_class = UserForm
    success_url = "/login/"
    template_name = "users/register.html"

    def form_valid(self, form):
        form.save()
        return super(UserRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserRegisterFormView, self).form_invalid(form)


@login_required
def user(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/account.html', {'username': username})


@login_required
@transaction.atomic
def edit_profile(request, username):
    if request.method == 'POST':
        user_form = UserFormEdit(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect(user, username=username)
        else:
            print('ololo')
    else:
        user_form = UserFormEdit(instance=request.user)
    print(user_form)
    return render(request, 'users/edit.html', {
        'user_form': user_form,
    })
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, View
from django.shortcuts import render, get_object_or_404
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

def edit_profile(request):
    user = User.objects.get(pk=request.user.pk)
    profile = user.profile
    #form = UserFormEdit(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            form = UserFormEdit(request.POST, instance=profile)

            if form.is_valid():
                update = form.save(commit=False)               
                update.user = user
                update.save()
            return HttpResponse('Профиль успешно отредактирован') 
        else:
            form = UserFormEdit()
        print(form)
        return render(request, "users/account.html", {'form': form})
    else:
        raise PermissionDenied
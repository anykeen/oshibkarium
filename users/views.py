from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, UserFormEdit
from django.core.exceptions import PermissionDenied
from core.models import Card, Category
from core.views import card_from_post
from django.views.decorators.csrf import csrf_exempt


class UserRegisterFormView(FormView):
    form_class = UserForm
    success_url = "/accounts/login/"
    template_name = "users/register.html"

    def form_valid(self, form):
        form.save()
        return super(UserRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserRegisterFormView, self).form_invalid(form)


@login_required
def user(request, username):
    user = get_object_or_404(User, username=username)
    cats = Category.objects.order_by('num')
    return render(request, 'users/account.html', {'username': username, 'cats': cats})


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
        user_form = UserFormEdit(instance=request.user)
    return render(request, 'users/edit.html', {
        'user_form': user_form,
    })


# У анонима нет profile — без этой проверки кнопки отдавали 500.
@csrf_exempt
def card_add_current(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    card = card_from_post(request)
    request.user.profile.finished.remove(card)
    request.user.profile.current.add(card)
    request.user.profile.save()

    return HttpResponse(status=204)

@csrf_exempt
def card_add_finish(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    card = card_from_post(request)
    request.user.profile.current.remove(card)
    request.user.profile.finished.add(card)
    request.user.profile.save()

    return HttpResponse(status=204)

@csrf_exempt
def card_remove(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    card = card_from_post(request)
    request.user.profile.current.remove(card)
    request.user.profile.finished.remove(card)
    request.user.profile.save()

    return HttpResponse(status=204)

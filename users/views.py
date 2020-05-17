from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, UserFormEdit
from django.core.exceptions import PermissionDenied
from core.models import Card, Category
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt


class UserRegisterFormView(FormView):
    form_class = UserForm
    success_url = "/accounts/login/"
    template_name = "users/register.html"

    def form_valid(self, form):
        form.save()
        email_subject = 'Добро пожаловать в Ошибкариум!'
        html_message = render_to_string('users/mail_template.html', {'username': form.cleaned_data.get('username')})
        plain_message = strip_tags(html_message)
        from_email = 'noreply@lapsus.timuroki.ink'
        to_email = form.cleaned_data.get('email')
        send_mail(email_subject, plain_message, 'noreply@lapsus.timuroki.ink', [to_email], html_message=html_message)
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
            print('')
    else:
        user_form = UserFormEdit(instance=request.user)
    print(user_form)
    return render(request, 'users/edit.html', {
        'user_form': user_form,
    })


@csrf_exempt
def card_add_current(request):
    card_id = request.POST.get('id')
    card = get_object_or_404(Card, id=card_id)
    request.user.profile.finished.remove(card)
    request.user.profile.current.add(card)
    request.user.profile.save()

    return render(request, 'core/card_detail.html')

@csrf_exempt
def card_add_finish(request):
    card_id = request.POST.get('id')
    card = get_object_or_404(Card, id=card_id)
    request.user.profile.current.remove(card)
    request.user.profile.finished.add(card)
    request.user.profile.save()

    return render(request, 'core/card_detail.html')

@csrf_exempt
def card_remove(request):
    card_id = request.POST.get('id')
    card = get_object_or_404(Card, id=card_id)
    request.user.profile.current.remove(card)
    request.user.profile.finished.remove(card)
    request.user.profile.save()

    return render(request, 'core/card_detail.html')
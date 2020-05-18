from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import ugettext_lazy as _

class UserForm(UserCreationForm):
    username = forms.RegexField(label=_("Пользовательский логин"), max_length=25, regex=r"^[a-zA-Z0-9_@\.\+\-]+$", help_text=_("Не более 25 символов, только латинские буквы, цифры и символы @ . + - _"),
    error_messages={
        'invalid': _("Может содержать только латинские буквы, цифры и символы @ . + - _")},
    widget=forms.TextInput(attrs={'required': 'true'}))
    email = forms.EmailField(label=_("Email"), max_length=200, widget=forms.EmailInput(attrs={'required': 'true'}))
    password1 = forms.CharField(label=_("Пароль"), help_text=_("Как минимум 8 символов, сочетайте и буквы, и цифры, избегайте дешевых трюков с qwerty и 123456 (советуем использовать спецсимволы)."),widget=forms.PasswordInput(attrs={'required': 'true',}))
    password2 = forms.CharField(label=_("Подтверждение пароля"),widget=forms.PasswordInput(attrs={'type': 'password','required': 'true',}),help_text=_("Для подтверждения введите, пожалуйста, пароль повторно."))
    is_subscribed = forms.BooleanField(label='Я не против получать рассылку про новых жителей и новые функции Ошибкариума', required=False, initial=True)
    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2', 'is_subscribed')

class UserFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('current', 'finished' )

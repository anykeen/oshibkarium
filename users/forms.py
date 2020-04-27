from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Обязательное поле')
    is_subscribed = forms.BooleanField(label='Я не против получать рассылку про новых жителей и новые функции Ошибкариума', required=False)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', 'is_subscribed')

class UserFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('current', 'finished' )

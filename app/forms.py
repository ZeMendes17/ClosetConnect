from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')



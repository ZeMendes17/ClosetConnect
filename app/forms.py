from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import User as DBUser
from .models import Product


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')


class UploadUserProfilePicture(forms.Form):
    image = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control',
               'id': 'image',
               'name': 'input_file',
               'accept': 'image/*'
               }
    ))


class UpdateProfile(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control',
               'style': 'resize: none; height: 100px;',
               'placeholder': 'Write something about yourself...'
               }))

class UpdatePassword(forms.Form):
    old_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_new_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']
        labels = {
            'name': 'Product name',
        }

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class RegistForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    description = forms.CharField(label='Description', max_length=100)
    image = forms.CharField(label='Image', max_length=100)


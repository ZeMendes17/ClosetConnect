from django import forms


class RegistForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    name = forms.CharField(label='Name', max_length=100)
    second_password = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput)



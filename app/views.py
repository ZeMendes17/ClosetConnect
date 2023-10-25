from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from app.forms import RegistForm

from app.models import User
from app.models import Product
from app.models import Comment
from app.models import Message


# Create your views here.


def index(request):
    ls = Product.objects.all()
    ts = {'products': ls}
    return render(request, 'index.html', ts)


def register(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            # Check if user already exists
            u = User.objects.filter(username=form.cleaned_data['username'])
            if u:
                return render(request, 'register.html', {'form': form, 'error': True})

            else:
                # Autenticate user
                user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password'))
                auth_login(request, user)

                # Create user
                user = User(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            name=form.cleaned_data['name'],

                            )
                user.save()
                return redirect('/index')
    else:
        form = RegistForm()
        return render(request, 'register.html', {'form': form, 'error': False})
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

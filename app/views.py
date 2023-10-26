from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from app.forms import RegisterForm
from django.contrib.auth.models import User as AuthUser

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
        form = RegisterForm(request.POST)
        print(form.errors)

        if form.is_valid():
            # Check if user already exists
            u = User.objects.filter(username=form.cleaned_data['username'])

            if u:
                return render(request, 'register.html', {'form': form, 'error': True})

            else:
                form.save()
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')

                # Authenticate user then login
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)

                # Create user in our database
                user = User.objects.create(username=username, email=email, password=raw_password, name=form.cleaned_data['name'])
                user.save()

                return redirect('index')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form, 'error': False})
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')



def profile_settings(request):
    # get user from database
    return render(request, 'profile_settings.html')

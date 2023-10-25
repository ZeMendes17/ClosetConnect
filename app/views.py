from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import LoginForm
from app.forms import RegistForm

from app.models import User
from app.models import Product
from app.models import Comment
from app.models import Message


# Create your views here.


def index(request):
    ls = Product.objects.all()
    ts = {'products': ls}
    return render(request, 'index.html')


def login(request):
    if not request.user.is_authenticated or request.user.username != 'admin':
        return redirect('/login')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = User.objects.filter(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
            if u:
                request.session['username'] = form.cleaned_data['username']
                return redirect('/index')
            else:
                return render(request, 'login.html', {'form': form, 'error': True})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form, 'error': False})
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

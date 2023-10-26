from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from app.forms import RegisterForm, UploadUserProfilePicture

from app.models import User, Product


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
                user = User.objects.create(username=username, email=email, password=raw_password,
                                           name=form.cleaned_data['name'])
                user.save()

                return redirect('/')
        else:
            return render(request, 'register.html', {'form': form, 'error': True})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form, 'error': False})


def explore(request):
    return render(request, 'explore.html')


@login_required(login_url='/login')
def profile_settings(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user.username)
        image_form = UploadUserProfilePicture()
        return render(request, 'profile_settings.html', {'user': user, 'image_form': image_form})

    elif request.method == 'POST' and 'image' in request.FILES:
        print("POST")
        user = User.objects.get(username=request.user.username)
        image_form = UploadUserProfilePicture(request.POST, request.FILES)
        if image_form.is_valid():
            file = request.FILES['image']

            if file:
                user.image = file
                user.save()
                print(user.image)
                return redirect('/account/settings')
        else:
            image_form = UploadUserProfilePicture()
            print(image_form.errors)
            return render(request, 'profile_settings.html', {'user': user, 'image_form': image_form})

    else:
        print(request)
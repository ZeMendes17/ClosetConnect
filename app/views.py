from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from app.forms import RegisterForm, UploadUserProfilePicture, UpdateProfile, UpdatePassword

from app.models import User, Product


# Create your views here.


def index(request):
    ls = Product.objects.all()
    try:
        user = User.objects.get(username=request.user.username)
        return render(request, 'index.html', {'user': user, 'products': ls})
    except User.DoesNotExist:
        return render(request, 'index.html', {'user': None, 'products': ls})


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
        profile_form = UpdateProfile(initial={'name': user.name, 'username': user.username, 'email': user.email,
                                              'description': user.description})
        password_form = UpdatePassword()
        return render(request, 'profile_settings.html', {'user': user, 'image_form': image_form,
                                                         'profile_form': profile_form, 'password_form': password_form})

    elif request.method == 'POST' and 'image' in request.FILES:
        print("POST")
        user = User.objects.get(username=request.user.username)
        image_form = UploadUserProfilePicture(request.POST, request.FILES)
        if image_form.is_valid():
            file = request.FILES['image']

            if file:
                user.image = file
                user.update_image(file)
                user.save()
                print(user.image)
                return redirect('/account/settings')
        else:
            image_form = UploadUserProfilePicture()
            print(image_form.errors)
            return render(request, 'profile_settings.html', {'user': user, 'image_form': image_form})

    elif request.method == 'POST' and 'profile_change' in request.POST:
        # get the form info
        user = User.objects.get(username=request.user.username)
        profile_form = UpdateProfile(request.POST)
        if profile_form.is_valid():
            if user.name != profile_form.cleaned_data['name']:
                user.name = profile_form.cleaned_data['name']
            if user.username != profile_form.cleaned_data['username']:
                user.username = profile_form.cleaned_data['username']
            if user.email != profile_form.cleaned_data['email']:
                user.email = profile_form.cleaned_data['email']
            if user.description != profile_form.cleaned_data['description']:
                user.description = profile_form.cleaned_data['description']
            user.save()
            # update user info auth
            request.user.username = profile_form.cleaned_data['username']
            request.user.email = profile_form.cleaned_data['email']
            request.user.save()
            return redirect('/account/settings')

    elif request.method == 'POST' and 'password_change' in request.POST:
        user = User.objects.get(username=request.user.username)
        password_form = UpdatePassword(request.POST)
        image_form = UploadUserProfilePicture()
        profile_form = UpdateProfile(initial={'name': user.name, 'username': user.username, 'email': user.email,
                                              'description': user.description})
        if password_form.is_valid():
            if user.password == password_form.cleaned_data['old_password']:
                if password_form.cleaned_data['new_password'] == password_form.cleaned_data['confirm_new_password']:
                    user.password = password_form.cleaned_data['new_password']
                    request.user.password = password_form.cleaned_data['new_password']
                    user.save()
                    print('Password changed successfully!')
                    return render(request, 'profile_settings.html', {'user': user, 'password_form': password_form,
                                                                     'image_form': image_form,
                                                                     'profile_form': profile_form,
                                                                     'success': 'Password changed successfully!'})
                else:
                    print('Passwords do not match!')
                    return render(request, 'profile_settings.html', {'user': user, 'password_form': password_form,
                                                                     'image_form': image_form,
                                                                     'profile_form': profile_form
                        , 'error': 'Passwords do not match!'})
            else:
                print('Wrong password!')
                return render(request, 'profile_settings.html', {'user': user, 'password_form': password_form,
                                                                 'image_form': image_form,
                                                                 'profile_form': profile_form
                    , 'error': 'Wrong password!'})
        else:
            return render(request, 'profile_settings.html', {'user': user, 'password_form': password_form,
                                                             'image_form': image_form,
                                                             'profile_form': profile_form,
                                                             'error': 'Invalid form!'})
    elif request.method == 'POST' and 'delete_account' in request.POST:
        user = User.objects.get(username=request.user.username)
        request.user.delete()
        user.delete()
        return redirect('/login')

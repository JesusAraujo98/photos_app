from http import client
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Profile, Client
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from users.forms import ProfileForm

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def clients_views(request):
    user = request.user
    clients = Client.objects.filter(pk=user)
    
    



@login_required
def my_profile_view(request):
    return render(request, 'users/user.html')


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formTwo':
            
            u_name = request.POST['username']
            u_password = request.POST['password']
            x='hola'
    
            user = authenticate(request, username= u_name, password = u_password)
            if user:
                login(request, user)

                # return redirect('posts:albums')
                return redirect(reverse('posts:album', ))
            else:
                return render(request, 'users/login.html', {'error': 'invalid username and/or password'})

        elif request.POST.get("form_type") == 'formOne':
            
            s_name = request.POST['username_signup']
            s_password = request.POST['password_signup']
            s_email = request.POST['email_signup']

            # EMAIL VALIDATION
            u = User.objects.filter(email=s_email)
            if u:
                error = f'There is another account using {s_email}'
                return render(request, 'users/login.html', {'error': error})
            
            # USERNAME VALIDATION 

            try:
                user = User.objects.create_user(username= s_name, password = s_password)
                user.email = s_email
                user.save()
                profile = Profile(user = user)
                profile.email = s_email
                profile.save()
                return redirect('users:login')
                
            except IntegrityError:
                return render(request, 'users/login.html', {'error': 'Username is already in use'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


def index_view(request):
    return redirect('users:login')
 
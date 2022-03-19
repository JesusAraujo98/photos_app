from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User

# Create your views here.
def login_view(request):

    if request.method == 'POST':
    
        u_name = request.POST['username']
        u_password = request.POST['password']

        user = authenticate(request, username= u_name, password = u_password)
        if user:
            user_id = user.id
            login(request, user)
            return redirect(reverse('posts:album', args=(u_name,) ))
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and/or password'})
            

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')



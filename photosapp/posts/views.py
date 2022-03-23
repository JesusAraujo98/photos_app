from django.shortcuts import render
from .models import Album, Photos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
@login_required
def album_views(request, u_name):
    # album_list= Album.objects.filter()
    profile = request.user.profile
    email = profile.email

    
    album_list = Album.objects.filter(user=profile)


    return render(request, 'posts/albums.html', {
        'album_list': album_list,
        'email': email,
    }) 


 
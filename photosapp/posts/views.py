from django.shortcuts import render
from .models import Album, Photos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlbumForm


# Create your views here.
@login_required
def album_view(request, u_name):
    profile = request.user.profile
    album_list = Album.objects.filter(user=profile)
    return render(request, 'posts/albums.html', {
        'album_list': album_list,
    }) 

@login_required
def add_album_view(request):

    if request.method == 'POST':
        user= request.user.profile
        album= Album()
        album.album_name = request.POST['album_name']
        album.album_client = request.POST['client_name']
        album.cover_photo = request.POST['picture']
        album.user = user
        album.thumbnail_image()
        album.save()

    return render(request, 'posts/new_album.html', {
         
    })


# def add_album(request):
#     if request.method == 'POST':
#         a_name = request.POST['a_name']
#         a_client = request.POST['a_client']
#         a_cover_photo = request.POST['a_cover_photo']
#         album = Album.objects.create_album(album)


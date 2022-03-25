import profile
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
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            user= request.user.profile
            
            data = form.cleaned_data
            album = Album()
            album.user = user
            album.album_name = data['album_name']
            album.album_client = data['album_client']
            album.cover_photo = data['cover_photo']
            album.save()

    else:
        form = AlbumForm()

    return render(
        request= request, 
        template_name = 'posts/new_album.html', 
        context = {
            'profile': request.user.profile,
            'user': request.user,
            'form': form,
        })


def edit_album_view(request, album_name ):

    if request.method == 'POST':
        user = request.user
        
        


    return render(request, 'posts/edit_album.html')



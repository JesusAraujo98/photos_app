# import profile
from django.shortcuts import redirect, render
from .models import Album, Photos
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlbumForm
from django.urls import reverse


# Create your views here.


# def folders_view(request):
#     if request.method == 'POST':
#         user = request.user.profile
        
@login_required
def folders_view(request):
    user = request.user
    album_list = Album.objects.filter(user=user).order_by('-created_at')
    
    pass

@login_required
def update_album_view(request):
    if request.method == 'POST':
        album_id = request.POST['album_id']
        album = Album.objects.get(pk=album_id)
        name_album = request.POST['album_name']
        client_album = request.POST['album_client']
        cover_album = request.POST['album_cover']
        
        photos_album = request.FILES.getlist('photos')
        user= request.user

        for photo in photos_album:
            new_photo = Photos()
            new_photo.album = album
            new_photo.image=photo
            new_photo.save()

        return redirect(reverse('posts:album', ))
       

@login_required
def photos_view(request):
    if request.method == 'POST':
        seleccion = request.POST['selected_album']

        album_state = Album.objects.get(pk=seleccion)
        if album_state.is_active == True:
            photos_list = Photos.objects.filter(album=seleccion)
            return render(request, 'posts/photos.html', {
            'photos_list':photos_list,
            'album_id':seleccion
            })
        else:
            return render(request, 'posts/album.html', {
            'photos_list':photos_list
            })
    print('*******')
    

@login_required
def album_view(request):
    user = request.user
    first_list = Album.objects.filter(user=user).order_by('-created_at')
    album_list = []
    if len(first_list)>=5:
        for i in range(0,5):
            album_list.append(first_list[i])
    else:
        album_list=first_list
        
    
    return render(request, 'posts/albums.html', {
        'album_list': album_list,
        
    }) 


@login_required
def add_album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            user= request.user
            data = form.cleaned_data
            album = Album()
            album.user = user
            album.album_name = data['album_name']
            album.album_client = data['album_client']
            album.cover_photo = data['cover_photo']
            album.save()
            return redirect(reverse('posts:album', ))
    else:
        form = AlbumForm()
    return render(
        request= request, 
        template_name = 'posts/new_album.html', 
        context = {
            'profile': request.user,
            'user': request.user,
            'form': form,
        })





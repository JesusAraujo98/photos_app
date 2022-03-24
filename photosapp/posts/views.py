from django.shortcuts import render
from .models import Album, Photos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
@login_required
def album_views(request, u_name):
    profile = request.user.profile
    

    
    album_list = Album.objects.filter(user=profile)


    return render(request, 'posts/albums.html', {
        'album_list': album_list,
        
    }) 


# def add_album(request):
#     if request.method == 'POST':
#         data = request.POST
#         images = request.POST.get('images')

#         if 
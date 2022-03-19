from django.shortcuts import render
from .models import Album, Photos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
@login_required
def album_views(request, user_name):
    # album_list= Album.objects.filter()
    return HttpResponse(f'este es el usuario {user_name}')


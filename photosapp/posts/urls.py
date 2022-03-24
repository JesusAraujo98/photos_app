from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve 

app_name= 'posts'
urlpatterns = [
    path('<u_name>', views.album_views, name='album'),
]

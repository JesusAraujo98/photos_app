from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve 

app_name= 'posts'
urlpatterns = [
    path('', views.album_view, name='album'),
    path('new_album/', views.add_album_view, name='add_album'),
    path('photos/', views.photos_view, name='photos'),
    path('update/', views.update_album_view, name='update'),
    path('albums/', views.folders_view, name='folders'),

]

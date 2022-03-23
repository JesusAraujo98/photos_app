from django.urls import path
from . import views

app_name= 'posts'
urlpatterns = [
    path('<u_name>', views.album_views, name='album'),
]
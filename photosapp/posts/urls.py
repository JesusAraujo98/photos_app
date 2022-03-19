from django.urls import path
from . import views

app_name= 'posts'
urlpatterns = [
    path('<user_name>', views.album_views, name='album'),
]
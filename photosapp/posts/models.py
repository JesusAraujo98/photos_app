from django.db import models

from users.models import Profile

# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    album_client = models.CharField(max_length=200 , blank=True)
    album_name= models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(blank=True)
    



class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    image = models.ImageField(blank=True)
    preview = models.ImageField(blank=True)
    


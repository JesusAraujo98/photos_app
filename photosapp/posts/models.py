from distutils.command.upload import upload
from django.db import models

from users.models import Profile

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    album_client = models.CharField(max_length=200 , blank=True)
    album_name= models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(blank=True, upload_to='posts/albums')
    
    thumbnail_image = ImageSpecField(
        source='cover_photo', 
        processors=[ResizeToFill(500, 300)],
        format = 'JPEG',
        options={'quality': 60})
    



class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    image = models.ImageField(blank=True, upload_to='posts/photos')
    preview = models.ImageField(blank=True)
    


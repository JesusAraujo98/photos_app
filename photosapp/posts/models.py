from distutils.command.upload import upload
from secrets import choice
from turtle import back
from django.db import models

from users.models import Profile, User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    """ Choices part """

    # CHOICES_color = [
    #     ('coffe', 'coffe'),
    #     ('black', 'black'),
    #     ('white', 'white'),
    #     ('gray' (
    #         ('gray', '25-75'),
    #         ('gray', '50-50'),
    #         ('gray', '75-20'),
    #     ))
    #     ]
    # CHOICES_grid = [
    #     ('mosaico','mosaico'),
    #     ('cuadrados','cuadrados')
    #     ('album','album')
    # ]
    
    
    # background_color = models.Choices(choices = CHOICES_color)
    # grid = models.Choices(choices = CHOICES_grid)

    



class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    image = models.ImageField(blank=True, upload_to='posts/photos')
    thumbnail_photo = ImageSpecField(
        source='image', 
        processors=[ResizeToFill(500, 700)],
        format = 'JPEG',
        options={'quality': 60})
    


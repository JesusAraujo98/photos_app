from django.db import models

# Create your models here.


class Album(models.Model):
    user = models.IntegerField()
    album_name= models.CharField(max_length=100)

    created_at = models.DateTimeField()



class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    image = models.ImageField(blank=True)
    preview = models.ImageField(blank=True)
    


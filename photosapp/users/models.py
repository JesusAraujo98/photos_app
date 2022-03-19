from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    email = models.EmailField()
    phone = models.IntegerField()
    
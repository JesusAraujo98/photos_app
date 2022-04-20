from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =models.CharField(max_length=50, blank=True)
    last_name =models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    
    phone_number = models.CharField(max_length=20, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    User._meta.get_field('email')._unique = True

    def __str__(self):
        return self.user.username
    
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    client_name = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)


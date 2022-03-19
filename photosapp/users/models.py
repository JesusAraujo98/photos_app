from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    phone = models.IntegerField()
    User._meta.get_field('email')._unique =True

    def __str__(self):
        return self.user.username
    
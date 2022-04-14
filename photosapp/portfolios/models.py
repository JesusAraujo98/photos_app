from random import choices
from unicodedata import category
from django.db import models
from django.contrib.postgres.fields import ArrayField

from users.models import User

# Create your models here.

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    choices_categories = [
        ('wedding', 'wedding'),
        ('nature', 'nature'),
        ('budoir', 'budoir'),
        ('night', 'night'),
        ('sport', 'sport'),
        ('fashion', 'fashion'),
        ('art', 'art'),
        ('landscape ', 'landscape '),
        ('portrait', 'portrait'),
    ]

    choices = ArrayField(
    models.CharField(choices=choices_categories, max_length=5, blank=True),
    )


# Generated by Django 4.0.3 on 2022-03-25 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_album_cover_photo_alter_photos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='preview',
        ),
    ]

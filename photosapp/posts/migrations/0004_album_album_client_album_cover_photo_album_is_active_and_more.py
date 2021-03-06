# Generated by Django 4.0.3 on 2022-03-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_album_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_client',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='album',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-19 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
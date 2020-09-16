# Generated by Django 2.2.4 on 2020-07-03 17:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trading', '0009_friend_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend_list',
            name='friend_name',
        ),
        migrations.AddField(
            model_name='friend_list',
            name='friend_name',
            field=models.ManyToManyField(max_length=100, related_name='list', to=settings.AUTH_USER_MODEL),
        ),
    ]
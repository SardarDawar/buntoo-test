from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import math
import ckeditor
# import User model that already comes with Django

class advert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500,blank=True)
    linked = models.URLField(blank=True)
    img = models.ImageField(blank=True,upload_to='ad_images')
    video = models.FileField(blank=True,upload_to='ad_videos')
    active = models.BooleanField(default=False)
    start = models.BigIntegerField(default=0)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Friend_List(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    friend_name = models.ManyToManyField(User,related_name='list')

    def __str__(self):
        return self.user.username

# Create your models here.
class Post(models.Model):
    # title = models.CharField(max_length=254)
    img = models.ImageField(blank=True,upload_to='post_images')
    video = models.FileField(blank=True,upload_to='post_videos')
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    
    def __str__(self):
        return self.author.username

    def time_since_posted(self):
        now = timezone.now()

        diff = now - self.date_posted

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

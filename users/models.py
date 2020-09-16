from django.db import models
from django.utils import timezone
# import User model that already comes with Django
from django.contrib.auth.models import User
from trading.models import Friend_List
from PIL import Image

# Create your models here.


class Trading(models.Model):
    name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

# extend django's Users model and add any other fields you want to it


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ForeignKey(Friend_List , on_delete= models.CASCADE , blank=True , null = True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        ''' Overrides the save method on the parent class so we can resize an image before saving it. '''
        super(Profile, self).save(*args, **kwargs)

        with Image.open(self.image.path) as img:
            rgb_img = img.convert('RGB')
            # resize the image
            if rgb_img.height > 300 or rgb_img.width > 300:
                output_size = (300, 300)
                rgb_img.thumbnail(output_size)
                rgb_img.save(self.image.path)

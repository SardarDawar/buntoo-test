from django.contrib import admin
from .models import Trading #Import the model
from .models import Profile

# Register your models here.
admin.site.register(Trading)
admin.site.register(Profile)

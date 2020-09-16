from rest_framework import serializers
from .models import *
from users.models import *
from django.contrib.auth.models import User




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id","user", "friends","image")
    

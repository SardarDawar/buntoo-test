from rest_framework import serializers
from .models import *
from users.models import *
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id","user", "friends","image")
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend_List
        fields = '__all__'
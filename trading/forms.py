from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['date_posted','author']

class advertform(forms.ModelForm):
    class Meta:
        model = advert
        fields = ['content','linked','img','video']
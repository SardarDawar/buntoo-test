from rest_framework import routers
from trading import views as myapp_views
from django.urls import path,include

router = routers.DefaultRouter()


router.register(r'profile', myapp_views.ProfileViewset),
router.register(r'post', myapp_views.PostViewset),
router.register(r'add_friend', myapp_views.FriendViewset),



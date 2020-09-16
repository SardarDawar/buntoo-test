"""bfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports from Django-provided stuff
from django.contrib import admin
from django.urls import path, include
# import a default Django view for login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,re_path
# Imports from apps you've created
from users import views as user_views
from .api import router
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('register/', user_views.register, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='users/profile.html'), name="login"),
    path('login/', user_views.login, name="login"),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('logout/', user_views.logout, name='logout'),
    path('profile/', user_views.user_profile, name="user_profile"),
    url(r'^Userprofile/(?P<user>\w+)/$', user_views.profile, name="Userprofile"),
       #password Reset URLS.............
    path('password_reset/', PasswordResetView.as_view(), name='password_reset' ),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
      ####################..............
    path('', include('trading.urls')),
    path('', include('chat.urls')),
    path('api/v1/', include(router.urls)),
    re_path('api/(?P<version>(v1|v2))/', include('trading.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Buntoo Admin Panel"

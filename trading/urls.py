from django.urls import path, include
from . import views
from chat import views as view

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home_page, name='home_page'),
    path('post_form/', views.PostView, name='post_form'),
    path('search/', views.search, name='search'),
    path('Friendlist/', views.Friendlist, name='Friendlist'),
    path('adevertise/', views.adView, name='ad_form'),
    #path('ad-dash', views.addash, name='ad_dash'),
    path('count-clicks/<int:id>', views.countclick, name='count-click'),
    path('chat/', view.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', view.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>', view.message_list, name='message-detail'),
    path('api/messages', view.message_list, name='message-list'),
    path('api/users/<int:pk>', view.user_list, name='user-detail'),
    path('api/users', view.user_list, name='user-list'),
    ######## REST API URLS #########################
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/register/', include('rest_auth.registration.urls')),
]



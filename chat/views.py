from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message, UserProfile
from chat.serializers import MessageSerializer, UserSerializer
from rest_framework.response import Response
from users.models import Profile
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

@csrf_exempt
def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:
            users = User.objects.filter(id=pk)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.create_user(username=data['username'], password=data['password'])
            UserProfile.objects.create(user=user)
            return JsonResponse(data, status=201)
        except Exception:
            return JsonResponse({'error': "Something went wrong"}, status=400)


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver) | Message.objects.filter(sender_id=receiver, receiver_id=sender)
        for message in messages:
            message.is_read = True
            message.save()
        print(messages)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(data = {"messages": serializer.data}, status = 200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            data['sender'] = User.objects.get(id=int(data['sender']))
        except:
            return JsonResponse(data={'message': 'User does not exisit'}, status=404)
        try:
            data['receiver'] = User.objects.get(id=int(data['receiver']))
        except:
            return JsonResponse(data={'message': 'User does not exisit'}, status=404)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




def chat_view(request):
    username = None
    if request.method == 'POST':
        username =request.POST.get('username')
        print(username)
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "GET" and username==None:
        return render(request, 'chat/chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})
    else:
        return render(request, 'chat/chat.html',
                      {'user': User.objects.get(username=username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
        
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})

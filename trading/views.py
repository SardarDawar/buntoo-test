from django.shortcuts import render, redirect
from .models import *  # import model so you can display the data in a view
from users.models import *
from django.contrib import messages
# import stops user from accessing routes if their not logged in
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from .models import Post , advert
from django.contrib.auth.models import User
from .forms import PostForm , advertform
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import json
import time
import random
#payment gateway
from bfinder import settings
import stripe
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

# Landing Page
def landing_page(request):
    # if the user is logged in and tries to access '' route (landing_page), redirect to users home content page
    if request.user.is_authenticated:
        return redirect('home_page')
    # render html from templates folder
    return render(request, 'trading/landing-page.html')

from itertools import chain
# Home Page (Newsfeed, whatever, main content NOT THE USER PROFILE)
# a built-in decorator that requires the user to be logged in to access this view
@login_required
def home_page(request):
    #######################################
    test_ads()
    user_list = []
    for i in User.objects.all():
        user_list.append(i.username)
    user_list_json=json.dumps(user_list)
    userzero = User.objects.all()[0]

    ########### Post Form #################
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        if not request.POST.get('content') and not request.FILES.get('img') and not request.FILES.get('video'):
            messages.warning(request, "Information: Empty posts are not allowed.")
            return redirect('home_page')

        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            form.save()
            new.save()
            return redirect('landing_page')

    #######################################
    current = []
    current_user = Post.objects.filter(author=request.user)
    for i in current_user:
        current.append(i)
    posts = []
    user_profile = Profile.objects.get(user=request.user)
    try:
        friends = user_profile.friends.friend_name.all() 
        
        for i in friends:
            posts.append(Post.objects.filter(author=i).order_by('-date_posted'))
        posts_sorted=[]
        for i in posts:
            for j in i:
                posts_sorted.append(j) 
    except :
           posts=[]
           posts_sorted=[]
 

    for i in current_user:
        posts_sorted.append(i)

    posts = sorted(list(chain(posts_sorted)),key= lambda instance:instance.date_posted)[::-1]
    all_ads = advert.objects.all()
    alist = {}

    count = 0

    for i in posts:
        if count == 8:
            try:
                alist['a'+str(len(alist))] = all_ads[random.randint(0,len(all_ads)-1)]
            except:
                alist['p'+str(len(alist))] = i
            count = 0
        else:
            alist['p'+str(len(alist))] = i
            count = count + 1
    
    blist = []
    clist = []
    for i,j in alist.items():
        clist.append(j)
        if i[0] == 'a':
            blist.append(True)
        else:
            blist.append(False)
    empty = -1
    if not blist and not clist:
        empty = 1 

    context = {
        'posts': zip(blist,clist),
        'users': User.objects.all() ,
        'user_list_json': user_list_json,
        'userzero':userzero,
        'form':form,
        'empty': empty,
    }

    return render(request, 'trading/home.html', context)



@login_required
def PostView(request):
      ######################################
    test_ads()
    ######################################
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            form.save()
            new.save()
            return redirect('landing_page')
    try:
        ad = advert.objects.all()[random.randint(0,len(advert.objects.all())-1)]
    except:
        ad = advert.objects.all()

    context = {
        'form':form,
        'user_list_json':user_list_json,
        'userzero':userzero,
        'ad':ad
    }
     
    return render(request,'trading/post.html',context)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def search(request):
       ######################################
    user_list = []
    for i in User.objects.all():
        user_list.append(i.username)
    user_list_json=json.dumps(user_list)
    userzero = User.objects.all()[0]

    ######################################
    query=request.POST.get('query',None)
    user=User.objects.all()
    if query is not None:
        user=user.filter(
        Q(username__icontains=query)
        )
    try:
        friend_list = Friend_List.objects.get(user=request.user).friend_name.all(),
    except ObjectDoesNotExist:
        friend_list = None


    ############################################
    action = request.POST.get('action')

    if action:
        ids= request.POST.get('id')
        print(ids)
        name = User.objects.get(id=ids)
        try:
            instance=Friend_List.objects.get(user=request.user)
            instance.friend_name.add(name)
        except ObjectDoesNotExist:
            instance=Friend_List.objects.create(user=request.user)
            pro=Profile.objects.get(user=request.user)
            pro.friends=instance
            pro.save()
        
            print('success')
            instance.friend_name.add(name)
   

    ################################################


    context={
        'friend_list':friend_list,
        'user':user,
        'query':query,
        'user_list_json':user_list_json,
        'userzero':userzero
    }

    return render(request,'trading/search.html',context)



@login_required
def Friendlist(request):
     ######################################
    user_list = []
    for i in User.objects.all():
        user_list.append(i.username)
    user_list_json=json.dumps(user_list)
    userzero = User.objects.all()[0]


    ######################################
    ids= request.POST.get('id')
    # print(ids)
    name = User.objects.get(id=ids)
    try:
        instance=Friend_List.objects.get(user=request.user)
        instance.friend_name.add(name)
    except ObjectDoesNotExist:
        instance=Friend_List.objects.create(user=request.user)
        pro=Profile.objects.get(user=request.user)
        pro.friends=instance
        pro.save()
     
        print('success')
        instance.friend_name.add(name)

    context = {
      'name':name,
      'user_list_json':user_list_json,
      'userzero':userzero
    }
     
    return render(request,'trading/Added.html',context)


@login_required
def adView(request):
      ######################################
    user_list = []
    for i in User.objects.all():
        user_list.append(i.username)
    user_list_json=json.dumps(user_list)
    userzero = User.objects.all()[0]

    ######################################
    form = advertform()
    if request.method == 'POST':
        form = advertform(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.start = time.time()
            form.save()
            new.save()
            try:
                charge = stripe.Charge.create(
                    amount='1500',
                    currency='usd',
                    description='Payment For Add',
                    source=request.POST['stripeToken']
                )
            except:
                objs = advert.objects.last()
                objs.delete()
            return redirect('/')

    context = {
        'form':form,
        'user_list_json':user_list_json,
        'userzero':userzero

    }
     
    return render(request,'trading/advert.html',context)


def test_ads():
    adslist = advert.objects.all()
    a = (60 * 60) * 24
    for i in adslist:
        if (time.time()-i.start) >= a:
            i.delete()
    return

@login_required
def addash(request):
    user_list = []
    for i in User.objects.all():
        user_list.append(i.username)
    user_list_json=json.dumps(user_list)
    userzero = User.objects.all()[0]

    ######################################

    objs = advert.objects.filter(author=request.user)


    context = {
        'ads':objs,
        'user_list_json':user_list_json,
        'userzero':userzero

    }
     
    return render(request,'trading/dash.html',context)

@login_required
def countclick(request,id):
    obj = advert.objects.get(pk=id)
    obj.clicks = obj.clicks + 1
    obj.save()
    return redirect(obj.linked)



########################## REST API VIEWS ##############################
from .serializers import *
from rest_framework import viewsets
class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
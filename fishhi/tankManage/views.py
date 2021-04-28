from django.shortcuts import render,redirect
import os, sys, urllib.request, json , requests, random
from bs4 import BeautifulSoup
from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse,Http404
import tankManage.views
import account.views
import base64,datetime
from .models import Feed, Timeline, Fish, Plant, Supplies
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required

# Create your views here.
def tankcalc(request):
    # if request.GET.get['width'] ==
    tankWidth = request.GET.get('width','' )
    tankHeight = request.GET.get('height','' )
    tankDepth = request.GET.get('depth','' )
    tankWeight = request.GET.get('weight','' )
    tankSand = request.GET.get('sand','' )
    waterLevel = request.GET.get('water','')

    javascript_key = os.environ["JAVASCRIPT_KEY"]
    context = {
        'tankWidth':tankWidth,
        'tankHeight':tankHeight,
        'tankDepth':tankDepth,
        'tankWeight':tankWeight,
        'tankSand':tankSand,
        'waterLevel':waterLevel,
        'javascript_key': javascript_key,
    }
    return render(request, 'tankcalc.html', context)

def list(request,keyword):
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=50&sort=sim" # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    requests = urllib.request.Request(url)
    requests.add_header("X-Naver-Client-Id",client_id)
    requests.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(requests)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print( response_body)

        # getJson= json.loads(response_body.decode('utf-8'))
        
        # print(getJson)
        # for item in getJson:
        #     print(item["title"])
    else:
        print("Error Code:" + rescode)
    
    return HttpResponse(response_body, content_type="text/json-comment-filtered")

def search(request):
    keyword = request.GET.get('keyword','' )
    return render(request, 'search.html' , {'keyword':keyword, 'blog':blog_feed(3)})

def feed(request):
    return render(request, 'feed.html',{'blog':blog_feed(10)})

def blog_feed(n):
    print(n)
    pwd = os.path.dirname(__file__)
    with open(pwd + '/blog.json') as f:
        blog = json.load(f)
    # print(blog)
    return blog[:n]

def test(request):
    feed = Feed.objects.create(title='test')
    Timeline.objects.create(content_object=feed, title="mythic")
    return render(request,"index.html")
def add_fish(request,pid):
    feed_fish_id = Feed.objects.get(id=pid)

    if feed_fish_id.username == request.user:
        if request.method == "POST":
            name = request.POST['name']
            hmf = request.POST['hmf']
            price = request.POST['price']
            sex = request.POST['sex']
            username = request.user
            if hmf == '':
                hmf = 0
            if request.POST['get'] != '':
                get = datetime.datetime.strptime(request.POST['get'],"%Y-%m-%d").date()
            else:
                get = None
            if request.FILES:
                img = request.FILES['img']
            else:
                img = None
            Fishes = Fish.objects.create(username=username, name=name, feed_fish_id=feed_fish_id, img=img, sex=sex,hmf=hmf,get=get,price=price)
            data ='성공'
            Timeline.objects.create(content_object=feed_fish_id , title= name + "봉달")
    else:
        data = '본인의 어항이 아닙니다.'
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")
def add_plant(request,pid):
    feed_plant_id = Feed.objects.get(id=pid)

    if feed_plant_id.username == request.user:
        if request.method == "POST":
            name = request.POST['name']
            price = request.POST['price']
            username = request.user
            if request.POST['get'] != '':
                get = datetime.datetime.strptime(request.POST['get'],"%Y-%m-%d").date()
            else:
                get = None
            if request.FILES:
                img = request.FILES['img']
            else:
                img = None
            Plants = Plant.objects.create(username=username, name=name, feed_plant_id=feed_plant_id, img=img,get=get,price=price)
            data ='성공'
            Timeline.objects.create(content_object=feed_plant_id , title= name + "봉달")
    else:
        data = '본인의 어항이 아닙니다.'
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

def add_supplies(request,pid):
    feed_supplies_id = Feed.objects.get(id=pid)

    if feed_supplies_id.username == request.user:
        if request.method == "POST":
            name = request.POST['name']
            price = request.POST['price']
            username = request.user
            if request.POST['get'] != '':
                get = datetime.datetime.strptime(request.POST['get'],"%Y-%m-%d").date()
            else:
                get = None
            if request.FILES:
                img = request.FILES['img']
            else:
                img = None
            supplies = Supplies.objects.create(username=username, name=name, feed_supplies_id=feed_supplies_id, img=img,get=get,price=price)
            data ='성공'
            Timeline.objects.create(content_object=feed_supplies_id , title= name + "봉달")
    else:
        data = '본인의 어항이 아닙니다.'
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

def create_fishtank(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['contents']
        public = request.POST['public']
        changewater = request.POST['changewater']
        if request.POST['start'] != '':
            start = datetime.datetime.strptime(request.POST['start'],"%Y-%m-%d").date()
        else:
            start = None

        if public == 'true' :
            public = True
        else:
            public = False
        if request.FILES :
            thumbnail = request.FILES['thumbnail']
        else:
            thumbnail = None
        username = request.user

        Feeds = Feed.objects.create(title=title, username=username, contents=content, public=public,thumbnail=thumbnail,changewater=changewater,start=start)

        if Feeds.thumbnail:
            thumbnail = Feeds.thumbnail.url
        else:
            thumbnail = None
        data = {
            'title':title,
            'content':content,
            'Fid':Feeds.id,
            'public':public,
            'thumbnail':thumbnail,
            'changewater':changewater,
            'start':start,
            
        }
        
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

    # title = request.POST.get('title')
    # content = erquest.POST.get('content')
    # username = request.user

    # Feed.objects.create(title=title, username=username, contents=content)
    # print(request.method)
def fishtank(request,pid):
    try:
        fishtank = Feed.objects.get(id=pid)
    except Feed.DoesNotExist:
        raise Http404("Does not exist!")
    today = datetime.date.today()
    fishes = Fish.objects.all().filter(feed_fish_id=pid) 
    plants = Plant.objects.all().filter(feed_plant_id=pid) 
    supplies = Supplies.objects.all().filter(feed_supplies_id=pid) 

    return render(request, 'fishtank.html',{'fishtank':fishtank,"fishes":fishes,"plants":plants, "supplies":supplies,"today":today,"pid":pid})

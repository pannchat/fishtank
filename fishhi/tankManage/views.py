from django.shortcuts import render
import os
import sys
import urllib.request
import json
import requests,random
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import tankManage.views
import json
# Create your views here.
def index(request):
    # if request.GET.get['width'] ==
    tankWidth = request.GET.get('width','' )
    tankHeight = request.GET.get('height','' )
    tankDepth = request.GET.get('depth','' )
    tankWeight = request.GET.get('weight','' )
    tankSand = request.GET.get('sand','' )
    waterLevel = request.GET.get('water','')

    javascript_key = os.environ["JAVASCRIPT_KEY"]

    return render(request, 'index.html',{
        'tankWidth':tankWidth,
        'tankHeight':tankHeight,
        'tankDepth':tankDepth,
        'tankWeight':tankWeight,
        'tankSand':tankSand,
        'waterLevel':waterLevel,
        'javascript_key': javascript_key,
        })

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

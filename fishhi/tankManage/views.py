from django.shortcuts import render
import os
import sys
import urllib.request
import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    return render(request, 'search.html')

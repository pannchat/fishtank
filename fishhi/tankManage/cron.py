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

import json
from collections import OrderedDict



def blog_crwall():
    file_data = OrderedDict()
    blog = []
    blog_list=[
        { 'id':'kjmvhzl', 'category':'70', 'p_category':'70' },
        { 'id':'j2541833', 'category':'8', 'p_category':'' },
        { 'id':'cheo5474', 'category':'1', 'p_category':'1' },
        { 'id':'song6374', 'category':'74', 'p_category':'' },
        # { 'id':'p_min0', 'category':'39', 'p_category':'' },
        # { 'id':'p_min0', 'category':'41', 'p_category':'' },
        ]

    for i in blog_list:


        url = 'https://blog.naver.com/PostList.nhn?blogId=' + i.get('id') + '&categoryNo='+i.get('category')
        if i.get('p_category') != '':
            url += '&parentCategoryNo=' + i.get('p_category')
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            #PostThumbnailAlbumViewArea > ul > li:nth-child(1) > a > div.area_thumb > img
            #PostThumbnailAlbumViewArea > ul > li:nth-child(1) > a > div.area_text > strong
            for i in range(1,len(soup.select('#PostThumbnailAlbumViewArea > ul > li'))+1):
                if(soup.select_one('#PostThumbnailAlbumViewArea > ul > li:nth-child('+ str(i) +') > a > div.area_thumb > img') != None):
                    link = 'http://blog.naver.com/'+ soup.select_one('#PostThumbnailAlbumViewArea > ul > li:nth-child('+ str(i) +') > a ').get('href')
                    title = soup.select_one('#PostThumbnailAlbumViewArea > ul > li:nth-child('+ str(i) +') > a > div.area_text > strong').text
                    img = soup.select_one('#PostThumbnailAlbumViewArea > ul > li:nth-child('+ str(i) +') > a > div.area_thumb > img').get('src')
                    # print(link)
                blog.append({'link':link,'img':img,'title':title })
                
    random.shuffle(blog)
    file_data = blog
    print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    with open('blog.json','w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
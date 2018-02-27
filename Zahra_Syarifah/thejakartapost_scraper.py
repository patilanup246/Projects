# -*- coding: utf-8 -*-
'''
Created on 27-Jan-2018

@author: Administrator
'''
import requests, csv, os
from pyquery import PyQuery
from selenium import webdriver
from glob import glob


output_f = open('final_csv.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Date','Title','Article','Link','Topics'])
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': "trctestcookie=ok; trctestcookie=ok; __cfduid=d0fdc9b69ba40f79786e31650bac20b011517044330; _ga=GA1.2.883317505.1517044335; _gid=GA1.2.1426464245.1517044336; __auc=5cf1914516136e384fe8e449e52; trctestcookie=ok; __asc=54e64e3516140f659b0b7d9803c; _gat_UA-8353993-1=1; tjp=true; XSRF-TOKEN=eyJpdiI6IllkM1wvSFNTZ1hmaFFDV3R5S0pcLzd1QT09IiwidmFsdWUiOiJjQWNGK1RiZzF2MDRIQ0ZzTVhUbk1xZ1FTaEVzblRvZmtnQmJuZVRkMDRqY3FYWUFaaStORXVlV1k1ZWhOdWhWdUQ1cXVBdDR6VVp1ZExyVnlTcTRpZz09IiwibWFjIjoiZjhmOWUwMTk2MTVkZmI5ZDUyNTQ3MWIyY2VhNDgyOGEwYjRlZjlhMDRmMzE1YzJjNjM2ODQxNjFmN2U1ZjU4ZiJ9; laravel_session=eyJpdiI6IjVlY1RSMTRpTHFpZkFvaU00c2tcLzJBPT0iLCJ2YWx1ZSI6ImZhT090UUdMaHYyTk1kZGdpOFBldnRXaGJGdzZEYW5LdW5VWmZYa2ZWUVc3ZFJ6NGZmZExQMTh6OGw2d2hHc3VUYjVZT1hKejRUQ0crVHlTeVlvcERBPT0iLCJtYWMiOiI3ZTkyZDAyNzUyZGY3ZWI3MDc1OGMzMGIyMTc4NDdhYzgxYjZmOTRhNTA5YzU5YzM4ZGJjODNhN2RhZDRjMDM1In0%3D",
    'Host': "www.thejakartapost.com",
    'Pragma': "no-cache",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }



for u in open('thejakartaposturls.txt',encoding='utf-8').read().split('\n'):
#for u in ['http://www.thejakartapost.com/news/2018/01/27/ri-weave-inclusive-thread-pakistan.html']:
    #u = 'http://www.thejakartapost.com/news/2018/01/27/ri-weave-inclusive-thread-pakistan.html'
    try:
        print (u)
        r = requests.get(u, headers=headers).text
        
        pq = PyQuery(r)
        
        details = []
        
        details.append(pq('[class="day"]').text())
        details.append(pq('[class="title-large"]').text())
        details.append(pq('.show-define-text').text())
        print (len(pq('.show-define-text').text()))
        details.append(u)
        details.append(pq('[class="topicBottom"] li a').text())
        
        wr.writerow(details)
    except Exception as e:
        print (e)
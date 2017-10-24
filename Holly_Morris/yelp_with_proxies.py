# -*- coding: utf-8 -*-
'''
Created on 24-Oct-2017

@author: Administrator
'''
from pyquery import PyQuery
import requests
import urllib


proxy_list = [
    '35.161.5.60:3128',
'195.154.163.181:3128',
'74.208.182.99:8888',
'216.56.48.118:9000',
'45.6.216.66:3128',
'137.74.163.137:3128',
'35.161.196.69:3128',
'149.255.154.4:8080',
'94.177.175.232:3128',
'51.254.104.103:3128',
'89.236.17.106:3128',
'202.62.12.174:53281',
'210.54.213.130:53281',
'110.77.208.186:52305',
'77.104.250.236:53281',
'181.112.226.122:8080',
'115.167.78.141:53281',
'119.42.94.27:52335',
'110.78.148.237:52335',
'203.123.229.38:53281',
]

http_proxy  = "http://do-ex-us-sf-4.northghost.com:443"
https_proxy = "https://35.161.5.60:3128"
ftp_proxy   = "ftp://do-ex-us-sf-4.northghost.com:443"



f_output = open('output_urls.txt','w',encoding='utf-8')
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }
proxyDict = { 
              #"http"  : "http://"+, 
              "https" : "https://"+proxy_list[0], 
              #"ftp"   : ftp_proxy
            }
count = 0
new_proxy_count = 0
for url in open('input_urls',encoding='utf-8').read().split('\n'):
    
    if count == 1000:
        new_proxy_count+=1
        proxyDict = { 
              #"http"  : "http://"+, 
              "https" : "https://"+proxy_list[new_proxy_count], 
              #"ftp"   : ftp_proxy
            }
        count = 0
    
    r = requests.get(url, headers=headers, proxies=proxyDict)
    pq = PyQuery(r.text)
    a = ''
    try:
        a = urllib.parse.unquote(urllib.parse.unquote((pq('.biz-website a').attr('href')))).replace('/biz_redir?url=','').split('&')[0].split('/')
        a = '/'.join(a[:3])
    except Exception as e:
        print (e)
    if a:
        f_output.write(a+'\n')
        f_output.flush()
        print (a)
    else:
        f_output.write(''+'\n')
        f_output.flush()
        print ()
        
    count+=1
        
        
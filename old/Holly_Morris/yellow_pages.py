'''
Created on 06-Nov-2017

@author: Administrator
'''

locations = open('location_list.txt').read().split('\n')


import requests
from pyquery import PyQuery
import time

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "www.yellowpages.com",
    'pragma': "no-cache",
    'referer': "https://www.yellowpages.com/search?search_terms=fitness&geo_location_terms=Holtsville%2C+NY",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }
output = open('output.txt','w')
for l in locations:
    page = 1
    while True:
        response = requests.request("GET", 'https://www.yellowpages.com/search?search_terms=fitness&geo_location_terms={}&page={}'.format(l,str(page)), headers=headers)

        pq = PyQuery(response.text)
        print (l +'\t'+ str(page))
        if not len(pq('[class="info"]')):
            break
        for p in pq('[class="info"] h2 a'):
            output.write(l+'\t'+p.attrib['href']+'\n') 
            output.flush()
        
        time.sleep(10)
        
        page+=1
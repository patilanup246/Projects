'''
Created on 08-Oct-2017

@author: Administrator
'''
import requests
import os
import urllib.request
from pyquery import PyQuery
from time import gmtime, strftime

site_name = 'shufersal'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'http://prices.shufersal.co.il/?page='
resp1 = requests.get(starting_url)
pq1 = PyQuery(resp1.text)
 
max_num = int (pq1('tr td a:nth-child(6)').attr('href').split('&')[0].split('=')[1]) + 1
gz_list = []
page_num = 1
while page_num < max_num:
    resp = requests.get(starting_url+str(page_num))
    print (starting_url+str(page_num))
    pq = PyQuery(resp.text)
    
    if len(pq('tbody td a')) == 0:
        break
    
    for g in pq('tbody tr'):
        name_link = str(pq(g)('td:nth-child(7)').text()).lower()
        if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link:
            print (name_link)
            urllib.request.urlretrieve (pq(g)('td a').attr('href'), site_name+'/'+name_link+'.gz')
    page_num+=1
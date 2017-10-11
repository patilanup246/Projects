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

gz_list = []
page_num = 1
while True:
    resp = requests.get(starting_url+str(page_num))
    pq = PyQuery(resp.text)
    
    if len(pq('tbody td a')) == 0:
        break
    
    for g in pq('tbody tr'):
        print (pq(g)('td:nth-child(7)').text()+'.gz')
        urllib.request.urlretrieve (pq(g)('td a').attr('href'), site_name+'/'+pq(g)('td:nth-child(7)').text()+'.gz')
    page_num+=1
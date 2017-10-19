'''
Created on 10-Oct-2017

@author: Administrator
'''
import requests
import os
import urllib.request
from pyquery import PyQuery
from time import gmtime, strftime

site_name = 'mega_retail'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'http://publishprice.mega.co.il/'
r_main = requests.get(starting_url).text
pq = PyQuery(r_main)
#print (r_main)
gz_list = []
page_num = 1
fold = pq('table tr td:nth-child(1) a')[1]
print (fold.attrib['href'])
print (starting_url+fold.attrib['href'])

p = PyQuery(requests.get(starting_url+fold.attrib['href']).text)
for gz in p('table tr td:nth-child(1) a'):
    print (starting_url+'/'+fold.attrib['href']+'/'+gz.attrib['href'])
    if not gz.attrib['href'] == '/':
        if 'promofull' in gz.attrib['href'].lower() or 'pricefull' in gz.attrib['href'].lower() or 'stores' in gz.attrib['href'].lower():
            urllib.request.urlretrieve (starting_url+'/'+fold.attrib['href']+'/'+gz.attrib['href'], site_name+'/'+gz.attrib['href'])

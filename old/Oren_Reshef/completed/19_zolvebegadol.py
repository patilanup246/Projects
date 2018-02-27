'''
Created on 10-Oct-2017

@author: Administrator
'''
import requests
import os
import urllib.request
from pyquery import PyQuery
from time import gmtime, strftime

site_name = 'zolvebegadol'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'http://zolvebegadol.com/'
r_main = requests.get(starting_url+'?C=M&O=D').text
pq = PyQuery(r_main)
#print (r_main)
gz_list = []
page_num = 1
for fold in pq('table tr td a'):
    print (fold.attrib['href'])
    print (starting_url+fold.attrib['href'])
    
    p = PyQuery(requests.get(starting_url+fold.attrib['href'].split('?')[0]+'/gz/').text)
    for gz in p('table tr td a'):
        name_link = gz.attrib['href'].lower()
        if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link:
            print (starting_url+'/'+fold.attrib['href']+'/gz/'+gz.attrib['href'])
            try:
                if not gz.attrib['href'] == '/':
                    urllib.request.urlretrieve (starting_url+'/'+fold.attrib['href'].split('?')[0]+'/gz/'+gz.attrib['href'], site_name+'/'+gz.attrib['href'])
            except Exception as e:
                pass
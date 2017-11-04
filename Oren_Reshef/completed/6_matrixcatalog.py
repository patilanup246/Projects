# -*- coding: utf-8 -*-
'''
Created on 08-Oct-2017

@author: Administrator
'''
import requests
import os
import urllib.request
from pyquery import PyQuery
import selenium
from selenium import webdriver
import time 
from time import gmtime, strftime

site_name = 'Matrix_Catalog'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'http://matrixcatalog.co.il/NBCompetitionRegulations.aspx'



        
r = requests.get(starting_url).text
pq = PyQuery(r)
#time.sleep(10)
for g in pq('table tr'):
    try:
        print (pq(g)('td a').attr('href'))
        name_link =  str(pq(g)('td a').attr('href')).lower()
        print (name_link)
        if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link:
            urllib.request.urlretrieve ('http://matrixcatalog.co.il/'+pq(g)('td a').attr('href'), site_name+'/'+pq(g)('td:nth-child(2)').text()+'_'+pq(g)('td:nth-child(1)').text())
        
    #time.sleep(10)
    except Exception as e:
        print (e)
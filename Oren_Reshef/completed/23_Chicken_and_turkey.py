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

site_name = 'Chicken_abd_turkey'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'http://prices.super-bareket.co.il/'



        
r = requests.get(starting_url).text
pq = PyQuery(r)
#time.sleep(10)
for g in pq('.Promofull.allFile a'):
    try:

        print (g.text)
        urllib.request.urlretrieve ('http://prices.super-bareket.co.il//'+g.attrib['href'], site_name+'/'+g.text)
        
    #time.sleep(10)
    except Exception as e:
        print (e)
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

site_name = 'Kings_Store'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'https://www.kingstore.co.il/Food_Law/MainIO_Hok.aspx?WStore=0&WDate=&WFileType=4'



        
r = requests.get(starting_url).json()

for g in r:
    try:
        if g['TypeExpFile'] == 'gz':
            print (g['FileNm'])
            urllib.request.urlretrieve ('https://www.kingstore.co.il/Food_Law/Download/'+g['FileNm'], site_name+'/'+g['FileNm'])
        
    except Exception as e:
        print (e)
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

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()+'\\'+site_name,'profile.default_content_setting_values.automatic_downloads': 1}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get(starting_url)

driver.find_element_by_id('filterBtn').click()    
time.sleep(10) 

all_links = driver.find_elements_by_css_selector('.allFile a')
promofull = 0
pricefull = 0
stores = 0
for link in all_links:
    
    if 'promofull' in link.text.lower() and promofull == 0:
        print (link.text)
        urllib.request.urlretrieve (link.get_attribute('href'), site_name+'/'+link.text)
        promofull= 1
    if 'pricefull' in link.text.lower() and pricefull == 0:
        print (link.text)
        urllib.request.urlretrieve (link.get_attribute('href'), site_name+'/'+link.text)
        pricefull = 1
    if 'stores' in link.text.lower() and stores == 0:
        print (link.text)
        urllib.request.urlretrieve (link.get_attribute('href'), site_name+'/'+link.text)
        stores = 1
        
    if promofull == 1 and pricefull == 1 and stores == 1:
        break
    

driver.quit()
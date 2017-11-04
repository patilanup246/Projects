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

site_name = 'Super_Pharm'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'http://prices.super-pharm.co.il/?type=&date=&page='


page_num = 1
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()+'\\'+site_name,'profile.default_content_setting_values.automatic_downloads': 1}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
try:
    while True:
        
        driver.get(starting_url+str(page_num))
        
        if len(driver.find_elements_by_css_selector('table tr')) == 0:
            break
        
        #time.sleep(10)
        for g in driver.find_elements_by_css_selector('table tr'):
            try:
                name_link = g.find_element_by_css_selector('td:nth-child(2)').text.lower()
                if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link:
                    driver.execute_script("arguments[0].click();", g.find_element_by_css_selector('td a'))
            except Exception as e:
                print (e)
        time.sleep(60)
        page_num+=1
finally:
    driver.quit()

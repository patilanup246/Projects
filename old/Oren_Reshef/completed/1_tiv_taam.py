# -*- coding: utf-8 -*-
'''
Created on 09-Oct-2017

@author: Administrator
'''
import requests
import os
import urllib.request
from pyquery import PyQuery
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
from time import gmtime, strftime

site_name = 'tiv_taam'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass

username = 'TivTaam'
password = ''

starting_url = 'https://url.publishedprices.co.il/login'


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()+'\\'+site_name}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

try:
    driver.get(starting_url)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('login-button').click()
    
    
    link_container = []
    
    while True:
        
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.f")))

        links = driver.find_elements_by_css_selector('a.f')
        
        for l in links:
            try:
                link_container.append (l.get_attribute("href"))
                #print (l.get_attribute("href"))
            except Exception as e:
                print (e)
        try:
            driver.find_element_by_css_selector('.paginate_button.next.disabled')
            break
        except Exception as e:
            driver.execute_script("$('#fileList_next').click()")
            time.sleep(3)
            print (e)
    

    for l in link_container:
        name_link = str(l).lower().split('/')[-1]
        if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link:
            print (name_link)
            if not '.xml' in name_link:  
                driver.get(l)
                
            else:
                driver.get(l)
                try:
                    with open(site_name+'/'+name_link, 'w', encoding='utf-8') as f:
                        f.write(str(driver.find_element_by_css_selector('#webkit-xml-viewer-source-xml').get_attribute('innerHTML')))

                except Exception as e:
                    print(e)
            
    
    
finally:
    time.sleep(100)
    driver.quit()
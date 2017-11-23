# -*- coding: utf-8 -*-
'''
Created on 22-Nov-2017

@author: Administrator
'''
from selenium import webdriver
import time
profile = webdriver.FirefoxProfile()
profile.set_preference("privacy.trackingprotection.enabled", False)
driver = webdriver.Firefox()
output_firefox_file = open('output_firefox_file','w',encoding='utf-8')
for c in open('companies.txt').read().split('\n'):
    driver.get('https://www.linkedin.com/company/'+str(c))
    time.sleep(1)
    name = ''
    address = ''
    size = ''
    website = ''
    founded = ''
    
    try:
        name = (driver.find_element_by_css_selector('[class="name"] span').text)
    except Exception as e:
        pass
    
    try:
        address = (driver.find_element_by_css_selector('[itemprop="address"]').text)
    except Exception as e:
        pass
    
    try:
        size = (driver.find_element_by_css_selector('[class="company-size"] p').text)
    except Exception as e:
        pass
    
    try:
        website = (driver.find_element_by_css_selector('[class="website"] a').text)
    except Exception as e:
        pass
    
    try:
        founded = (driver.find_element_by_css_selector('[class="founded"] p').text)
    except Exception as e:
        pass

    print (name+'\t'+address+'\t'+size+'\t'+website+'\t'+founded+'\n')
    
    output_firefox_file.write(name+'\t'+address+'\t'+size+'\t'+website+'\t'+founded+'\n')
    output_firefox_file.flush()
    
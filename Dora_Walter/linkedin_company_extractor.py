# -*- coding: utf-8 -*-
'''
Created on 24-Oct-2017

@author: Administrator
'''
import requests
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
#chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--no-sandbox")
#chromeOptions.add_extension('anticaptcha.crx')
chromeOptions.add_argument("--disable-setuid-sandbox")
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chromeOptions)

driver.get('https://www.linkedin.com/sales/')



driver.find_element_by_id('session_key-login').send_keys('kumar.jan08@gmail.com')
driver.find_element_by_id('session_password-login').send_keys('sindhu007')

driver.find_element_by_id('btn-primary').click()

time.sleep(10)
output_f = open('linkedin_sales_nav_output','w',encoding='utf-8')
for comp_id in open('linkedin_sales_nav_input').read().split('\n'):
    driver.get('https://www.linkedin.com/sales/accounts/insights?companyId='+str(comp_id))
    time.sleep(5)
    output = str(comp_id)+'\t'
    
    try:
        output += driver.find_element_by_css_selector('.acct-name').text+'\t'
    except:
        output += '\t'
        
    try:
        output += driver.find_element_by_css_selector('.location.detail').text+'\t'
    except Exception as e:
        #print (e)
        output += '\t'
        
    try:
        output += driver.find_element_by_css_selector('.size.detail').text+'\t'
    except:
        output += '\t'
    
    try:
        output += driver.find_element_by_css_selector('.industry.detail').text+'\t'
    except:
        output += '\t'    
    
    try:
        output += driver.find_element_by_css_selector('.account-term-desc.addr-term-desc').text+'\t'
    except:
        output += '\t'
    
    try:
        output += driver.find_element_by_css_selector('.account-term:nth-child(3) p a').text+'\n'
    except Exception as e:
        output += '\n'
    print (output)
    output_f.write(output)
    output_f.flush()
    time.sleep(25)
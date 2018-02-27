# -*- coding: utf-8 -*-
import urllib.parse
from selenium import webdriver
from openpyxl import load_workbook
import time
import sqlite3
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--no-sandbox")
#chromeOptions.add_extension('anticaptcha.crx')
chromeOptions.add_argument("--disable-setuid-sandbox")
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chromeOptions)
# profile = webdriver.FirefoxProfile()
# profile.set_preference("privacy.trackingprotection.enabled", False)
# driver = webdriver.Firefox()
#driver = webdriver.Chrome(chrome_options=chromeOptions)
# driver.get('chrome-extension://neodgnejhhhlcdoglifbmioajmagpeci/options.html')
# driver.find_element_by_id('auto_submit_form').click()
# driver.find_element_by_name('account_key').send_keys('5f6b75f0738a1bd09cf717392c9804a3')
# driver.find_element_by_id('save').click()

#driver.get('https://www.google.nl')

time.sleep(10)


input_f = open('googling_input',encoding='utf-8').read().split('\n')
output_f = open('googling_output','w',encoding='utf-8')

output_firefox_file = open('output_firefox_file','w',encoding='utf-8')

for row in input_f:
    print (row)
    #time.sleep(1)
    output_f.write(row+'\t')
    output_f.flush()
    try:
        driver.get('https://www.bing.com/search?q='+ urllib.parse.quote(str(row), safe=''))
        driver.find_element_by_css_selector('h2 a').click()
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
         
        try:
            output_f.write(str(driver.find_element_by_css_selector('[class="b_algo"] cite').text)+'\n')
        except:
            output_f.write('\n')
         
        output_f.flush()
        
    except Exception as e:
        pass



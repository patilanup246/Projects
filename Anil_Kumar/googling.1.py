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
driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe',chrome_options=chromeOptions)
#driver = webdriver.Chrome(chrome_options=chromeOptions)
# driver.get('chrome-extension://neodgnejhhhlcdoglifbmioajmagpeci/options.html')
# driver.find_element_by_id('auto_submit_form').click()
# driver.find_element_by_name('account_key').send_keys('5f6b75f0738a1bd09cf717392c9804a3')
# driver.find_element_by_id('save').click()

driver.get('https://www.google.nl')




input_f = open('googling_input',encoding='utf-8').read().split('\n')
output_f = open('googling_output','w',encoding='utf-8')



for row in input_f:
    print (row)
    #time.sleep(1)
    output_f.write(row+'\t')
    output_f.flush()
    try:
        driver.get('https://www.google.nl/search?q='+ urllib.parse.quote(str(row), safe=''))
        time.sleep(1)
        #driver.find_element_by_css_selector('.gsfi[title="Search"]').send_keys(Keys.RETURN)
        #time.sleep(2)
        try:
            output_f.write(str(driver.find_element_by_css_selector('[class="_Rm"]').text)+'\t')
            #print (a)
            #output_f.write(a)
            #output_f.flush()
        except Exception as e:
            print (e)
            output_f.write('\t')
        
        try:
            output_f.write(str(driver.find_element_by_css_selector('span._Xbe._ZWk.kno-fv [data-dtype="d3ph"] span').text)+'\t')
        except:
            output_f.write('\t')
         
        try:
            output_f.write(str(driver.find_element_by_css_selector('._b1m.kp-hc a.ab_button[role="button"]').get_attribute('href'))+'\t')
        except:
            output_f.write('\t')
         
        try:
            output_f.write(str(driver.find_element_by_css_selector('[class="_Xbe"]').text)+'\n')
        except:
            output_f.write('\n')
         
        output_f.flush()
        
    except Exception as e:
        pass



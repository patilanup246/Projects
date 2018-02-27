'''
Created on 10-Nov-2017

@author: Administrator
'''
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
output_file = open('output.txt','w', newline='',encoding='utf-8')
for i in range(1,200):
    driver.get('https://es.aliexpress.com/premium/category/204000419/{}.html?site=esp&g=y&SortType=total_tranpro_desc&tc=ppc&tag=&needQuery=n&isFreeShip=y'.format(str(i)))
    for i in range(1,10):
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(5)
    for l in driver.find_elements_by_css_selector('.list-item'):
        output_file.write (str(l.find_element_by_css_selector('.atc-product-id').get_attribute('value'))+'\t')
        output_file.write (str(l.find_element_by_css_selector('.product ').get_attribute('title'))+'\t')
        output_file.write (str(l.find_element_by_css_selector('[itemprop="price"]').text)+'\t')
        output_file.write (str(l.find_element_by_css_selector('[class="pic"] img').get_attribute('src'))+'\t')
        output_file.write (str(l.find_element_by_css_selector('.product').get_attribute('href'))+'\n')
        output_file.flush()
    
        
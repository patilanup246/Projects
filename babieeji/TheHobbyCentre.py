# -*- coding: utf-8 -*-
'''
Created on Aug 13, 2018

@author: talib
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import csv
# from openpyxl.reader.excel import load_workbook
# 
# 
# 
# 
# all_result = []
# output = open('thehobbycentre.csv','w', newline='')
# WR = csv.writer(output, quoting=csv.QUOTE_ALL)
# WR.writerow(['title', 'duration', 'content', 'date', 'hall_value', 'learn_more_link'])


driver = webdriver.Chrome()
driver.get('http://thehobbycenter.org/index.php?q=node/133')
# all_shows= []

# image = driver.find_element_by_css_selector('[class="image image-thumbnail "]')
# title = driver.find_elements_by_css_selector('[class="views-field-title"]')
# duration = driver.find_elements_by_css_selector('[class="views-field-field-duration-value"]')
# date = driver.find_elements_by_css_selector('[class="date-display-single"]')
# hall_value = driver.find_elements_by_css_selector('[class="views-field-field-hall-value"]')
# learn_more_link = driver.find_elements_by_css_selector('[class="views-field-field-learn-url"] a')
for l in learn_more_link:
    print (l.get_attribute('href'))
content = driver.find_elements_by_css_selector('[class="field-content"]')



# for t in title:
#     print(t.text)
#     
# for d in duration:
#     print(d.text)
#     
# 
#     
# for x in date:
#     print(x.text)    
#     
# for h in hall_value:
#     print(h.text)

for c in content:
    print(c.text)  
    
    
# print(title, duration, content, date, hall_value)

# print(image.get_attribute('src'))


for a in driver.find_elements_by_css_selector('.views-row'):
    print (a.find_element_by_css_selector('views-field-field-duration-value').text)
    print (a.find_element_by_css_selector('views-field-field-duration-value').text)

time.sleep(5)
driver.quit()
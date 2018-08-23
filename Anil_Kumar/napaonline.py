import requests
from pyquery import PyQuery
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import csv
import time
#driver = webdriver.Chrome()

# output_f = open('napaonline.csv','w',encoding='utf-8', newline='')
# wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
# #wr.writerow(['Product Type',    'Quantity',    'Collection',    'Vendor',    'Tags',    'meta descr',    'meta title',    'H1',    'SKU',    'Name',    'Category',    'Fitment',    'Fitment HTMl',    'URL',    'Price',    'Features',    'Features HTML',    'Details',    'Details HTMl',    'H2',    'Images',    'Option: 1',    'Option: 2',    'Option: 3'])


# import webbrowser
# o = open('napaonline_links.txt').read().split('\n')
# i = 1
# 
# #     driver.get(a)
# #     try:
# #         WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id^="map_canvas"]')))
# #         t = driver.find_element_by_css_selector('[id^="map_canvas"]').get_attribute('data-stores')
# #         y = json.loads(t)
# #         print (y)
# #         details = []
# #         
# #         details.append(y['name'])
# #         details.append(y['address'])
# #         details.append(y['url'])
# #         details.append(y['latitude'])
# #         details.append(y['longitude'])
# #         
# #         wr.writerow(details)
# #         time.sleep(30)
# #     except Exception as e:
# #         print (e)
# for a in o:
#     if i%15 ==0 :
#         time.sleep(30)
#     webbrowser.open_new_tab('https://napaonline.com/en'+a)
#     i+=1

output_f = open('napaonline.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
import glob
i = 0
for a in glob.glob("C:\\Users\\talib\\Downloads\\html\\*.html"):
    print (i)
    i+=1
    try:
        pq = PyQuery(open(a).read())
        details = []
        y = json.loads(pq('[id^="map_canvas"]').attr('data-stores'))
        details.append(y['name'])
        details.append(y['address'])
        details.append(y['url'])
        details.append(y['latitude'])
        details.append(y['longitude'])
        details.append(pq('.store-detail-listing .store-listing-hours').text())
         
        wr.writerow(details)
        #print (details)
    except Exception as e:
        print (e)


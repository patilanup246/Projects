# -*- coding: utf-8 -*-
'''
Created on 07-Feb-2018

@author: Administrator
'''
import requests, csv, os
from pyquery import PyQuery
from selenium import webdriver
from glob import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import json
from selenium.webdriver.support.ui import Select
import time
#driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})
DRIVER = webdriver.Chrome(chrome_options=chrome_options)

output_f = open('ricochetoffroad.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Product Type',    'Quantity',    'Collection',    'Vendor',    'Tags',    'meta descr',    'meta title',    'H1',    'SKU',    'Name',    'Category',    'Fitment',    'Fitment HTMl',    'URL',    'Price',    'Features',    'Features HTML',    'Details',    'Details HTMl',    'H2',    'Images',    'Option: 1',    'Option: 2',    'Option: 3'])


  
def get_products_links():
    i = 1
    products = []
    while True:
        r = requests.get('https://ricochetoffroad.com/search?page={}&q=%2A'.format(str(i))).text
        time.sleep(5)
        pq = PyQuery(r)
        i+=1
        
        for p in pq('[class="product-content"] a'):
            print (p.attrib['href'])
            products.append('https://ricochetoffroad.com'+p.attrib['href'])
        
        if len(pq('[class="product-content"] a')) == 0:
            break
        break
    return products
      



#85323
for product in list(set(get_products_links())):
    r = requests.get(product).text
    time.sleep(1)
    pq = PyQuery(r)
    print ('Scraping : '+product)
    description_data =  (pq('[itemprop="description"]').text().split('\n'))
    fitment = ''
    for d in description_data:
        #print (d)
        if 'fits' in d.lower() or 'available for' in d.lower() or 'kits available for' in d.lower():
            fitment =  d
            break
    
    try:
        details = []
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        
        details.append('<h1>'+pq('[itemprop="name"]').text()+'</h1>')
        details.append(pq('[itemprop="description"] p em').text())
        details.append(pq('[itemprop="name"]').text())
        details.append('UTV Accessories')
        details.append(fitment)
        details.append(fitment)
        details.append(product)
        p1 = ''
        try:
            DRIVER.delete_all_cookies()
            DRIVER.get(product)
            p1 = DRIVER.find_element_by_css_selector('[id="productPrice"]').text.replace('$ ','').replace(',','')
            DRIVER.execute_script('$(\'[id="addToCart"]\').click()')
            time.sleep(3)
            DRIVER.get('https://ricochetoffroad.com/cart')
            select = Select(DRIVER.find_element_by_id('address_province'))
            select.select_by_visible_text('Arizona')
            DRIVER.find_element_by_css_selector('[id="address_zip"]').send_keys('85338')
            DRIVER.execute_script('$(\'[value="Calculate shipping"]\').click()')
            time.sleep(3)
            DRIVER.get('https://ricochetoffroad.com/cart/async_shipping_rates')
            prices = []
            
            for h in json.loads(DRIVER.find_element_by_css_selector('pre').text)['shipping_rates']:
                prices.append(float(h['price']))
        except Exception as e:
            print (e)
            
        
        
        
        details.append(float(p1)+min(prices))
        details.append('')
        details.append('')
        
        details.append(pq('[id="descrip"]').text())
        details.append(pq('[id="descrip"]').html())
        details.append('<h2>'+pq('[itemprop="name"]').text()+'</h2>')
        images = []
        for i in pq('[class="swiper-img"]'):
            images.append('https:'+i.attrib['src'])
        
        details.append(', '.join(images))
        
        for o in pq('[class="selector-wrapper"]'):
            #print (pq(o)('label').text())
            options = []
            for oo in pq(o)('select option'):
                options.append(oo.text)
            
            details.append(pq(o)('label').text() + ' : '+', '.join(options))
        
        wr.writerow(details)
        #print (details)
    except Exception as e:
        print (e)
            
DRIVER.quit()
    
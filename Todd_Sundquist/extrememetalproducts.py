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
#driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')
DRIVER = webdriver.Chrome()

output_f = open('extrememetalproducts.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Product Type',    'Quantity',    'Collection',    'Vendor',    'Tags',    'meta descr',    'meta title',    'H1',    'SKU',    'Name',    'Category',    'Fitment',    'Fitment HTMl',    'URL',    'Price',    'Features',    'Features HTML',    'Details',    'Details HTMl',    'H2',    'Images',    'Option: 1',    'Option: 2',    'Option: 3'])

r_all = requests.get('http://extrememetalproducts.com').text
pq_all = PyQuery(r_all)
categories = []
for m in pq_all('[class="main-nav"] a'):
    if not '#' in m.attrib['href']:
        categories.append('http://extrememetalproducts.com/'+m.attrib['href'])
  
categories = list(set(categories))
  
# categories = [
#                 'http://extrememetalproducts.com/c-711904-utv-parts-accessories.html',
#                 'http://extrememetalproducts.com/c-765988-tractor-compact-trackhoe.html',
#                 'http://extrememetalproducts.com/c-766015-4wd-accessories-rock-crawler.html',
#                 'http://extrememetalproducts.com/c-1136678-best-sellers.html',
#                 'http://extrememetalproducts.com/c-645776-featured-products.html',
#                 'http://extrememetalproducts.com/c-765973-motorcycle-accessories.html',
#                 'http://extrememetalproducts.com/c-766010-snowmobile.html'
#               ]
products = []
for cat in categories:
    #print ('Getting Items from : '+cat)
    i = 1
    while True:
        url = cat.split('-')
        url[1] = url[1]+'.'+str(i)
        r = requests.get('-'.join(url)).text
        pq = PyQuery(r)
          
        if len(pq('#wsm-prod-list-view .wsm-cat-title a')):
            print ('Getting Items from : '+cat+'\t'+str(pq('.wsm-cat-prod-innerwrapper .wsm-cat-pagination-top .wsm-cat-pag-prodcount').text()))
            for h in pq('#wsm-prod-list-view .wsm-cat-title a'):
                products.append (h.attrib['href'])
        else:
            break
        i+=1
      
print (len(list(set(products))))


#85323
for product in list(set(products)):
    
    print ('Scraping : '+product)
    try:
        details = []
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        details.append('')
        
        shipping = 0.00
        try:
            DRIVER.get(product)
            DRIVER.find_element_by_css_selector('.wsm-addtocart-button').click()
            DRIVER.find_element_by_css_selector('.wsm_cart_shipping_tool_input').send_keys('85323')
            DRIVER.find_element_by_css_selector('.wsm_interface_cart_shipping_tool_button').click()
            
            element = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#wsm_cart_shipping_tool_rate_list li")))
            DRIVER.find_elements_by_css_selector('#wsm_cart_shipping_tool_rate_list li')
            for e in DRIVER.find_elements_by_css_selector('#wsm_cart_shipping_tool_rate_list li'):
                if 'FedEx Ground Home Delivery' in e.text:
                    shipping =  float(e.text.split(' - ')[0].replace('$',''))
                    break
        except:
            pass
        DRIVER.delete_all_cookies()
        
        r = requests.get(product)
        pq = PyQuery(r.text)
        
        details.append('<h1>'+pq('[itemprop="name"]').text()+'</h1>')
        details.append(pq('#wsm-prod-info [class="wsm-prod-sku"]').text())
        details.append(pq('[itemprop="name"]').text())
        details.append('UTV Accessories')
        details.append(pq('#wsm-prod-tab-details [class="productInfo"]').text())
        details.append(pq('#wsm-prod-tab-details [class="productInfo"]').html())

        details.append(product)
        price = float(pq('[itemprop="price"]').text().strip().replace('$',''))
        if shipping:
            details.append('$'+str(price+shipping))
        else:
            details.append(str(price))
        details.append('')
        details.append('')
        details.append(pq('#wsm-prod-tab-decrip .wsm-prod-tab-content').text())
        details.append(pq('#wsm-prod-tab-decrip .wsm-prod-tab-content').html())
        details.append('<h2>'+pq('[itemprop="name"]').text()+'</h2>')
        images = []
        images.append(pq('.wsm_product_image_zoom').attr('href'))
        for img in pq('[id*="primage"]'):
            images.append(img.attrib['href'])

        details.append(', '.join(list(set(images))))

        details.append('')
        wr.writerow(details)
    except Exception as e:
        print (e)
            
DRIVER.quit()
    
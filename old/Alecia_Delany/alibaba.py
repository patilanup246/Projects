# -*- coding: utf-8 -*-
'''
Created on 09-Jan-2018

@author: Administrator
'''
import requests, csv, os
from pyquery import PyQuery
from selenium import webdriver
from glob import glob

#driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')


# output_f = open('output.csv','w',encoding='utf-8', newline='')
# wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
# wr.writerow([])
# products_url = ''
# 
# page = 1
# while True:
#     r = requests.get('https://wholesaler.alibaba.com/category_search?catI=15&pageId={}&sm=null&em=1&sp=20&ep=300&freeshipping=AU'.format(str(page)))
#     pq = PyQuery(r.text)
#     no_of_products = len(pq('.item-main'))
#     print (str(page) + ' - '+str(no_of_products))
#     if no_of_products < 1:
#         break
#     for f in pq('.item-main'):
#         stars = len(pq(f)('i.ui2-icon-svg-diamond-level-one'))
#         if stars >= 2:
#             wr.writerow ([pq(f)('h2 a').attr('href')])
#             #print (stars)
#     page+=1
#     
#     
#     
output_f = open('output_product.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
#wr.writerow([])
products_url = ''

for product in open('output.csv').read().split('\n'):
    print (product)
    details = []
    details.append(product)
    
    product_id  = (product.replace('.html','').split('_')[-1])
    r = requests.get(product).text
     
    pq = PyQuery(r)
    details.append(pq('[property="og:image"]').attr('content'))
    print (pq('[property="og:image"]').attr('content'))
    details.append(pq('[property="og:title"]').attr('content'))
    details.append(pq('[property="og:description"]').attr('content'))
    details.append(pq('[property="og:price:amount"]').attr('content'))
    try:
        r_delivery = requests.get('https://market.alibaba.com/groupsourcing/cost-logistics.htm?&country=AU&productId={}&count=1&dispatchLocation=CN'.format(str(product_id))).json()['data'][0]['time']
        details.append(r_delivery)
    except Exception as e:
        details.append('')
        print (e)
    
    wr.writerow(details)
    
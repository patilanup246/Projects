'''
Created on May 7, 2017

@author: Mukadam
'''
import requests , re, json
from pyquery import PyQuery
from unicodedata import category
from datetime import datetime
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
file_product_list = open('file_product_list.txt','w')
file_store_list = open('file_store_list.txt','w')
url = "https://www.aliexpress.com/wholesale"

file_product_ids = open('file_product_ids.txt','r').read().split('\n')
file_product_list = open('product_details.txt','w')
current_count = 1
for product in file_product_ids:
    print 'Count : '+str(current_count)
    current_count+=1
    #querystring = {"SearchText":str(product)}
    response = requests.request("GET", "https://www.aliexpress.com/wholesale?SearchText="+str(product))
    
    pq = PyQuery(response.text)
    
    product_id = ''
    store_id = ''
    product_title = ''
    product_image_urls = []
    price = ''
    currency = ''
    unit = ''
    discount_price = ''
    discount_currency = ''
    discount_unit = ''
    rating = ''
    votes = ''
    rating_5 = ''
    rating_4 = ''
    rating_3 = ''
    rating_2 = ''
    rating_1 = ''
    category = []
    shipping = ''
    estimated_delivery_time = ''
    pieces_available = ''
    orders = ''
    
    
    product_id =                str(product).strip()
    store_id =                  pq('.store-number').text().strip()
    product_title =             pq('.product-name').text()
    product_image_urls = []
    for image in pq('.img-thumb-item img'):
        product_image_urls.append(image.attrib['src'].replace('jpg_50x50.jpg','jpg_640x640.jpg'))
    price =                     pq('#j-sku-price').text()
    currency =                  pq('.p-del-price-detail .p-symbol').text()
    unit =                      pq('.p-del-price-detail .p-unit').text()
    discount_price =            pq('#j-sku-discount-price').text()
    discount_currency =         pq('.p-current-price [itemprop="priceCurrency"]').text()
    discount_unit =             pq('.p-current-price .p-unit').text()
    rating =                    pq('.product-customer-reviews [itemprop="ratingValue"]').text()
    votes =                     pq('.product-customer-reviews [itemprop="reviewCount"]').text()
    rating_5 =                  pq('.detail .rate-list [data="5 Stars"]').text()
    rating_4 =                  pq('.detail .rate-list [data="4 Stars"]').text()
    rating_3 =                  pq('.detail .rate-list [data="3 Stars"]').text()
    rating_2 =                  pq('.detail .rate-list [data="2 Stars"]').text()
    rating_1 =                  pq('.detail .rate-list [data="1 Stars"]').text()
    category = []
    for cat in pq('.ui-breadcrumb a'):
        category.append(re.sub("\D", "", cat.attrib['href']))
    orders = pq('#j-order-num').text()
    time_scraped = str(datetime.now())
    output_data = str(product_id)+'\t'+str(store_id)+'\t'+str(product_title)+'\t'+str(product_image_urls)+'\t'+str(price)+'\t'+str(currency)+'\t'+str(unit)+'\t'+str(discount_price)+'\t'+str(discount_currency)+'\t'+str(discount_unit)+'\t'+str(rating)+'\t'+str(votes)+'\t'+str(rating_5)+'\t'+str(rating_4)+'\t'+str(rating_3)+'\t'+str(rating_2)+'\t'+str(rating_1)+'\t'+str(category)+'\t'+str(shipping)+'\t'+str(estimated_delivery_time)+'\t'+str(pieces_available)+'\t'+str(orders)+'\t'+str(time_scraped)+'\n'
    file_product_list.write(output_data) 
    file_product_list.flush()
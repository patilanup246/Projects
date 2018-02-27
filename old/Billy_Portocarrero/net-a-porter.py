'''
Created on 08-Oct-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import re
import json
import csv

file_export = open('net-a-porter.csv','w', newline='')
csv_headers = ['Handle','Title','Body (HTML)','Vendor','Type','Option1 Name','Option1 Value',    'Option2 Name','Option2 Value',    'Variant Grams','Variant Inventory Qty','Variant Price','Variant Compare At Price','Variant Requires Shipping',    'Variant Taxable','Image Src','Variant Image']

wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
wr.writerow (csv_headers)





def get_products():
    product_links = []
    starting_urls = ['https://www.net-a-porter.com/us/en/m/Shop/Beauty/All?cm_sp=topnav-_-beauty-_-allbeauty&pn=']
     
    for u in starting_urls:
        page_num = 110
        while True:
            print (u+str(page_num))
            r_page = requests.get(u+str(page_num)).text
            pq = PyQuery(r_page)
            if len(pq('.product-row .description a')) == 0:
                break
             
            for p in pq('.product-row .description a'):
                product_links.append('https://www.net-a-porter.com'+p.attrib['href'])
            page_num+=1
         
    
    
    return product_links










for url in get_products():
    try:
        print (url)
        r_product = requests.get(url).text
        pq = PyQuery(r_product)
        
        handle = url.split('/')[-1]
        title = pq('.product-name').text()
        body = pq('.font-list-copy').html()
        quantity = '1'
        price = ''
        old_price = str(int(pq('.product-data').attr('data-price'))/100)
        vendor = pq('.designer-name span').text()
        category = pq('.product-data').attr('data-breadcrumb-keys')
        i_int = 0
        thumb_length = len(pq('.thumbnail-image'))
        for t in pq('.thumbnail-image'):
            if i_int == 0:
                product_details = []                        
                product_details.append(handle)
                product_details.append(title)
                product_details.append(body)
                product_details.append(vendor)
                product_details.append(category)
                product_details.append('')
                product_details.append('')
                product_details.append('')          
                product_details.append('')
                product_details.append('')
                product_details.append(quantity)
                product_details.append(old_price)
                product_details.append('')           
                product_details.append('TRUE')
                product_details.append('TRUE')
                product_details.append('https://'+t.attrib['src'][2:].replace('_xs','_pp'))
                product_details.append('')
                
                wr.writerow (product_details)
                i_int=1
            else:
                product_details = []                        
                product_details.append(handle)
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')          
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append('https://'+t.attrib['src'][2:].replace('_xs','_pp'))
                product_details.append('')
                
                wr.writerow (product_details)
    except:
        pass
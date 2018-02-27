'''
Created on 07-Oct-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import re
import json
import csv\


file_export = open('nastygal.csv','w', newline='')
csv_headers = ['Handle','Title','Body (HTML)','Vendor','Type','Option1 Name','Option1 Value',    'Option2 Name','Option2 Value',    'Variant Grams','Variant Inventory Qty','Variant Price','Variant Compare At Price','Variant Requires Shipping',    'Variant Taxable','Image Src','Variant Image']

wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
wr.writerow (csv_headers)



def get_products():  
    start_num = 0
    start_url = 'http://www.nastygal.com/womens/accessories?sz=120&start='
    product_links = []
    while True:
        r_list = requests.get(start_url+str(start_num))
        pq = PyQuery(r_list.text)
        if len(pq('.search-result-items .name-link')) == 0:
            break
        for p in pq('.search-result-items .name-link'):
            product_links.append(p.attrib['href'])
        start_num+=120
    return product_links
        


for url in get_products():
    try:
        print (url)
        r_product = requests.get(url).text
        pq = PyQuery(r_product)
        handle = url.replace('http://www.nastygal.com/', '').split('/')[0]
        title = pq('.is-mobile [itemprop="name"]').text()
        body = (pq('[name="description"]').attr('content'))+' Free shipping (No minimum) is available for this item. Go on Baby! Treat yourself.'
        quantity = pq('.quantity #Quantity').attr('data-available')
        price = pq('.is-mobile .price-sales').text()
        vendor = ''
        i_int = 0
        thumb_length = len(pq('.thumbnail-link'))
        for c in pq('.swatches.color span'):
            
            for s in pq('.swatches.size span'):
                if i_int == 0:
                    product_details = []                        
                    product_details.append(handle)
                    product_details.append(title)
                    product_details.append(body)
                    product_details.append(vendor)
                    product_details.append(pq('.breadcrumb-item:nth-child(4)').text())
                    product_details.append('Size')
                    product_details.append(json.loads(s.attrib['data-variation-values'])['attributeValue'])
                    product_details.append('Color')          
                    product_details.append(json.loads(c.attrib['data-variation-values'])['attributeValue'])
                    product_details.append('')
                    product_details.append(quantity)
                    product_details.append(price.replace('$',''))
                    product_details.append('')
                    product_details.append('TRUE')
                    product_details.append('TRUE')
                    product_details.append('')
                    product_details.append('http://'+json.loads(c.attrib['data-lgimg'])['hires'][2:])
                    wr.writerow (product_details)
                    i_int=1
                else:
                    product_details = []                        
                    product_details.append(handle)
                    product_details.append('')
                    product_details.append('')
                    product_details.append('')
                    product_details.append(pq('.breadcrumb-item:nth-child(4)').text())
                    product_details.append('Size')
                    product_details.append(json.loads(s.attrib['data-variation-values'])['attributeValue'])
                    product_details.append('Color')          
                    product_details.append(json.loads(c.attrib['data-variation-values'])['attributeValue'])
                    product_details.append('')
                    product_details.append(quantity)
                    product_details.append(price.replace('$',''))
                    product_details.append('')
                    product_details.append('TRUE')
                    product_details.append('TRUE')
                    product_details.append('')
                    product_details.append('http://'+json.loads(c.attrib['data-lgimg'])['hires'][2:])
                    wr.writerow (product_details)
            for l in range(1,thumb_length+1):
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
                img_url = json.loads(c.attrib['data-lgimg'])['hires'][2:].split('?')
                
                product_details.append('http://'+img_url[0]+'_'+str(l)+'?'+img_url[1])
                product_details.append('')
                wr.writerow (product_details)
    except:
        pass
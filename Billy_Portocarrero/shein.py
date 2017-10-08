'''
Created on 08-Oct-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import re
import json
import csv

file_export = open('shein.csv','w', newline='')
csv_headers = ['Handle','Title','Body (HTML)','Vendor','Type','Option1 Name','Option1 Value',    'Option2 Name','Option2 Value',    'Variant Grams','Variant Inventory Qty','Variant Price','Variant Compare At Price','Variant Requires Shipping',    'Variant Taxable','Image Src','Variant Image']

wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
wr.writerow (csv_headers)


def get_products():
    product_links = []
    starting_urls = ['http://us.shein.com/Sweaters-c-1734',
                    'http://us.shein.com/Sweatshirts-c-1773',
                    'http://us.shein.com/Shirts-c-1733',
                    'http://us.shein.com/US-Clothing-vc-34769',
                    'http://us.shein.com/women-dresses-c-1727',
                    'http://us.shein.com/US-Bottoms-vc-31859',
                    'http://us.shein.com/Women-shoes-c-1745',
                    'http://us.shein.com/Body-Jewellery-c-1908',
                    'http://us.shein.com/Accessories-c-1765',
                    'http://us.shein.com/Underwear-c-1862'
                    ]
     
    for u in starting_urls:
        page_num = 1
        while True:
            print (u+'-p'+str(page_num)+'.html')
            r_page = requests.get(u+'-p'+str(page_num)+'.html').text
            pq = PyQuery(r_page)
            if len(pq('.product .description a')) == 0:
                break
             
            for p in pq('.product .description a'):
                product_links.append('http://us.shein.com'+p.attrib['href'])
            page_num+=1
            
        
        
        
    
    return product_links







for url in get_products():
    try:
        print (url)
        r_product = requests.get(url).text
        pq = PyQuery(r_product)
        
        handle = url.replace('http://us.shein.com/', '').replace('html','')
        title = pq('h2.name').text().strip()
        body = pq('[property="og:description"]').attr('content').replace('SheIn','Portocarrero') + ' Free shipping (No minimum) is available for this item. Go on Baby! Treat yourself. \n'+ pq('.goods_description_con').html().replace('SheIn','Portocarrero')
        quantity = '1'
        price = re.search('gb_ga_price = "(.*?)"', r_product).group(1)
        size_json = json.loads(re.search('var _testattr = (.*?);', r_product).group(1))
        size_array = []
        for k in size_json.keys():
            if size_json[k]['name'] == 'Size':
                size_array = size_json[k]['value']
        
        old_price = ''
        vendor = ''
        category = pq('.she-breadcrumb li:nth-child(3) a.gap-top-cats').text()
        i_int = 0
        #thumb_length = len(pq('.thumbnail-link'))
    
        for s in size_array:
            if i_int == 0:
                product_details = []                        
                product_details.append(handle)
                product_details.append(title)
                product_details.append(body)
                product_details.append(vendor)
                product_details.append(category)
                product_details.append('Size')
                product_details.append(s['attr_value'])
                product_details.append('')          
                product_details.append('')
                product_details.append('')
                product_details.append(quantity)
                product_details.append(price.replace('$',''))
                product_details.append(old_price)
                
                           
                product_details.append('TRUE')
                product_details.append('TRUE')
                product_details.append('')
                product_details.append('')
                wr.writerow (product_details)
                
                
                for t in pq('.vertical-wrap img'):
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
                    product_details.append(t.attrib['src'])
                    product_details.append('')
                    wr.writerow (product_details)
                
                
                i_int=1
            else:
                product_details = []                        
                product_details.append(handle)
                product_details.append('')
                product_details.append('')
                product_details.append('')
                product_details.append(category)
                product_details.append('Size')
                product_details.append(s['attr_value'])
                product_details.append('')          
                product_details.append('')
                product_details.append('')
                product_details.append(quantity)
                product_details.append(price.replace('$',''))
                product_details.append(old_price)
                
                
                product_details.append('TRUE')
                product_details.append('TRUE')
                product_details.append('')
                product_details.append('')
                wr.writerow (product_details)
    except:
        pass
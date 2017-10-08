'''
Created on 07-Oct-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import re
import json
import csv

file_export = open('urbanoutfitters.csv','w', newline='')
csv_headers = ['Handle','Title','Body (HTML)','Vendor','Type','Option1 Name','Option1 Value',    'Option2 Name','Option2 Value',    'Variant Grams','Variant Inventory Qty','Variant Price','Variant Compare At Price','Variant Requires Shipping',    'Variant Taxable','Image Src','Variant Image']

wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
wr.writerow (csv_headers)



def get_products():
    product_links = []
    starting_urls = ['https://www.urbanoutfitters.com/shoes-for-women?page=','https://www.urbanoutfitters.com/women-accessories?page=']
    
    for u in starting_urls:
        page_num = 1
        while True:
            print (u+str(page_num))
            r_page = requests.get(u+str(page_num)).text
            pq = PyQuery(r_page)
            if len(pq('.js-product-tile')) == 0:
                break
            
            for p in pq('.js-product-tile .c-product-tile-controls__quickshop-link'):
                product_links.append('https://www.urbanoutfitters.com'+p.attrib['href'])
            page_num+=1
        
    
    
    return product_links



for url in get_products():
    try:
        print (url)
        r_product = requests.get(url).text
        pq = PyQuery(r_product)
        
        handle = url.replace('https://www.urbanoutfitters.com/shop/', '').split('?')[0]
        title = pq('[property="og:title"]').attr('content')
        body = pq('[property="og:description"]').attr('content').replace('Urban Outfitters','Portocarrero').replace(', colors and brands','').replace(' today','') + ' Free shipping (No minimum) is available for this item. Go on Baby! Treat yourself.'
        quantity = '1'
        price = pq('[property="product:price:amount"]').attr('content')
        old_price = pq('.c-product-meta__original-price').text().replace('$','')
        vendor = ''
        category = pq('[property="product:retailer_category"]').attr('content')
        i_int = 0
        thumb_length = len(pq('.thumbnail-link'))
        for c in pq('.js-product-colors li a'):
            
            for s in pq('.js-product-sizes [data-qa-size]'):
                if i_int == 0:
                    product_details = []                        
                    product_details.append(handle)
                    product_details.append(title)
                    product_details.append(body)
                    product_details.append(vendor)
                    product_details.append(category)
                    product_details.append('Size')
                    product_details.append(s.text)
                    product_details.append('Color')          
                    product_details.append(c.attrib['title'])
                    product_details.append('')
                    product_details.append(quantity)
                    product_details.append(price.replace('$',''))
                    product_details.append('')           
                    product_details.append('TRUE')
                    product_details.append('TRUE')
                    product_details.append('')
                    product_details.append('http://images.urbanoutfitters.com/is/image/UrbanOutfitters/'+pq('[property="product:retailer_item_id"]').attr('content')+'_'+c.attrib['data-color-code']+'_b?$xlarge$')
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
                    product_details.append(s.text)
                    product_details.append('Color')          
                    product_details.append(c.attrib['title'])
                    product_details.append('')
                    product_details.append(quantity)
                    product_details.append(price.replace('$',''))
                    product_details.append('')
                    product_details.append('TRUE')
                    product_details.append('TRUE')
                    product_details.append('')
                    product_details.append('http://images.urbanoutfitters.com/is/image/UrbanOutfitters/'+pq('[property="product:retailer_item_id"]').attr('content')+'_'+c.attrib['data-color-code']+'_b?$xlarge$')
                    wr.writerow (product_details)
    #         for l in range(1,thumb_length+1):
    #             product_details = []                        
    #             product_details.append(handle)
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')          
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             product_details.append('')
    #             img_url = json.loads(c.attrib['data-lgimg'])['hires'][2:].split('?')
    #             
    #             product_details.append('http://'+img_url[0]+'_'+str(l)+'?'+img_url[1])
    #             product_details.append('')
    #             wr.writerow (product_details)
    except:
        pass
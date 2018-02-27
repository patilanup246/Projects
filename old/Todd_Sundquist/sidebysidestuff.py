'''
Created on 06-Dec-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import json



def get_all_brands():
    j_list = []
    r = requests.get('https://www.sidebysidestuff.com/featured-brands.html').text
    pq = PyQuery(r)
    for p in pq('table [class="name"] a'):
        j_obj = {}
        j_obj['site'] = 'https://www.sidebysidestuff.com/'+p.attrib['href']
        j_obj['name'] = p.text
        
        j_list.append(j_obj)
        
    return j_list


def get_all_brand_products(brand_site):
    r = requests.get(brand_site).text
    pq = PyQuery(r)
    products = []
    for p in pq('table [class="name"] a'):
        products.append('https://www.sidebysidestuff.com/'+p.attrib['href'])
    return products

products_list = []
for b in get_all_brands():
    brand_products = get_all_brand_products(b['site'])
    
    for product in brand_products:
        try:
            print (b['name']+'\t'+product)
            p_obj = {}
            r = requests.get(product).text
            pq = PyQuery(r)
            p_obj['URL'] = product
            p_obj['name'] = pq('[itemprop="name"]').text()
            p_obj['code'] = pq('[class="code"] td').text()
            p_obj['brand'] = pq('[class="brand"] td').text()
            p_obj['availability'] = pq('[class="availability"] td').text()
            p_obj['description'] = pq('[itemprop="description"]').html()
            
            
            if pq('[class="sale-price"]'):
                p_obj['old_price'] = pq('#pitPriceBx').text()
                p_obj['price'] = pq('#pitSalePriceBx').text()
                p_obj['saved_amount'] = pq('#pitYouSaveBx').text()
            else:
                p_obj['price'] = pq('#pitPriceBx').text()
                
            for s in pq('tr.options select'):
                options_o = []
                for o in pq(s)('option'):
                    options_o.append(o.text)
                p_obj[s.attrib['name']] = ', '.join(options_o)
            images = []
            for i in pq('[rel="prettyPhoto[gallery]"]'):
                images.append(i.attrib['href'])
                
            p_obj['images'] = ', '.join(images)
            
            products_list.append(p_obj)

        except Exception as e:
            print (e)
            
output_file = open('sidebysidestuff_output.txt','w',encoding='utf-8')
output_file.write(json.dumps(products_list))
output_file.close()
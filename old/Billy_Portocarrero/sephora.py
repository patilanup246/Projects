'''
Created on 06-Oct-2017

@author: Administrator
'''

import requests
from pyquery import PyQuery
import re
import json
import csv

starting_url = 'https://sephora.com/rest/products/?ref=900031&include_categories=true&include_refinements=true&brandId=1073&currentPage='
file_export = open('sephora.csv','w', newline='')
csv_headers = ['Handle','Title','Body (HTML)','Vendor','Type','Option1 Name','Option1 Value',    'Option2 Name','Option2 Value',    'Variant Grams','Variant Inventory Qty','Variant Price','Variant Compare At Price','Variant Requires Shipping',    'Variant Taxable','Image Src','Variant Image']

wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
wr.writerow (csv_headers)

def get_product_list():
    products = []
    page_num = 1
    while True:
        print (starting_url+str(page_num))
        r_prod_list = requests.get(starting_url+str(page_num)).json()
        
        if r_prod_list['products']:
            for product in r_prod_list['products']:
                products.append('https://sephora.com'+product['product_url'])
        
        else:
            break
        page_num+=1
    return products
    


for p in get_product_list():
    try:
        r_product_page = requests.get(p).text
        
        product_json = json.loads(re.search( r'<script id="linkJSON" type="text/json" data-comp="PageJSON">(.*?)</script>', r_product_page).group(1))
        
        print (p)
        for o in product_json:
            try:
                
                current_product = o['props']['currentProduct']
        
                variants = []
                
                
                handle = current_product['seoName']
                title = current_product['seoTitle']
                body = current_product['seoMetaDescription'].replace('Sephora','Portocarrero')
                vendor = current_product['brand']['displayName']
                category = current_product['parentCategory']['parentCategory']['parentCategory']['displayName'] +' > '+current_product['parentCategory']['parentCategory']['displayName']+' > '+current_product['parentCategory']['displayName']
                
    
                
                main_product_images = []
                main_product_images.append(object)
                try:
                    current_product['regularChildSkus']
                    i_int=0
                    for v in current_product['regularChildSkus']:
                        #print ('variationType - '+v['variationType'])
                        variant_obj = {}
                        variant_obj['price'] = v['listPrice']
                        variant_obj['quantity'] = v['maxPurchaseQuantity']
                        variant_obj['size'] = v['size']
                        variant_obj['image'] =  'https://sephora.com'+v['skuImages']['image1500']
                        
                        if i_int == 0:
                            product_details = []                        
                            product_details.append(handle)
                            product_details.append(title)
                            product_details.append(body)
                            product_details.append(vendor)
                            product_details.append(current_product['parentCategory']['displayName'])
                            product_details.append('Size')
                            product_details.append(v['size'])
                            product_details.append('Color')
                            if v['variationType'] == 'Color':  
                                product_details.append(v['variationValue'])
                            else:
                                product_details.append('')
                            product_details.append('')
                            product_details.append(v['maxPurchaseQuantity'])
                            product_details.append(v['listPrice'].replace('$',''))
                            product_details.append('')
                            product_details.append('TRUE')
                            product_details.append('TRUE')
                            product_details.append('https://sephora.com'+v['skuImages']['image1500'])
                            product_details.append('')
                            
                            wr.writerow (product_details)
                            i_int=1
                        else:
                            product_details = []                        
                            product_details.append(handle)
                            product_details.append('')
                            product_details.append('')
                            product_details.append('')
                            product_details.append(current_product['parentCategory']['displayName'])
                            product_details.append('')
                            product_details.append(v['size'])
                            product_details.append('')
                            if v['variationType'] == 'Color':  
                                product_details.append(v['variationValue'])
                            else:
                                product_details.append('')
                            product_details.append('')
                            product_details.append(v['maxPurchaseQuantity'])
                            product_details.append(v['listPrice'].replace('$',''))
                            product_details.append('')
                            product_details.append('TRUE')
                            product_details.append('TRUE')
                            product_details.append('')
                            product_details.append('https://sephora.com'+v['skuImages']['image1500'])                
                            wr.writerow (product_details)
                        
                        
                        variants.append(variant_obj)
                except Exception as e:
                    try:
                        variant_obj = {}
                        variant_obj['price'] = current_product['currentSku']['listPrice']
                        variant_obj['quantity'] = current_product['currentSku']['maxPurchaseQuantity']
                        variant_obj['size'] = ''
                        variant_obj['image'] =  'https://sephora.com'+current_product['currentSku']['skuImages']['image1500']
                        variants.append(variant_obj)
                        
                        
                        product_details = []                        
                        product_details.append(handle)
                        product_details.append(title)
                        product_details.append(body)
                        product_details.append(vendor)
                        product_details.append(current_product['parentCategory']['displayName'])
                        product_details.append('')
                        product_details.append('')
                        product_details.append('')
                        product_details.append('')
                        product_details.append('')
                        product_details.append(current_product['currentSku']['maxPurchaseQuantity'])
                        product_details.append(current_product['currentSku']['listPrice'].replace('$',''))
                        product_details.append('')
                        product_details.append('TRUE')
                        product_details.append('TRUE')
                        product_details.append('https://sephora.com'+current_product['currentSku']['skuImages']['image1500'])
                        product_details.append('')
                        
                        wr.writerow (product_details)
    
                    except Exception as e:
                        print (str(e)+' - failed in current sku') 
                #print (variants)
                
                
                
                break
            except Exception as e:
                #print (e)
                pass
    except:
        pass

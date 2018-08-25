'''
Created on 06-Dec-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import json
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import csv
output_f = open('sidebyside_export.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['URL',	'Title',	'Body HTML',	'Vendor',	'Image Src','Variant Position',	'Variant SKU',	'Variant Price','Option1 Name',	'Option1 Value',	'Option2 Name',	'Option2 Value',	'Option3 Name',	'Option3 Value'])



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
        print (brand_site+' --> '+'https://www.sidebysidestuff.com/'+p.attrib['href'])
    return products


'''
# def get_all_brands():
#     j_list = []
#     r = requests.get('https://www.sidebysidestuff.com/featured-brands.html').text
#     pq = PyQuery(r)
#     for p in pq('table [class="name"] a'):
#         j_obj = {}
#         j_obj['site'] = 'https://www.sidebysidestuff.com/'+p.attrib['href']
#         j_obj['name'] = p.text
#         
#         j_list.append(j_obj)
#         
#     return j_list
# 
# 
# def get_all_brand_products(brand_site):
#     r = requests.get(brand_site).text
#     pq = PyQuery(r)
#     products = []
#     for p in pq('table [class="name"] a'):
#         products.append('https://www.sidebysidestuff.com/'+p.attrib['href'])
#     return products
# 
# products_list = []
# #for b in get_all_brands():
# #    brand_products = get_all_brand_products(b['site'])
#     
# for product in ['https://www.sidebysidestuff.com/front-windshield-arctic-cat-wildcat-1000-4-4x.html']:
#     try:
#         #print (b['name']+'\t'+product)
#         p_obj = {}
#         r = requests.get(product).text
#         pq = PyQuery(r)
#         p_obj['URL'] = product
#         p_obj['name'] = pq('[itemprop="name"]').text()
#         p_obj['code'] = pq('[class="code"] td').text()
#         p_obj['brand'] = pq('[class="brand"] td').text()
#         p_obj['availability'] = pq('[class="availability"] td').text()
#         p_obj['description'] = pq('[itemprop="description"]').html()
#         
#         
#         if pq('[class="sale-price"]'):
#             p_obj['old_price'] = pq('#pitPriceBx').text()
#             p_obj['price'] = pq('#pitSalePriceBx').text()
#             p_obj['saved_amount'] = pq('#pitYouSaveBx').text()
#         else:
#             p_obj['price'] = pq('#pitPriceBx').text()
#             
#         for s in pq('tr.options select'):
#             options_o = []
#             for o in pq(s)('option'):
#                 options_o.append(o.text)
#             p_obj[s.attrib['name']] = ', '.join(options_o)
#         images = []
#         for i in pq('[rel="prettyPhoto[gallery]"]'):
#             images.append(i.attrib['href'])
#             
#         p_obj['images'] = ', '.join(images)
#         
#         products_list.append(p_obj)
# 
#     except Exception as e:
#         print (e)
#             
# output_file = open('sidebysidestuff_output.txt','w',encoding='utf-8')
# output_file.write(json.dumps(products_list))
# output_file.close()
'''

driver = webdriver.Chrome()
applicable_brands = [x.lower() for x in open('brands.txt').read().split('\n')]

for b in get_all_brands():
    if not b['name'].strip().lower() in applicable_brands:
        continue
    brand_products = get_all_brand_products(b['site'])
    for u in brand_products:
        try:
            print ('Extracting : '+u)
            r=[[]]
            driver.get(u)

            url         = u
            title       = driver.find_element_by_css_selector('[itemprop="name"]').text
            sku         = driver.find_element_by_css_selector('[id="itemCode"]').text
            vendor      = driver.find_element_by_css_selector('[id="itemBrand"]').text
            body        = driver.find_element_by_css_selector('[itemprop="description"]').get_attribute('innerHTML')



            p = []
            for a in driver.find_elements_by_css_selector('[class="itemOption"] select')[:3]:
                p.append(Select(a).options)


            labels = []
            for a in driver.find_elements_by_css_selector('[class="itemOption"] [class="label"]')[:3]:
                labels.append(a.text)

            for x in p:
                r = [ i + [y] for y in x for i in r ]

            images = []
            for i in driver.find_elements_by_css_selector('[rel="prettyPhoto[gallery]"]'):
                images.append(i.get_attribute('href'))


            vp = 1
            for m in r:
                details = []
                details.append(url)
                details.append(title)
                details.append(body)
                details.append(vendor.replace('BRAND: ',''))
                details.append('; '.join(images))
                details.append(vp)
                details.append(sku.replace('ITEM # ',''))
                details.append ('')
                li = 0
                for n in m:
                    n.click()
                    details.append(labels[li])
                    details.append (n.get_attribute('value'))
                    li+=1
                
                details[7] = driver.find_element_by_css_selector('[class="salePrice"]').text
                
                vp+=1
                

                wr.writerow(details)
        except Exception as e:
            print (e)
            print (u)
    
driver.quit()
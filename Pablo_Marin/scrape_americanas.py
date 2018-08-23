# -*- coding: utf-8 -*-
import requests
import json
from pyquery import PyQuery
import pandas as pd
'''
Created on Jul 29, 2018

@author: tasneem
'''
def get_specs_buscape(url):
    
    r = requests.get(url).text
    pq = PyQuery(r)
    
    #get table description
    specs={}
    for row in pq('table tbody tr'):    
        td=[]
        for column in pq(row)('td'):
            td.append(column.text)
        specs[td[0]]=td[1]
    
    try:
        #images code
        images = []
        for img in pq('[class="swiper-slide"] a'):
            images.append(img.attrib['href'])
        specs['images'] = images
    except Exception as e:
        print (e)
    

    specs['url'] = url
    
    return specs


def get_all_products():
    offset = 0
    mobiles = [] 
    while True:
        products = requests.get('https://mystique-v2-americanas.b2w.io/search?offset={}&sortBy=topSelling&source=omega&filter=%7B%22id%22%3A%22category.id%22%2C%22value%22%3A%22345395%22%2C%22fixed%22%3Atrue%7D&limit=100&suggestion=true'.format(str(offset))).json()['products']
        
        for p in products:
            mobiles.append(p['id'])
        
        if len(products) < 100:
            break
        offset+=100
        
        #remove this break.  Added only for testing
        break
    return set(mobiles)


all_mobiles_dict = []
for mobile in get_all_products():
    print ('https://www.americanas.com.br/produto/'+str(mobile))
    all_mobiles_dict.append (get_specs_buscape('https://www.americanas.com.br/produto/'+str(mobile)))
    
open('final_output_americanas.txt','w').write(json.dumps(all_mobiles_dict))
df = pd.DataFrame.from_dict(all_mobiles_dict)
print (df)
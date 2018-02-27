'''
Created on May 6, 2017

@author: Mukadam
'''
import requests
from pyquery import PyQuery

base_url = 'https://m.aliexpress.com'

file_ali_express_category_list = open('file_ali_express_category_list.txt','w')

def get_cat_ids( site ):
    pq_categories  = PyQuery(requests.get(site).text)
    for item in pq_categories('.categories .ms-rc-ripple.ms-rc-custom a'):
        file_ali_express_category_list.write(item.attrib['href']+'\n')
        get_cat_ids(base_url+item.attrib['href'])
    

get_cat_ids(base_url+'/categoryList.htm')
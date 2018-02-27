'''
Created on 31-Dec-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import xmltodict, json
page_num = 1
output_file =  open('1mg_input.txt','w')
while True:
    print (page_num)
    try:
        r = requests.get('https://www.1mg.com/sitemap_drugs_{}.xml'.format(str(page_num))).text
        o = xmltodict.parse(r)
        for j in o['urlset']['url']:
            output_file.write (j['loc']+'\n')
            output_file.flush()
        page_num+=1
    except Exception as e:
        break
# pq = PyQuery(r)
# 
# for p in pq('[id^=collapsible]  div.expanded  div.collapsible-content  span.text'):
#     print (p.text)
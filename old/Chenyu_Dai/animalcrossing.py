# -*- coding: utf-8 -*-
'''
Created on 03-Nov-2017

@author: Administrator
'''
from pyquery import PyQuery
import requests
import json
import re
import csv
file_export = open('data_output.csv', 'w', newline='',encoding='utf-8')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Items','Theme', 'Selling Price','Cost to Make','Buying Price','Time to Craft (s)','Variation','Size','Furniture Reaction','Category','Series','Animal Gift Exclusive','Difficulty to Unlock','Special Requests from Contacts']
wr.writerow(headers)
#get furniture json
url = 'https://s3.us-east-2.amazonaws.com/gamepress-json/acpc/furniture.json'

furn = requests.get(url).json()
for f in furn:
    print (furn.index(f))
    details = []
    r_furn = requests.get('https://animalcrossing.gamepress.gg/' + str(re.match('<a href="(.*?)"', f['title']).group(1)))
    pq = PyQuery(r_furn.text)
    details.append(pq('.field.field--name-title.field--type-string.field--label-hidden').text())
    items = []
    for item in pq('.views-table.views-view-table.cols-2 tbody tr'):
        items.append(pq(item)('[hreflang="en"]').text() + ':' + pq(item)('.views-field.views-field-field-amount-required').text())
    details.append(', '.join(items))
    try:
        details.append(pq('.field--name-field-theme-image img').attr('src').split('/')[-1].replace('.png',''))
    except Exception as e:
        details.append('')
    i_num=0
    for i in pq('#furniture-details-table tr td'):    
        if not i_num == 0:
            details.append(pq(i).text())
        i_num = 1
    
    special_request = []
    for i in pq('.views-field.views-field-title [class="field-content"] a'):
        special_request.append(i.text)
    details.append(', '.join(special_request))
    
    wr.writerow(details)
    
    
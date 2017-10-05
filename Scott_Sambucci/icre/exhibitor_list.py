'''
Created on May 23, 2017

@author: Mukadam
'''
import requests
from pyquery import PyQuery

resp = requests.get('http://irce.a2zinc.net/IRCE2017/public/exhibitors.aspx').text
file_exhibitors = open('file_exhibitors_list.txt','w')
pq = PyQuery(resp)
for item in pq('.exhibitorName'):
    print pq('.exhibitorName').index(item)
    resp_booth = requests.get('http://irce.a2zinc.net/IRCE2017/public/'+item.attrib['href']).text
    pq_booth = PyQuery(resp_booth)
    
    name = pq_booth('.panel.panel-default .panel-body h1').text()
    city = pq_booth('.BoothContactCity').text()
    state = pq_booth('.BoothContactState').text()
    country = pq_booth('.BoothContactCountry').text()
    contact_url = pq_booth('.BoothContactUrl').text()
    category = pq_booth('.ProductCategoryContainer').text()
    
    
    file_exhibitors.write(name +'\t'+ city +'\t'+ state +'\t'+ country +'\t'+ contact_url +'\t'+ category+'\n')
    file_exhibitors.flush()
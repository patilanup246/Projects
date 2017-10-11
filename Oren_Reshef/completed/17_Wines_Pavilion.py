'''
Created on 10-Oct-2017

@author: Administrator
'''
import requests
import os
from pyquery import PyQuery
from time import gmtime, strftime

site_name = 'Wines_Pavilion'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass


starting_url = 'https://info.ybitan.co.il/pirce_update'
r_main = requests.get(starting_url,verify = False).text

pq = PyQuery(r_main)

for zip1 in pq('[data-type="items_"] a'):
    print (zip1.text)
    #urllib.request.urlretrieve (starting_url+'/'+zip1.attrib['href'], site_name+'/'+zip1.text)
    r = requests.get(starting_url+'/'+zip1.attrib['href'], verify=False,stream=True)
    with open(site_name+'/'+zip1.text, 'wb') as f:
        f.write(r.content)
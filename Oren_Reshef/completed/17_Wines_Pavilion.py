'''
Created on 10-Oct-2017

@author: Administrator
'''
import requests
import os
import urllib.request
from pyquery import PyQuery
from time import gmtime, strftime

site_name = 'Wines_Pavilion'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    'x-devtools-emulate-network-conditions-client-id': "f70d6403-10fb-4afc-ab2c-690d25591493",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://info.ybitan.co.il/pirce_update",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cookie': "PHPSESSID=7ca3r4squc5ja2a5frkdrlj1e0; _ga=GA1.3.1849746903.1507652667; _gid=GA1.3.189700375.1509770180; __atuvc=4%7C41%2C1%7C42%2C0%7C43%2C1%7C44; __atuvs=59fd43c389c1e9e6000"
    }
starting_url = 'https://info.ybitan.co.il/pirce_update'
r_main = requests.get(starting_url,verify = False).text

pq = PyQuery(r_main)

for zip1 in pq('[data-type="items_"] a'):
    name_link = zip1.text.lower()
    if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link or 'items' in name_link:
        print (zip1.text)
        
        #urllib.request.urlretrieve (starting_url+'/'+zip1.attrib['href'], site_name+'/'+zip1.text)
        
        r = requests.get(starting_url+'/'+zip1.attrib['href'],headers=headers, verify=False,stream=True)
        with open(site_name+'/'+zip1.text, 'wb') as f:
            f.write(r.content)
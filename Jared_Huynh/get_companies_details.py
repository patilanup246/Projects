'''
Created on May 20, 2017

@author: Mukadam
'''
import requests, re
from pyquery import PyQuery
file_input = open('companies_sites.txt','r').read().split('\n')
i=0
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
for item in file_input:
    try:
        response = requests.get(item,headers=headers).text
        #pq = PyQuery(response)
    
        #print response
        print item+'\t'+re.findall('\"website\":\"(.*?)\"', response.encode('ascii','ignore'))[0]+'\t'+re.findall('\"size\":\"(.*?)\"', response.encode('ascii','ignore'))[0]
    except Exception,e:
        print e
    print i
    i+=1
    if(i>1000):
        break
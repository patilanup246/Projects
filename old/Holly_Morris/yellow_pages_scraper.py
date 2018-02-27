'''
Created on 06-Nov-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
url = "https://www.yellowpages.com/worcester-ma/mip/x-core-fitness-461540907"
import time
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "www.yellowpages.com",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }
output = open('holly_output_urls.txt','w')
for url in open('holly_input_urls.txt').read().split('\n'):
    print (url)
    response = requests.request("GET", 'https://www.yellowpages.com'+url, headers=headers)

    pq = PyQuery(response.text)
    
    output.write(
                str('https://www.yellowpages.com'+url)+'\t'+
                str(pq('.sales-info h1').text())+'\t'+
                str(pq('.contact p:nth-child(1)').text())+'\t'+
                str(pq('.contact p:nth-child(2)').text())+'\t'+
                str(pq('.secondary-btn.website-link').attr('href'))+'\t'+
                str(pq('.email-business').attr('href'))+'\n'
                )
    
    output.flush()
    time.sleep(1)
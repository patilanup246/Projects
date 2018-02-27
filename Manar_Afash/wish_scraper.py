# -*- coding: utf-8 -*-

'''
Created on 18-Jan-2018

@author: Administrator
'''
import requests, csv, os
import time
import urllib.parse
import re
import json
Number_of_pages = 4
search_word = 'aleppo'
intervals = 5
headers1 = {
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Content-Length': "1741",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': '_timezone=5.5; _xsrf=2|723fbba6|3e4b9781f5b502964a3ad1e338e84bd6|1517128219; bsid=6c354612d79748b4a35538dab261d806; __utma=96128154.296359953.1517128222.1517128222.1517128222.1; __utmc=96128154; __utmz=96128154.1517128222.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _timezone=5.5; sweeper_session="2|1:0|10:1517128700|15:sweeper_session|84:NjhjODZjODMtNWNmNy00NzFhLWE2NzUtMWE2MzIyODFiOGMxMjAxOC0wMS0yOCAwODozODoxNS4zNDg1MTQ=|422730aff433e2c89e7bf235730a54f145eedbac364a534ce4036d5a48fa1ed5"; sessionRefreshed_5a6d8bf6a3b738272ca95950=true; __utmt=1; __utmb=96128154.13.10.1517128222; sweeper_uuid=e65c5c36679c46a98f9ee7facbf9c9ae; RT="sl=26&ss=1517128216574&tt=177766&obo=0&bcn=%2F%2F36fb607e.akstat.io%2F&sh=1517128968631%3D26%3A0%3A177766%2C1517128966918%3D25%3A0%3A173129%2C1517128951706%3D24%3A0%3A168492%2C1517128950113%3D23%3A0%3A165183%2C1517128939988%3D22%3A0%3A161874&dm=www.wish.com&si=b7908d85-2f1d-4b67-8fdb-15f523d59cb9&ld=1517128968631&r=https%3A%2F%2Fwww.wish.com%2Fsearch%2Faleppo&ul=1517128971400"',
    'Host': "www.wish.com",
    'Origin': "https://www.wish.com",
    'Pragma': "no-cache",
    'Referer': "https://www.wish.com/search/jacket",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.85 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'X-XSRFToken': "2|723fbba6|3e4b9781f5b502964a3ad1e338e84bd6|1517128219"
    }


def get_first_page_products(search1,price_array):
    headers2 = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': '_timezone=5.5; _xsrf=2|723fbba6|3e4b9781f5b502964a3ad1e338e84bd6|1517128219; bsid=6c354612d79748b4a35538dab261d806; __utma=96128154.296359953.1517128222.1517128222.1517128222.1; __utmc=96128154; __utmz=96128154.1517128222.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _timezone=5.5; sweeper_session="2|1:0|10:1517128700|15:sweeper_session|84:NjhjODZjODMtNWNmNy00NzFhLWE2NzUtMWE2MzIyODFiOGMxMjAxOC0wMS0yOCAwODozODoxNS4zNDg1MTQ=|422730aff433e2c89e7bf235730a54f145eedbac364a534ce4036d5a48fa1ed5"; sessionRefreshed_5a6d8bf6a3b738272ca95950=true; __utmt=1; __utmb=96128154.13.10.1517128222; sweeper_uuid=e65c5c36679c46a98f9ee7facbf9c9ae; RT="sl=26&ss=1517128216574&tt=177766&obo=0&bcn=%2F%2F36fb607e.akstat.io%2F&sh=1517128968631%3D26%3A0%3A177766%2C1517128966918%3D25%3A0%3A173129%2C1517128951706%3D24%3A0%3A168492%2C1517128950113%3D23%3A0%3A165183%2C1517128939988%3D22%3A0%3A161874&dm=www.wish.com&si=b7908d85-2f1d-4b67-8fdb-15f523d59cb9&ld=1517128968631&r=https%3A%2F%2Fwww.wish.com%2Fsearch%2Faleppo&ul=1517128971400"',
    'Host': "www.wish.com",
    'Pragma': "no-cache",
    'Referer': "https://www.wish.com/search/aleppo",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.100 Safari/537.36"
    }

    m = []
    r = requests.get('https://www.wish.com/search/'+str(urllib.parse.quote_plus(search1)),headers=headers2).text
    t = json.loads(re.findall(r"pageParams\['orig_feed_items'\] \= (.*);",r)[0])
    for p in t:
        price_array.append(int(p['commerce_product_info']['variations'][0]['price']))
        m.append(p['commerce_product_info']['variations'][0]['product_id'])
    o = ''
    for h in m:
        o+='&last_cids%5B%5D='+str(h)
    return (o)





output_f = open('output_wish.txt','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
url = "https://www.wish.com/api/search"



i=25
price_array = []
s1 = get_first_page_products(search_word,price_array)
while i < Number_of_pages*25:
    
    
    
    payload = "start="+str(i)+"&_buckets=&_experiments=&query="+search_word+"&transform=true"+s1
    response = requests.request("POST", url, data=payload, headers=headers1)
    print ('Scraping page -'+str(int(i/25)+1))
    i+=25

    s1 = ''
    if not response.json()['data']['results']:
        break
    for p in response.json()['data']['results']:
        #print (p)
        price_array.append(int(p['commerce_product_info']['variations'][0]['price']))
        s1+='&last_cids%5B%5D='+str(p['commerce_product_info']['variations'][0]['product_id'])
    time.sleep(5)



t = 0
while t < max(price_array):
    counter_p = 0
    for p in price_array:
        if t <= int(p) < (t+intervals):
            counter_p+=1
    output_f.write('{} - {} : {}\n'.format(str(t),str(t+intervals),counter_p))
    t+=intervals
    

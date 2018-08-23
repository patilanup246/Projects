# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
from pyquery import PyQuery
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import pandas as pd


total_page= 58



def get_specs_buscape(url):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter) 
    page = session.get(url,headers={"User-Agent":"Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    table=soup.find("table",{"class":"product-specs"})
    specs={}
    for row in table.find_all("tr",{"class":"product-specs__spec display"}):    
        td=[]
        for column in row.find_all("td"):
            td.append(column.text)
        specs[td[0]]=td[1]
    
    try:
        #images code
        pq = PyQuery(page.content)
        img = json.loads(pq('[type="application/ld+json"]').text())
        specs['images'] = img['image']
    except Exception as e:
        pass
    
    try:
        #Price code
        m = re.findall("{preco: (.*?), lojista: '(.*?)'}",pq('#dataLayerOffers').attr('value'))
        prices = []
        for n in m:
            price = {}
            price['preco']=n[0]
            price['lojista']=n[1]
            prices.append (price)
        specs['prices'] = prices
    except Exception as e:
        pass
    
    #added URL 
    specs['url'] = url
    
    return specs


all_links = []
for page_num in range(1,total_page+1):
    r = requests.get('https://www.buscape.com.br/celular-e-smartphone?neids=2&obn=1&pagina='+str(page_num))
    pq = PyQuery(r.text)
    print (page_num,len(pq('.card__item .wrapper-see-more a')))
    for l in pq('.card__item .wrapper-see-more a'):
        all_links.append(l.attrib['href'])
        
        
all_products = []
for l in set(all_links):
    print ('https://www.buscape.com.br'+l)
    try:
        specs=get_specs_buscape('https://www.buscape.com.br'+l)
        all_products.append(specs)
    except Exception as e:
        print (e)



open('final_output.txt','w').write(json.dumps(all_products))
df = pd.DataFrame.from_dict(all_products)

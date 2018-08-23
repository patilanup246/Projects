'''
Created on Jul 27, 2018

@author: talib
'''
# -*- coding: utf-8 -*-
import requests
import pandas as pd
from pyquery import PyQuery
from requests.adapters import HTTPAdapter

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "max-age=0",
    'connection': "keep-alive",
    'host': "www.buscape.com.br",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
def url_with_specs(cellphone):
    '''given a cellphone, ir returns a url where the tech specs are found. The search is done in buscape, brazilian site
    '''
    search_url='https://www.buscape.com.br/search/'
    url_to_search=search_url+cellphone
    
    
    r = requests.get(url_to_search,headers=headers).text
    

      
    #found 
    get_location=soup.find('div',{"class": "offers-result"})
    
    if get_location:
        for found in get_location.find_all('div',{"class": "card__item columns small-6 medium-6 large-4"}):
            link=found.find('div',{"class": "wrapper-see-more"})
            if link:
                a=link.find('a', href=True)
                http='https://www.buscape.com.br'+a['href']
                break
            else:
                http=''
    else:
        http=''
    
    return http

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
     
    return specs


#get specs for one cellphone
df=pd.read_csv('C:/Users/PabloCastano/PycharmProjects/marketplace/out_final.csv',encoding='latin-1')
cellphone_id=df['id'][0]
url=url_with_specs(cellphone_id)
specs=get_specs_buscape(url)

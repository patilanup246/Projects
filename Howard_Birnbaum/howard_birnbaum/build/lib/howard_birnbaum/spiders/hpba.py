# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class hpba(scrapy.Spider):
    name="hpba"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        i=1
        while True:
            r = requests.get('http://secure.hpba.org/cvweb/cgi-bin/utilities.dll/CustomList?DISTANCE=5000&COUNTRY_field=United+States&COUNTRYSEARCH=United+States&RANGE={}/25&NOWEBFLG=%3C%3EY&ISMEMBERFLG=Y&SHOWSQL=N&SORT=ORGNAME&SQLNAME=ORGSEARCH&WHP=organization.htm&WBP=organizationList.htm'.format(str(i))).text
            pq1 = PyQuery(r)
            print (i)
            
            for m in pq1('[data-label="Name"] a'):
                self.all_urls.append (m.attrib['onclick'].replace("getCVPageLink('orgProfile','","").replace("')",""))
            if len(pq1('[data-label="Name"] a')) < 25:
                break
            i+=25 
            


        
        

    def start_requests(self):
        for url in self.all_urls:
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'host': "www.hpba.org",
                "Cookie": ".ASPXANONYMOUS=kzwNksPz0wEkAAAAMGYxYzJmYWEtZDg2Yi00ZGZjLThkNjktNzJjYzI1Zjg3NzI10; _ga=GA1.2.1297773982.1521209957; dnn_IsMobile=False; language=en-US; _gid=GA1.2.832118142.1521552982",
                'pragma': "no-cache",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                }
            yield scrapy.Request(url='https://secure.hpba.org/cvweb/cgi-bin/organizationdll.dll/Info?orgcd='+str(url), headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        item = HowardBirnbaumItem()
        address = 0
        state = 0
        country = 0
        phone = 0
        web = 0
        email = 0
        city = 0
        postal = 0
        
        t = 1
        for i in pq('[class="dl-horizontal"] dt'):
            
            if 'Address' == i.text:
                address = t
            if 'City' in i.text:
                city = t
            if 'State' in i.text:
                state = t
            if 'Zip' in i.text:
                postal = t
            if 'Country' in i.text:
                country = t
            if 'Phone' in i.text:
                phone = t
            if 'Email' in i.text:
                email = t
            if 'Web Site' in i.text:
                web = t
                
            
            t+=1
        
        
        try:
            item['company'] = pq('[id="ORGNAME"]').text()
        except Exception as e:
            print (e)
        try:
            item['address'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(address)).text()
        except Exception as e:
            print (e)        
        try:
            item['state'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(state)).text()
        except Exception as e:
            print (e)        
        try:
            item['country'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(country)).text()
        except Exception as e:
            print (e)        
        try:
            item['phone_number'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(phone)).text()
        except Exception as e:
            print (e)        
        try:
            item['web_site_url'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(web)).text()
        except Exception as e:
            print (e)        
        try:
            item['email'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(email)).text()
        except Exception as e:
            print (e)
        try:
            item['city'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(city)).text()
        except Exception as e:
            print (e)
        try:
            item['postal_code'] = pq('[class="dl-horizontal"] dd:nth-of-type({})'.format(postal)).text()
        except Exception as e:
            print (e)
                    
       

        yield item
    

    
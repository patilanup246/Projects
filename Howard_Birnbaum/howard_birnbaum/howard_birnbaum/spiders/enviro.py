# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class enviro(scrapy.Spider):
    name="enviro"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass

        
        

    def start_requests(self):
        for i in range(1,3):
            for j in range(1,52):
                
                r = requests.get('http://enviro.com/find-a-dealer/dealer-locater/?country={}&prov={}'.format(str(i),str(j)))
                pq = PyQuery(r.text)
                for p in pq('[name="city"] [value]'):
                    yield scrapy.Request(url='http://enviro.com/find-a-dealer/dealer-locater/?country={}&prov={}&city={}'.format(str(i),str(j),p.attrib['value']), callback=self.parse)
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        scrape_item = pq('[style="float:left;"] [class="west"]').text().split('\n')
        item = HowardBirnbaumItem()
        try:
            item['company'] = scrape_item[0]
        except Exception as e:
            print (e)
        try:
            item['address'] = scrape_item[1]+' '+scrape_item[2]+' '+scrape_item[3]
        except Exception as e:
            print (e)        
        try:
            item['state'] = ''
        except Exception as e:
            print (e)        
        try:
            item['country'] = ''
        except Exception as e:
            print (e)        
        try:
            item['phone_number'] = scrape_item[4].replace('Ph:','')
        except Exception as e:
            print (e)        
        try:
            item['web_site_url'] = pq('[style="float:left;"] [class="west"] a[href*="http"]').attr('href')
        except Exception as e:
            print (e)        
        try:
            item['email'] = pq('[style="float:left;"] [class="west"] a[href*="mailto:"]').attr('href').replace('mailto:','')
        except Exception as e:
            print (e)
        try:
            item['city'] = ''
        except Exception as e:
            print (e)
        try:
            item['postal_code'] = ''
        except Exception as e:
            print (e)
                    
       

        yield item
        

    
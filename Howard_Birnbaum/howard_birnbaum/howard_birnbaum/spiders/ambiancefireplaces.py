# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class ambiancefireplaces(scrapy.Spider):
    name="ambiancefireplaces"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        url = "https://storage.scrapinghub.com/collections/293632/s/latlong"
        
        headers = {
            'content-type': "application/json",
            'authorization': "Basic ZWE3NmIwMzcxMGU3NDVlOGI2YWIxYTg2MGFiMjcxOGU6"
            }
        
        response = requests.request("GET", url, headers=headers).json()

        for i in response['value']:
            self.all_urls.append(i)


        
        

    def start_requests(self):

        yield scrapy.Request( url='https://ambiancefireplaces.com/wp-content/plugins/store-locator/sl-xml.php'.format(),callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(json.dumps(xmltodict.parse(response.body_as_unicode())))
        
        for m in r['markers']['marker']:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['@name']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['@address']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['@state']
            except Exception as e:
                print (e)        
            try:
                item['country'] = ''
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['@phone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['@url']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['@email']
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['@city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['@zip']
            except Exception as e:
                print (e)             
    
            yield item
        

    
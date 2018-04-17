# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class dimplex(scrapy.Spider):
    name="dimplex"
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
        for url in self.all_urls:
            url1 = url.split('$')
            yield scrapy.Request( url='https://www.dimplex.com/ajax/ajax-locator-showrooms.php?lat={}&lng={}&product=&radius=100'.format(str(url1[1]),str(url1[2])),callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['name']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['street1']+' '+m['street2']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['province']
            except Exception as e:
                print (e)        
            try:
                item['country'] = ''
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['phone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['website']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['email']
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['postal']
            except Exception as e:
                print (e)             
    
            yield item
        

    
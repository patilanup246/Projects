# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class firerock(scrapy.Spider):
    name="firerock"
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
            yield scrapy.Request( url='https://www.easylocator.net/ajax/search_by_lat_lon_geojson/FireRock%20Dealers/{}/{}/75/20'.format(str(url1[1]),str(url1[2])),callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r['physical']:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['properties']['name']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['properties']['street_address']+' '+m['properties']['street_address_line2']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['properties']['state_province']
            except Exception as e:
                print (e)        
            try:
                item['country'] = m['properties']['country']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['properties']['phone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['properties']['website_url']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['properties']['email']
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['properties']['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['properties']['zip_postal_code']
            except Exception as e:
                print (e)             
    
            yield item
        

    
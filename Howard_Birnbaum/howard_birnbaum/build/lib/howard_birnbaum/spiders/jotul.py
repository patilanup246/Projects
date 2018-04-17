# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class jotul(scrapy.Spider):
    name="jotul"
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

        yield scrapy.Request( url='https://jotul.com/us/retailers.xml',callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(json.dumps(xmltodict.parse(response.body_as_unicode())))
        
        for m in r['retailers']['retailer']:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['name']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['address']['street_long']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['address']['state']
            except Exception as e:
                print (e)        
            try:
                item['country'] = m['address']['country']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['contact']['phone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['contact']['url']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['contact']['email']
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['address']['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['address']['postal_code']
            except Exception as e:
                print (e)             
    
            yield item
        

    
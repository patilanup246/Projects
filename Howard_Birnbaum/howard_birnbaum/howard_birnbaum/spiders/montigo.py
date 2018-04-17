# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery
import re

class montigo(scrapy.Spider):
    name="montigo"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass


        
        

    def start_requests(self):
            yield scrapy.Request(url='https://www.montigo.com/find-a-dealer/')
    
    def parse(self, response):
        pq = PyQuery(response.body_as_unicode())
        r =  json.loads(re.findall('var json_dealers = (.*);',response.body_as_unicode())[0])
        
        for m in r:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['name']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['street']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['state']
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
                item['web_site_url'] = m['web']
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
        

    
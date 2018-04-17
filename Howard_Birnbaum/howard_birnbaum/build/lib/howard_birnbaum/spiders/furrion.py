# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class furrion(scrapy.Spider):
    name="furrion"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass


        
        

    def start_requests(self):

        yield scrapy.Request(url='https://www.furrion.com/cms/ajax?block=2', callback=self.parse)
        
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r['list']:
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
                item['state'] = m['postal']
            except Exception as e:
                print (e)        
            try:
                item['country'] = m['country']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = ''
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = ''
            except Exception as e:
                print (e)        
            try:
                item['email'] = ''
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['zip']
            except Exception as e:
                print (e)             
    
            yield item
        

    
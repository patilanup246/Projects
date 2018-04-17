# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class flarefireplaces(scrapy.Spider):
    name="flarefireplaces"
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

        yield scrapy.Request( url='http://flarefireplaces.com/wp-admin/admin-ajax.php?action=store_search&lat=37.09024&lng=-95.71289100000001&max_results=100&search_radius=100&autoload=1',callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['store']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['address']+' '+m['address2']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['state']
            except Exception as e:
                print (e)        
            try:
                item['country'] = m['country']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['phone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['url']
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
                item['postal_code'] = m['zip']
            except Exception as e:
                print (e)     
           
    
            yield item
        

    
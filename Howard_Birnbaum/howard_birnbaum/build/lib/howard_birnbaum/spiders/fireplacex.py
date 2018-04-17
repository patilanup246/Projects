# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class fireplacex(scrapy.Spider):
    name="fireplacex"
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
            req_url = "https://www.fireplacex.com/dealer-locator.aspx/GetNearest"
            headers = {
                'content-type': "application/json",
                'cache-control': "no-cache"
            }
            payload = {"request":{"lat":str(url1[1]),"lng":str(url1[2])}}
            yield scrapy.Request(method='POST', url=req_url, body=json.dumps(payload) ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(json.loads(response.body_as_unicode())['d'])
        
        for m in r:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['b']
            except Exception as e:
                print (e)
            try:
                item['address'] = m['a']
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['l']
            except Exception as e:
                print (e)        
            try:
                item['country'] = m['c']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['n']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['w']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['m']
            except Exception as e:
                print (e)        
                
            try:
                item['city'] = m['t']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['p']
            except Exception as e:
                print (e)     
           
    
            yield item
        

    
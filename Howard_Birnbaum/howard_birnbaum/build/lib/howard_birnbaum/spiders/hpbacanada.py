# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class hpbacanada(scrapy.Spider):
    name="hpbacanada"
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
            req_url = "http://hpbacanada.org/wp-admin/admin-ajax.php"
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache"
            }
            payload = "action=get_stores&lat={}&lng={}&radius=1000&categories%5B0%5D=".format(str(url1[1]),str(url1[2]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r.keys():
            item = HowardBirnbaumItem()
            try:
                item['company'] = r[m]['na']
            except Exception as e:
                print (e)
            try:
                item['address'] = r[m]['st']
            except Exception as e:
                print (e)        
            try:
                item['state'] = r[m]['rg']
            except Exception as e:
                print (e)        
            try:
                item['country'] = r[m]['co']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = r[m]['te']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = r[m]['we']
            except Exception as e:
                print (e)        
            try:
                item['email'] = r[m]['em']
            except Exception as e:
                print (e)      
            try:
                item['city'] = r[m]['ct']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = r[m]['zp']
            except Exception as e:
                print (e)    
           
    
            yield item
        

    
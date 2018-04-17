# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class rhpeterson(scrapy.Spider):
    name="rhpeterson"
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
            req_url = "http://www.rhpeterson.com/wp-admin/admin-ajax.php"
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache"
            }
            payload = "lat={}&lng={}&action=csl_ajax_search".format(str(url1[1]),str(url1[2]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r['response']:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['name']
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
                item['phone_number'] = m['data']['sl_phone']
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
        

    
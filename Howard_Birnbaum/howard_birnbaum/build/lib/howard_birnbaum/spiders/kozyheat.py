# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class kozyheat(scrapy.Spider):
    name="kozyheat"
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
            req_url = "http://www.kozyheat.com/wp-admin/admin-ajax.php"
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache"
            }
            payload = "action=get_dealers&filter=search&zip_code=10001&zipLat={}&zipLng={}&miles=150&metrica=Miles&state=&product_ids=&is_frontend=1".format(str(url1[1]),str(url1[2]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['business_name']
            except Exception as e:
                print (e)
            try:
                pq = PyQuery(m['address'])
                item['address'] = pq('div').text()
            except Exception as e:
                print (e)        
            try:
                item['state'] = ''
            except Exception as e:
                print (e)        
            try:
                item['country'] = ''
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['telephone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['website_url']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['email_address']
            except Exception as e:
                print (e)
            try:
                item['city'] = m['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = ''
            except Exception as e:
                print (e)
                        
           
    
            yield item
        

    
# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class valorfireplaces(scrapy.Spider):
    name="valorfireplaces"
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
        
        #for url in self.all_urls:
        headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded",
        'host': "valorfireplaces.com",
        'origin': "https://valorfireplaces.com",
        'pragma': "no-cache",
        'referer': "https://valorfireplaces.com/contact/",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        #url1 = url.split('$')
        req_url = "https://valorfireplaces.com/contact/"
        payload = "lat=&long=&geo=&myZIPCode=10001&radius=300&search=SEARCH"#.format(str(url1[0]))
        yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        
        for m in pq('table tr [valign="top"]'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('.dealer-titles').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('p').text()
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
        

    
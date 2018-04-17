# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class ironstrike(scrapy.Spider):
    name="ironstrike"
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
        headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "en-US,en;q=0.9",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            'host': "ironstrike.us.com",
            'pragma': "no-cache",
            'referer': "http://ironstrike.us.com/dealers",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
        for url in self.all_urls:
            url1 = url.split('$')
        req_url = "http://ironstrike.us.com/dealers?utf8=%E2%9C%93&zip=10001&submitted=Search&radius=500"#.format(str(url1[0]))
            
        yield scrapy.Request(url=req_url,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('[class="dealer"]'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('.title').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('.street').text()
            except Exception as e:
                print (e)        
            try:
                item['state'] = pq(m)('.city-state-zip').text().split(',')[1].strip().split(' ')[0]
            except Exception as e:
                print (e)        
            try:
                item['country'] = ''
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = pq(m)('.phone').text().replace('Phone: ','').split(' ')[0]
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = ''
            except Exception as e:
                print (e)        
            try:
                item['email'] = pq(m)('.email').text()
            except Exception as e:
                print (e)
            try:
                item['city'] = pq(m)('.city-state-zip').text().split(',')[0]
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = pq(m)('.city-state-zip').text().split(',')[1].strip().split(' ')[-1]
            except Exception as e:
                print (e)
                        
           
    
            yield item
        

    
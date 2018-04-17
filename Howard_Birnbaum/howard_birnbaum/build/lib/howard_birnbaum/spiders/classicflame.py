# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class classicflame(scrapy.Spider):
    name="classicflame"
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
            req_url = "http://twinstarhome.com.gotlocations.com/index.php"
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded",
                'host': "twinstarhome.com.gotlocations.com",
                'origin': "http://twinstarhome.com.gotlocations.com",
                'pragma': "no-cache",
                'referer': "http://twinstarhome.com.gotlocations.com/?product=Classicflame",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
                }
            payload = "product=Classicflame&address={}&ip_country=US&Submit=search&storename=".format(str(url1[0]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('[class*="altrow"]'):
            item = HowardBirnbaumItem()
            text_scraped =  pq(m).text().split('\n')
            try:
                item['company'] = text_scraped[0]
            except Exception as e:
                print (e)
            try:
                item['address'] = text_scraped[1]+' '+text_scraped[2]
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
                item['phone_number'] = text_scraped[3].replace('phone:','')
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('a[href*="http"][target="new"]').attr('href')
            except Exception as e:
                print (e)        
            try:
                item['email'] = pq(m)('a[href*="mailto"]').attr('href').replace('mailto:','')
            except Exception as e:
                print (e)
            try:
                item['city'] = ''
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = ''
            except Exception as e:
                print (e)
                        
           
    
            yield item
        

    
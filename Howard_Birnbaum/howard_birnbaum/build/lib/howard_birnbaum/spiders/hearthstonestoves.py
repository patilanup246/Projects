# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class hearthstonestoves(scrapy.Spider):
    name="hearthstonestoves"
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
            req_url = "http://ftp.hearthstonestoves.com/customer-resources/dealer-locator"
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded",
                'host': "ftp.hearthstonestoves.com",
                'origin': "http://ftp.hearthstonestoves.com",
                'pragma': "no-cache",
                'referer': "http://ftp.hearthstonestoves.com/customer-resources/dealer-locator",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
                }
            payload = "zip={}&submit=Find".format(str(url1[0]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('.dealer_information'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('h3').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('ul li:nth-of-type(1)').text()+' '+pq(m)('ul li:nth-of-type(2)').text()
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
                item['phone_number'] = pq(m)('ul li:nth-of-type(3)').text().replace('Phone:','')
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('ul li a[href*="www."]').attr('href')
            except Exception as e:
                print (e)        
            try:
                item['email'] = pq(m)('ul li a[href*="mailto:"]').text()
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
        

    
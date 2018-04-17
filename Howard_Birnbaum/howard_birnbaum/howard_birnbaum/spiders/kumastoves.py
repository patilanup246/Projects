# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class kumastoves(scrapy.Spider):
    name="kumastoves"
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
           
        yield scrapy.Request(url='https://www.kumastoves.com/Dealers/Locator', callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())

        for m in pq('.col-md-4 div'):
            phone = ''
            if not 'http' in pq(m).text().rsplit('\n')[-1]:
                phone = pq(m).text().rsplit('\n')[-1]
            else:
                phone = pq(m).text().rsplit('\n')[-2]
            item = HowardBirnbaumItem()
            x = pq(m)('span').text()
            try:
                item['company'] = pq(m)('span').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m).text().rsplit('\n',1)[0].replace(x,'').replace('\n','').replace(phone,'')
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
                item['phone_number'] = phone
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('a').text()
            except Exception as e:
                print (e)        
            try:
                item['email'] = ''
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
        

    
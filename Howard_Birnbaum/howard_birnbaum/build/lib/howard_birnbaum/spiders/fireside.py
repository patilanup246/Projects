# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class fireside(scrapy.Spider):
    name="fireside"
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

        
        
        yield scrapy.Request(url='http://www.fireside.com/Location-Finder.aspx', callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('[data-type="homeowner"]'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('h4').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('.location-address').text().replace('\n',' ')
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
                item['phone_number'] = pq(m)('.location-contacts dd:nth-of-type(1) a').text()
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = ''
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
        

    
# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class marquisfireplaces(scrapy.Spider):
    name="marquisfireplaces"
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
            
        for i in range(1,100):   
            yield scrapy.Request(url='https://marquisfireplaces.net/dealer-locations/page/{}/?gmw_address%5Bvalue%5D&gmw_distance=200&gmw_units=imperial&gmw_form=1&gmw_per_page=9&gmw_lat&gmw_lng&gmw_px=pt&action=gmw_post'.format(str(i)), callback=self.parse)
    
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('.dealer_locations'):
            item = HowardBirnbaumItem()

            try:
                item['company'] = pq(m)('h3').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('.wppl-address').text()
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
                item['phone_number'] = pq(m)('.phone .information').text()
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('.website .information').text()
            except Exception as e:
                print (e)        
            try:
                item['email'] = pq(m)('.email .information').text()
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
        

    
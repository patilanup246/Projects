# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class nehpba(scrapy.Spider):
    name="nehpba"
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

        yield scrapy.Request( url='https://nehpba.org/list/category/hearths-hearth-products-9',callback=self.parse)

    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('.mn-listing'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('.mn-title').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('[itemprop="address"]').text()
            except Exception as e:
                print (e)        
            try:
                item['state'] = pq(m)('[itemprop="addressRegion"]').text()
            except Exception as e:
                print (e)        
            try:
                item['country'] = ''
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = pq(m)('.mn-phone').text()
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('.mn-website a').attr('href')
            except Exception as e:
                print (e)        
            try:
                item['email'] = ''
            except Exception as e:
                print (e)        
            try:
                item['city'] = pq(m)('.mn-cityspan').text()
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = pq(m)('.mn-zipspan').text()
            except Exception as e:
                print (e)             
    
            yield item
        

    
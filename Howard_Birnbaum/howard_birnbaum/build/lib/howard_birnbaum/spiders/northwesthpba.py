# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class northwesthpba(scrapy.Spider):
    name="northwesthpba"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass


        
        

    def start_requests(self):
        headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "en-US,en;q=0.9",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            'host': "www.northwesthpba.org",
            'referer': "http://www.northwesthpba.org/business-directory/wpbdp_category/retail/",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }

            
        yield scrapy.Request(url='http://www.northwesthpba.org/business-directory/?wpbdp_view=all_listings',headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('.wpbdp-listing'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('.listing-title').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('.address-info').text().split('\n')[0].replace('Address ','')
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
                item['phone_number'] = pq(m)('.wpbdp-field-business_phone_number span').text()
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('.wpbdp-field-business_website_address a').text()
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
                item['postal_code'] = pq(m)('.address-info').text().split('\n')[1]
            except Exception as e:
                print (e)
                        
           
    
            yield item
        

    
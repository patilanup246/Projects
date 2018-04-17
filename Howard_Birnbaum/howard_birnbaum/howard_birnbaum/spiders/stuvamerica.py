# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class stuvamerica(scrapy.Spider):
    name="stuvamerica"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass


        
        

    def start_requests(self):
        
            
        yield scrapy.Request(url='http://stuvamerica.com/en/dealers/listing/', callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('[class="dealer-details"]'):
            item = HowardBirnbaumItem()
            scrape_text = pq(m).text().split('\n')
            try:
                item['company'] = scrape_text[0]
            except Exception as e:
                print (e)
            try:
                item['address'] = scrape_text[1]+' '+scrape_text[2]
            except Exception as e:
                print (e)        
            try:
                item['state'] = ''
            except Exception as e:
                print (e)        
            try:
                item['country'] = scrape_text[3]
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = scrape_text[4].replace('Phone:','')
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = ''
            except Exception as e:
                print (e)        
            try:
                item['email'] = ''
            except Exception as e:
                item['email'] = ''
            try:
                item['city'] = ''
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = ''
            except Exception as e:
                print (e)
                        
           
    
            yield item
        

    
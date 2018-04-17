# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class stellarhearth(scrapy.Spider):
    name="stellarhearth"
    all_urls = ['https://www.stellarhearth.com/dealers/state/AB/map',
'https://www.stellarhearth.com/dealers/state/AR/map',
'https://www.stellarhearth.com/dealers/state/AZ/map',
'https://www.stellarhearth.com/dealers/state/BC/map',
'https://www.stellarhearth.com/dealers/state/CA/map',
'https://www.stellarhearth.com/dealers/state/CO/map',
'https://www.stellarhearth.com/dealers/state/CT/map',
'https://www.stellarhearth.com/dealers/state/DE/map',
'https://www.stellarhearth.com/dealers/state/FL/map',
'https://www.stellarhearth.com/dealers/state/GA/map',
'https://www.stellarhearth.com/dealers/state/IA/map',
'https://www.stellarhearth.com/dealers/state/ID/map',
'https://www.stellarhearth.com/dealers/state/IL/map',
'https://www.stellarhearth.com/dealers/state/IN/map',
'https://www.stellarhearth.com/dealers/state/KS/map',
'https://www.stellarhearth.com/dealers/state/KY/map',
'https://www.stellarhearth.com/dealers/state/MA/map',
'https://www.stellarhearth.com/dealers/state/MB/map',
'https://www.stellarhearth.com/dealers/state/MD/map',
'https://www.stellarhearth.com/dealers/state/MI/map',
'https://www.stellarhearth.com/dealers/state/MN/map',
'https://www.stellarhearth.com/dealers/state/MO/map',
'https://www.stellarhearth.com/dealers/state/MT/map',
'https://www.stellarhearth.com/dealers/state/NC/map',
'https://www.stellarhearth.com/dealers/state/ND/map',
'https://www.stellarhearth.com/dealers/state/NE/map',
'https://www.stellarhearth.com/dealers/state/NH/map',
'https://www.stellarhearth.com/dealers/state/NJ/map',
'https://www.stellarhearth.com/dealers/state/NL/map',
'https://www.stellarhearth.com/dealers/state/NS/map',
'https://www.stellarhearth.com/dealers/state/NY/map',
'https://www.stellarhearth.com/dealers/state/OH/map',
'https://www.stellarhearth.com/dealers/state/ON/map',
'https://www.stellarhearth.com/dealers/state/OR/map',
'https://www.stellarhearth.com/dealers/state/PA/map',
'https://www.stellarhearth.com/dealers/state/QC/map',
'https://www.stellarhearth.com/dealers/state/SD/map',
'https://www.stellarhearth.com/dealers/state/SK/map',
'https://www.stellarhearth.com/dealers/state/TN/map',
'https://www.stellarhearth.com/dealers/state/TX/map',
'https://www.stellarhearth.com/dealers/state/UT/map',
'https://www.stellarhearth.com/dealers/state/VA/map',
'https://www.stellarhearth.com/dealers/state/VT/map',
'https://www.stellarhearth.com/dealers/state/WA/map',
'https://www.stellarhearth.com/dealers/state/WI/map']
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass


        
        

    def start_requests(self):
        for url in self.all_urls:
            
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('[class="views-field views-field-field-weblink"]'):
            item = HowardBirnbaumItem()

            try:
                item['company'] = pq(m)('[class="website button"]').attr('title')
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('[class="thoroughfare"]').text()+' '+pq(m)('[class="locality"]').text()
            except Exception as e:
                print (e)        
            try:
                item['state'] = pq(m)('[class="state"]').text()
            except Exception as e:
                print (e)        
            try:
                item['country'] = pq(m)('[class="country"]').text()
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = pq(m)('[class="phone"]').text().replace('Phone:','')
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('[class="website button"]').attr('href')
            except Exception as e:
                print (e)        
            try:
                item['email'] = pq(m)('[class="email"] a').attr('href').replace('mailto:','')
            except Exception as e:
                item['email'] = ''
            try:
                item['city'] = ''
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = pq(m)('[class="postal-code"]').text()
            except Exception as e:
                print (e)
                        
           
    
            yield item
        

    
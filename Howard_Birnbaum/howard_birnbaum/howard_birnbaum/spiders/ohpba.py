# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class ohpba(scrapy.Spider):
    name="ohpba"
    all_urls = [6936232  ,
29374247 ,
6936241  ,
6936206  ,
6936271  ,
27061009 ,
27061041 ,
27061065 ,
27061080 ,
27061098 ,
27061119 ,
27061136 ,
27061236 ,
27061254 ,
6936195  ,
6936196  ,
6936197  ,
6936205  ,
6936225  ,
6936240  ,
6936218  ,
6962634  ,
31768522 ,
31924799 ,
6936212  ,
6936216  ,
6936201  ,
30055239 ,
6936217  ,
6936204  ,
6936198  ,
6936230  ,
6936224  ,
6936203  ,
6936219  ,
6936226  ,
38439723 ,
6936239  ,
6936233  ,
6936247  ,
6936211  ,
11553906 ,
6936207  ,
6936227  ,
11015827 ,
6936236  ,
9925599  ,
6936215  ,
32472189 ,
11139848 ,
6936231  ,
6936214  ,
6936209  ,
6936237  ,
6936223  ,
6936248  
]
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        pass
            


        
        

    def start_requests(self):
        for url in self.all_urls:
            
            yield scrapy.Request(url='http://www.ohpba.org/Sys/PublicProfile/'+str(url)+'/1123683', callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        item = HowardBirnbaumItem()
        try:
            item['company'] = pq('[class="profileHeaderContainer"] h3').text()
        except Exception as e:
            print (e)
        try:
            item['address'] = ''
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
            item['phone_number'] = ''
        except Exception as e:
            print (e)        
        try:
            item['web_site_url'] = pq('[class="fieldBody"] [href*="http"]').text()
        except Exception as e:
            print (e)        
        try:
            item['email'] = pq('[class="fieldBody"] [href*="mailto:"]').text()
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
    

    
# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class ohpba(scrapy.Spider):
    name="ohpba"
    all_urls = ['http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936232/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​29374247/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936241/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936206/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936271/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061009/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061041/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061065/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061080/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061098/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061119/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061136/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061236/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​27061254/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936195/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936196/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936197/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936205/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936225/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936240/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936218/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6962634/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​31768522/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​31924799/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936212/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936216/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936201/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​30055239/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936217/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936204/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936198/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936230/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936224/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936203/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936219/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936226/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​38439723/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936239/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936233/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936247/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936211/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​11553906/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936207/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936227/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​11015827/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936236/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​9925599/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936215/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​32472189/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​11139848/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936231/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936214/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936209/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936237/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936223/​1123683',
'http:​/​/​www.ohpba.org/​Sys/​PublicProfile/​6936248/​1123683'
]
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        pass
            


        
        

    def start_requests(self):
        for url in self.all_urls:
            
            yield scrapy.Request(url=url, callback=self.parse)
    
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
    

    
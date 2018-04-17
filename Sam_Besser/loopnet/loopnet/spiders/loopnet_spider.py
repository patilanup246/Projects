# -*- coding: utf-8 -*-
from loopnet.items import LoopnetItem
import scrapy
import json
import requests
from pyquery import PyQuery
import re
class loopnet(scrapy.Spider):
    name="loopnet"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        self.all_urls = open('urls.txt').read().split('\n')
        
        

    def start_requests(self):
        headers = {
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "en-US,en;q=0.9",
            'Cache-Control': "no-cache",
            #'Connection': "keep-alive",
            'Host': "www.loopnet.com",
            'Pragma': "no-cache",
            'Referer': "http://www.loopnet.com/zip/10001-commercial-real-estate/2",
            'Upgrade-Insecure-Requests': "1",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }
        for url in self.all_urls:
            yield scrapy.Request(url='http://www.loopnet.com/'+url, headers=headers, callback=self.parse)
    
    def parse(self, response):
        item = LoopnetItem()
        resp = response.body_as_unicode()
        pq = PyQuery(resp)
        
        html_text = pq('html').text().lower()
        if 'under contract' in html_text or 'sale pending' in html_text:
            item['found']  =  'YES'
        else:
            item['found']  =  'NO'
        
        try:  
            item['url']  =  str(response.url)
        except Exception as e:  
            item['url']  =  ''
        try:  
            item['price']  =  str(pq('.property-price').text())
        except Exception as e:  
                item['price']  =  ''
        try:  
            item['title']  =  str(pq('.property-info h1').text())
        except Exception as e:  
                item['title']  =  ''
        

        
        yield item
        

    
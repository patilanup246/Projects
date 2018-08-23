# -*- coding: utf-8 -*-

import datetime
from sgpbusiness.items import SgpbusinessItem
import scrapy
import json
import requests
import xmltodict
import random
from pyquery import PyQuery
class sgpc(scrapy.Spider):
    name="linkedin"
    all_urls = open('linkedin_companies.txt').read().split('\n')
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        
        
        
        pass
        

    def start_requests(self):
        for url in self.all_urls:
            a = random.randint(24001,25000)
            http_proxy  = "http://127.0.0.1:{}".format(str(a))
            https_proxy = "https://127.0.0.1:{}".format(str(a))
            ftp_proxy   = "ftp://127.0.0.1:{}".format(str(a))
            proxyDict = { 
                      "http"  : http_proxy, 
                      "https" : https_proxy, 
                      "ftp"   : ftp_proxy
                    }
            headers = {
                #'x-lpm-session': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(26)),
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'upgrade-insecure-requests': "1",
                #'cookie': "__cfduid=d3d9adfa401dd214b99c2746e9714f11f1525713579; sgpbizsess=241e725205c5e36499d341513f115df726da66f8; _ga=GA1.2.1171727646.1525713609; _gid=GA1.2.1016994977.1525713609; _gat=1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
            
                }
            request =  scrapy.Request(url=url.split(',')[1], headers=headers, callback=self.parse)
            request.meta['proxy'] = "https://127.0.0.1:{}".format(str(a))
            yield request
    
    def parse(self, response):
        item = SgpbusinessItem()
        
        pq = PyQuery(response.body_as_unicode())
        
  
                        
        item['company_sgp_url'] = pq('[id="name"]').text()
        
        
        
        
        yield item
        

    
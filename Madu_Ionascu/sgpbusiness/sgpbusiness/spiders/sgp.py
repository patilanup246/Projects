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
    name="sgpbusiness"
    all_urls = open('sgp_companies.txt').read().split('\n')
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
                #'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'upgrade-insecure-requests': "1",
                #'cookie': "__cfduid=d3d9adfa401dd214b99c2746e9714f11f1525713579; sgpbizsess=241e725205c5e36499d341513f115df726da66f8; _ga=GA1.2.1171727646.1525713609; _gid=GA1.2.1016994977.1525713609; _gat=1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
            
                }
            request =  scrapy.Request(url=url, headers=headers, callback=self.parse)
            request.meta['proxy'] = "https://127.0.0.1:{}".format(str(a))
            yield request
    
    def parse(self, response):
        item = SgpbusinessItem()
        
        pq = PyQuery(response.body_as_unicode())
        
        
        company_sgp_url              = response.url
        company_uen                  = ''
        company_raw                  = ''
        company_description          = ''
        company_domain               = ''
        foundingDate = pq('[itemprop="foundingDate"]').text()
        if foundingDate:
            foundingDate = foundingDate.split(' ')
            
            dd = foundingDate[0]
            mm = foundingDate[1][0:3]
            yy = foundingDate[2]
            
            foundingDate = str(datetime.datetime.strptime(dd+mm+yy, '%d%b%Y').strftime("%d/%m/%y"))
            
            
        company_registration_date    = foundingDate
        company_registration_type    = ''
        company_status               = pq('.text-success').text()
        company_status_date          = ''
        industry_raw                 = ''
        company_phone                = ''
        email                        = ''
        company_social_media         = ''
        address                      = ''
        postal_code                  = ''
        Status = ''
        sm_links = []
        for t in pq('.list-group-item'):
            cur_label = pq(t)('.row_label').text()
            
        
            
            if 'Registration No.' == cur_label:
                company_uen = pq(t)('.col-sm-9').text()
                
            if 'Name' == cur_label:
                company_raw = pq(t)('.col-sm-9').text()
                
            if 'Description' == cur_label:
                company_description = pq(t)('.col-sm-9').text()
                
            if 'Website' == cur_label:
                company_domain = pq(t)('.col-sm-9').text()        
                        
            if 'Registration Type' == cur_label:
                company_registration_type = pq(t)('.col-sm-9').text()       
                 
            if 'Status' == cur_label:
                Status = pq(t)('.col-sm-9 small').text()     
                company_status = pq(t)('.col-sm-9 span').text()
            if 'Principal Business Activity' == cur_label:
                industry_raw = pq(t)('.col-sm-9').text()     
                   
            if 'Social Media' == cur_label:
                for sm in pq(t)('.col-sm-9 [itemprop="sameAs"]'):
                    sm_links.append(sm.attrib['href'])
                
            if 'Registration No.' == cur_label:
                company_uen = pq(t)('.col-sm-9').text()
                
            if 'Registration No.' == cur_label:
                company_uen = pq(t)('.col-sm-9').text()
                
        if Status:
            company_status_date = Status.replace('as on ','')
            
#             dd = Status[0]
#             mm = Status[1][0:3]
#             yy = Status[2]
#             try:
#                 company_status_date = str(datetime.datetime.strptime(dd+mm+yy, '%d%b%Y').strftime("%d/%m/%y"))
#             except Exception as e:
#                 pass
                        
        item['company_sgp_url'] = company_sgp_url
        item['company_uen'] = company_uen
        item['company_raw'] = pq('[itemprop="name"]').text()
        item['company_description'] = company_description
        item['company_domain'] = company_domain
        item['company_registration_date'] = company_registration_date
        item['company_registration_type'] = company_registration_type
        item['company_status'] = company_status
        item['company_status_date'] = company_status_date
        item['industry_raw'] = industry_raw
        item['company_phone'] = company_phone
        item['email'] = email
        item['company_social_media'] = ', '.join(sm_links)
        item['address'] = pq('[itemprop="streetAddress"]').text()+' '+ pq('[itemprop="addressCountry"]').text()
        item['postal_code'] = pq('[itemprop="postalCode"]').text()
        
        
        
        yield item
        

    
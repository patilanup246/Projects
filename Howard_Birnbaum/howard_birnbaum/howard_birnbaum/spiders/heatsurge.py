# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class heatsurge(scrapy.Spider):
    name="heatsurge"
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

        for url in self.all_urls:
            url1 = url.split('$')
            req_url = "https://www.heatsurge.com/locator/results_radius.php?s_Dealer_Zip={}&s_Dealer_Radius=25&s_Dealer_Country=&s_Category_ID=&s_Dealer_BusinessName=&s_Dealer_State=".format(str(url1[0]))
            
            yield scrapy.Request(url=req_url, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        if len(pq('[class*="Row"]')) > 1:
            for m in pq('[class*="Row"]'):
                item = HowardBirnbaumItem()
                scrape_item = pq(m)('td:nth-of-type(2)').text().split('\n')
                phone = ''
                email = ''
                
                for si in scrape_item:
                    if 'Phone:' in si:
                        phone = si.replace('Phone: ','')
                    if 'Email:' in si:
                        email = si.replace('Email: ','')
                
                try:
                    item['company'] = pq(m)('td:nth-of-type(2) [id*="BusinessName"]').text().replace(' - Preferred','')
                except Exception as e:
                    print (e)
                try:
                    item['address'] = pq(m)('td:nth-of-type(3)').text()
                except Exception as e:
                    print (e)        
                try:
                    item['state'] = pq(m)('td:nth-of-type(6)').text()
                except Exception as e:
                    print (e)        
                try:
                    item['country'] = pq(m)('td:nth-of-type(8)').text()
                except Exception as e:
                    print (e)        
                try:
                    item['phone_number'] = phone
                except Exception as e:
                    print (e)        
                try:
                    item['web_site_url'] = pq(m)('td:nth-of-type(2) [id*="WebSite"]').text()
                except Exception as e:
                    print (e)        
                try:
                    item['email'] = email
                except Exception as e:
                    print (e)
                try:
                    item['city'] = pq(m)('td:nth-of-type(5)').text().split(',')[0]
                except Exception as e:
                    print (e)
                try:
                    item['postal_code'] = pq(m)('td:nth-of-type(7)').text()
                except Exception as e:
                    print (e)
                            
               
        
                yield item
        

    
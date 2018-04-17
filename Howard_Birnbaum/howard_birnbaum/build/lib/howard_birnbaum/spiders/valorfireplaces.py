# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class valorfireplaces(scrapy.Spider):
    name="valorfireplaces"
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
            req_url = "https://valorfireplaces.com/contact/"
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded",
                'host': "valorfireplaces.com",
                'origin': "https://valorfireplaces.com",
                'pragma': "no-cache",
                'referer': "https://valorfireplaces.com/contact/",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
                }
            payload = "lat=&long=&geo=&myZIPCode={}&radius=300&search=SEARCH".format(str(url1[0]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        #print (response.body_as_unicode())
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('td:nth-of-type(1)'):
            item = HowardBirnbaumItem()
            scrape_item = pq(m)('p').text().split('\n')
            try:
                item['company'] = pq(m)('[class="dealer-titles"]').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = scrape_item[0]
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
                if 'Tel:' in scrape_item[1]:
                    item['phone_number'] = scrape_item[1].split(',')[0].replace('Tel: ','')
                else:
                    item['phone_number'] = ''
            except Exception as e:
                print (e)        
            try:
                if 'Web:' in scrape_item[3]:
                    item['web_site_url'] = scrape_item[3].replace('Web:','')
                else:
                    item['web_site_url'] = ''
            except Exception as e:
                print (e)        
            try:
                if 'E-mail:' in scrape_item[2]:
                    item['email'] = scrape_item[2].replace('E-mail:','')
                else:
                    item['email'] = ''
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
        

    
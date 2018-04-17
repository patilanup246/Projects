# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class rasmussengaslogs(scrapy.Spider):
    name="rasmussengaslogs"
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
            req_url = "http://rasmussen.com.gotlocations.com/index.php"
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded",
                'host': "rasmussen.com.gotlocations.com",
                'origin': "http://rasmussen.com.gotlocations.com",
                'pragma': "no-cache",
                'referer': "http://rasmussen.com.gotlocations.com/index.php",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
                }
            payload = "address={}&Submit=search".format(str(url1[0]))
            yield scrapy.Request(url=req_url, body=payload, headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('[class*="altrow"]'):
            item = HowardBirnbaumItem()
            phone = ''
            scrape_item = pq(m).text().split('\n')
            for s in scrape_item:
                if 'Phone:' in s:
                    phone = s.replace('Phone: ','')
                    break
            try:
                item['company'] = scrape_item[0]
            except Exception as e:
                print (e)
            try:
                item['address'] = scrape_item[1]+' '+scrape_item[2]
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

                item['phone_number'] = phone
    
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('[href*="www"][target="new"]').attr('href')
            except Exception as e:
                item['web_site_url'] = ''       
            try: 
                item['email'] = pq(m)('[href*="mailto:"]').attr('href').replace('mailto:','')
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
    

    
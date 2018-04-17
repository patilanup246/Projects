# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class sehpba(scrapy.Spider):
    name="sehpba"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        i = 1
        headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'cache-control': "no-cache",
            'pragma': "no-cache",
            'referer': "https://sehpba.org/listings-category/retail/page/2/",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
        while True:
            r = requests.get('https://sehpba.org/listings-category/retail/page/'+str(i),headers=headers).text
            pq1 = PyQuery(r)
            i+=1
            
            for p in pq1('.entry-title a'):
                print (p.attrib['href'])
                self.all_urls.append(p.attrib['href'])

            if len(pq1('.entry-title a')) == 0:
                break
            
        
        

    def start_requests(self):
        headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'cache-control': "no-cache",
            'pragma': "no-cache",
            'referer': "https://sehpba.org/listings-category/retail/page/2/",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
        for url in self.all_urls:
            
            yield scrapy.Request( url=url,headers=headers,callback=self.parse)

    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        
        item = HowardBirnbaumItem()
        company = ''
        address = ''
        state = ''
        country = ''
        phone_number = ''
        website = ''
        email = ''
        city = ''
        postal_code = ''
        for i in pq('table tr'):
            print (pq(i)('th').text())
            if 'Business Name' in pq(i)('th').text():
                company = pq(i)('td').text()
            if 'Address 1' in pq(i)('th').text():
                address = pq(i)('td').text()
            if 'State' in pq(i)('th').text():
                state = pq(i)('td').text()
            if 'Phone' in pq(i)('th').text():
                phone_number = pq(i)('td').text()
            if 'Website' in pq(i)('th').text():
                website = pq(i)('td').text()           
            if 'City' in pq(i)('th').text():
                city = pq(i)('td').text()

            if 'Postal Code' in pq(i)('th').text():
                postal_code = pq(i)('td').text()
                
        
        
        try:
            item['company'] = company
        except Exception as e:
            print (e)
        try:
            item['address'] = address
        except Exception as e:
            print (e)        
        try:
            item['state'] = state
        except Exception as e:
            print (e)        
        try:
            item['country'] = country
        except Exception as e:
            print (e)        
        try:
            item['phone_number'] = phone_number
        except Exception as e:
            print (e)        
        try:
            item['web_site_url'] = website
        except Exception as e:
            print (e)        
        try:
            item['email'] = email
        except Exception as e:
            print (e)        
        try:
            item['city'] = city
        except Exception as e:
            print (e)
        try:
            item['postal_code'] = postal_code
        except Exception as e:
            print (e)             

        yield item
        

    
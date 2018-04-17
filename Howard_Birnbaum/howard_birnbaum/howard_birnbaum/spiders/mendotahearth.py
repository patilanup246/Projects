# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class mendotahearth(scrapy.Spider):
    name="mendotahearth"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        pass


        
        

    def start_requests(self):

        yield scrapy.Request(url='http://mendotahearth.com/locator/data/dealers.php?origLat=39.7884076&origLng=-86.28695069999998&origAddress=46214&formattedAddress=Indianapolis%2C%20IN%2046214%2C%20USA&boundsNorthEast=%7B%22lat%22%3A39.823443%2C%22lng%22%3A-86.2668481%7D&boundsSouthWest=%7B%22lat%22%3A39.760383%2C%22lng%22%3A-86.30861089999996%7D',callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        
        for m in r:
            item = HowardBirnbaumItem()
            try:
                item['company'] = str(m['name'])
            except Exception as e:
                print (e)
            try:
                item['address'] = str(m['address'])+' '+str(m['address2'])
            except Exception as e:
                print (e)        
            try:
                item['state'] = str(m['state'])
            except Exception as e:
                print (e)        
            try:
                item['country'] = ''
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = str(m['phone'])
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = str(m['url'])
            except Exception as e:
                print (e)        
            try:
                item['email'] = str(m['email'])
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['zip']
            except Exception as e:
                print (e)
    
            yield item
        

    
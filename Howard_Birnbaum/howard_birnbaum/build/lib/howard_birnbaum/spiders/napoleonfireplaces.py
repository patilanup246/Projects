# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class napoleonfireplaces(scrapy.Spider):
    name="napoleonfireplaces"
    all_urls = [
        'Alabama',
        'Alaska',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Carolina',
        'North Dakota',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'West Virginia',
        'Wisconsin',
        'Wyoming'
    ]
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):

        
        pass

        
        

    def start_requests(self):
        for url in self.all_urls:
            yield scrapy.Request( url='https://hosted.where2getit.com/napoleonfireplaces/ajax?&xml_request=%3Crequest%3E%3Cappkey%3E762598CC-BF23-11DE-8595-0FA33B999D57%3C%2Fappkey%3E%3Cformdata+id%3D%22locatorsearch%22%3E%3Cdataview%3Estore_default%3C%2Fdataview%3E%3Corder%3ERANKING%3A%3Anumeric%2C_distance%3C%2Forder%3E%3Climit%3E250%3C%2Flimit%3E%3Cgeolocs%3E%3Cgeoloc%3E%3Caddressline%3E{}%3C%2Faddressline%3E%3Clongitude%3E%3C%2Flongitude%3E%3Clatitude%3E%3C%2Flatitude%3E%3Ccountry%3EUS%3C%2Fcountry%3E%3C%2Fgeoloc%3E%3C%2Fgeolocs%3E%3Csearchradius%3E250%3C%2Fsearchradius%3E%3Cradiusuom%3Ekm%3C%2Fradiusuom%3E%3Cwhere%3E%3Cor%3E%3Cicon%3E%3Cin%3Enapoleonpromotion%7Cnapoleonpremier%7Celectriconly%7Cdefault%3C%2Fin%3E%3C%2Ficon%3E%3C%2For%3E%3C%2Fwhere%3E%3C%2Fformdata%3E%3C%2Frequest%3E'.format(url.replace(' ','%20')),callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(json.dumps(xmltodict.parse(response.body_as_unicode())))
        
        for m in r['response']['collection']['poi']:
            item = HowardBirnbaumItem()
            try:
                item['company'] = m['name']
            except Exception as e:
                print (e)
            try:
                item['address'] = str(m['address1'])
            except Exception as e:
                print (e)        
            try:
                item['state'] = m['state']
            except Exception as e:
                print (e)        
            try:
                item['country'] = m['country']
            except Exception as e:
                print (e)        
            try:
                item['phone_number'] = m['phone']
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = m['website']
            except Exception as e:
                print (e)        
            try:
                item['email'] = m['contact_email']
            except Exception as e:
                print (e)        
            try:
                item['city'] = m['city']
            except Exception as e:
                print (e)
            try:
                item['postal_code'] = m['postalcode']
            except Exception as e:
                print (e)             
    
            yield item
        

    
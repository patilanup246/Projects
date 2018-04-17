# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class monessenhearth(scrapy.Spider):
    name="monessenhearth"
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
            req_url = "http://www.monessenhearth.com/api/LocatorAjax/LocatorStandardSearch"
            headers = {
                'content-type': "application/json",
                'cache-control': "no-cache"
            }
            payload = {
                "LocatorType": "consumer",
                "CountryCode": "USCA",
                "UserEntry": str(url1[0]),
                "SortType": "award",
                "FuelTypes": "",
                "ProSearchType": "county",
                "ProEntry": "",
                "ProState": "",
                "UISearchCount": 1,
                "UIFirstSearchType": "new search",
                "webapisession": {
                    "rawurl": "/WhereToBuy.aspx",
                    "sitecode": "MON",
                    "site": "MonessenHearth",
                    "sitebrandname": "Monessen Hearth",
                    "siterootpath": "/sitecore/content/monessenhearth home/",
                    "environment": "Production",
                    "sessionid": "a5xecib5qpk5tx2ivcphx4pt",
                    "viewedcoupon": "false",
                    "issyndicatedsession": "false",
                    "dealerid": "",
                    "lastlocatorsearch": "",
                    "debugtracking": "false"
                }
            }
            yield scrapy.Request(method='POST', url=req_url, body=json.dumps(payload) ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        r =  json.loads(response.body_as_unicode())
        try:
            for m in r['locatorsearchresponse']['Dealers']:
                item = HowardBirnbaumItem()
                try:
                    item['company'] = m['Name']
                except Exception as e:
                    print (e)
                try:
                    item['address'] = m['Address1']+' '+m['Address2']
                except Exception as e:
                    print (e)        
                try:
                    item['state'] = m['StateName']
                except Exception as e:
                    print (e)        
                try:
                    item['country'] = m['CountryName']
                except Exception as e:
                    print (e)        
                try:
                    item['phone_number'] = m['Phone']
                except Exception as e:
                    print (e)        
                try:
                    item['web_site_url'] = m['Website']
                except Exception as e:
                    print (e)        
                try:
                    item['email'] = m['LeadEmailAddresses']
                except Exception as e:
                    print (e)        
                try:
                    item['city'] = m['City']
                except Exception as e:
                    print (e)
                try:
                    item['postal_code'] = m['Zip']
                except Exception as e:
                    print (e)  
        
                yield item
        except Exception as e:
            pass
        

    
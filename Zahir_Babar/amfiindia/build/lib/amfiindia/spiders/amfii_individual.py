# -*- coding: utf-8 -*-
from amfiindia.items import AmfiindiaItem
import scrapy
import requests
from pyquery import PyQuery
import urllib

class Amfiindia(scrapy.Spider):
    name="Amfiindia_individual"
    all_urls = []
    def __init__(self, *args,**kwargs):
        try:        
            for p in PyQuery(requests.get('https://www.amfiindia.com/locate-your-nearest-mutual-fund-distributor-details').text)('#NearestFinAdvisorsCity option'):
                city = p.attrib['value']
                if city:
                    self.all_urls.append (city)
             
 
                     
         
        except Exception as e:
            print (e)

        

    def start_requests(self):
        for url in self.all_urls:
            payload = "nfaType=Individual&nfaARN=&nfaARNName=&nfaAddress=&nfaCity={}&nfaPin=".format(urllib.quote_plus(url))
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
            #response = requests.request("POST", "https://www.amfiindia.com/modules/NearestFinancialAdvisorsDetails", data=payload, headers=headers)
            yield scrapy.Request(method='POST', url="https://www.amfiindia.com/modules/NearestFinancialAdvisorsDetails", headers=headers, body=payload, callback=self.parse)
            
    def parse(self, response):
        item = AmfiindiaItem()

        pq = PyQuery(response.body_as_unicode())
        
        for n in pq('table tr'):
            details = []
            for row in pq(n)('td'):
                details.append(str(row.text))
            try:
                item['ARN'] = details[1]
                item['ARN_Holder_Name'] = details[2]
                item['Address'] = details[3]
                item['Pin'] = details[4]
                item['Email'] =    details[5]
                item['City'] =  details[6]
                item['Telephone_R'] =    details[7]
                item['Telephone_O']= details[8]
                item['ARN_Valid_Till'] =    details[9]
                item['ARN_Valid_From'] =   details[10]
                item['KYD_Compliant'] =  details[11]
                item['EUIN'] = details[12]
            
            
            
            
                yield item
            except Exception as e:
                print (e)
        

    
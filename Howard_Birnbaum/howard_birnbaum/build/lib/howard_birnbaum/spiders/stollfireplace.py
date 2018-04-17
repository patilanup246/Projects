# -*- coding: utf-8 -*-
from howard_birnbaum.items import HowardBirnbaumItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery


class stollfireplace(scrapy.Spider):
    name="stollfireplace"
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
            req_url = "https://www.stollfireplace.com/store/dealers"
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded",
                'host': "www.stollfireplace.com",
                'origin': "https://www.stollfireplace.com",
                'pragma': "no-cache",
                'referer': "https://www.stollfireplace.com/store/dealers",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                }
            
            rm = requests.get('https://www.stollfireplace.com/store/dealers',headers=headers)
            pqm = PyQuery(rm.text)
            
            payload = "__VIEWSTATE={}&__VIEWSTATEGENERATOR={}&__EVENTTARGET=&__EVENTARGUMENT=&__EVENTVALIDATION={}&ctl00%24Store_content%24ZipTextBox={}&ctl00%24Store_content%24EnterZipButton=Search".format(pqm('[name="__VIEWSTATE"]').attr('value').replace('/','%2F'),pqm('[name="__VIEWSTATEGENERATOR"]').attr('value').replace('/','%2F'),pqm('[name="__EVENTVALIDATION"]').attr('value').replace('/','%2F'),str(url1[0]))
            yield scrapy.Request(method='POST', url=req_url, body=payload ,headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        pq =  PyQuery(response.body_as_unicode())
        
        for m in pq('.ShellDealer'):
            item = HowardBirnbaumItem()
            try:
                item['company'] = pq(m)('.ShellName').text()
            except Exception as e:
                print (e)
            try:
                item['address'] = pq(m)('.ShellAddress1').text()+' '+ pq(m)('.ShellAddress2').text()+' '+pq(m)('.ShellAddress3').text()
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
                item['phone_number'] = pq(m)('.ShellContact1').text()
            except Exception as e:
                print (e)        
            try:
                item['web_site_url'] = pq(m)('.ShellContact5').text()
            except Exception as e:
                print (e)        
            try:
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
        

    
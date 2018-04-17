# -*- coding: utf-8 -*-
from jobstreet.items import JobstreetItem
import scrapy
import json
import requests
from pyquery import PyQuery
import re
class jobstreet(scrapy.Spider):
    name="jobstreet1"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        pass
        

    def start_requests(self):

        for url in range(1,3000):
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                #'cookie': "solUserId=0a992d05-c0fc-4d84-b988-392846202114; solPreviousSearchHash=3938; solPreviousSearchId=cb736a82-d117-4009-bedb-235c0eb3a3bb; __cfduid=d83c054efe8c08a89ff87a7506fe121e31522504136; _ga=GA1.3.1732307485.1522504136; __utma=1.1732307485.1522504136.1522504139.1522504139.1; __utmz=1.1522504139.1.1.utmcsr=salaryboard.atlassian.net|utmccn=(referral)|utmcmd=referral|utmcct=/wiki/spaces/SCRAP/pages/323321870/JobStreet%20Singapore%20scraper; scs=%7B%22t%22%3A1%7D; s_fid=18637F361E18B065-0DC44CABC98E566C; spUID=15225041458264849250187.ab8a04dd; s_vi=[CS]v1|2D5FC8EA052A3CD1-40000106200001B4[CE]; gatcmr=SGVISITOR; __utma=84921862.1732307485.1522504136.1522552094.1522552094.1; __utmz=84921862.1522552094.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); insSearchParameter=; inslastVisitedUrlus=https%3A%2F%2Fwww.jobstreet.com.sg%2Fen%2Fjob-search%2Fjob-vacancy.php%3Farea%3D1%26option%3D1%26job-source%3D1%252C64%26classified%3D1%26job-posted%3D0%26sort%3D1%26order%3D0%26pg%3D2922%26src%3D16%26srcr%3D1%26ojs%3D4; insdrSV=14; LDSESSIONID=fvtd7c4vhs830ofnrn6eb99ks3; YROTSIH=h%3At%3A%7Bm%3AuE%3A%22QMGU9FP7J_U9UUKML_K8%22%3Bm%3AuA%3A%22VpnkBj6pXmC5EzVy3yAliDDvm5%22%3B%7D; __cfruid=47affe1aefe5d7dda66aad33c9c063d9f299d071-1523076357; TBMCookie_15303015096444475054=752752001523077698MiiRYniVQidI+oq8jFv8dGs5XSg=; ___utmvm=###########; HCRSEABOJ=h%3At%3A%7Bm%3AA%3A%22mhplk2%22%3Bm%3A6t%3A%22+%2B%28mYnlm%3Au%29+%2B%28Zzi_mzo3jl_jzkl%3A%28t+A6+tuC%29%29%22%3B%7D",
                'pragma': "no-cache",
                'upgrade-insecure-requests': "1",
                'user-agent': "mother_of_all_bots_"+str(url)
                }
            yield scrapy.Request(url='https://www.jobstreet.com.sg/en/job-search/job-vacancy.php?area=1&option=1&job-source=1%2C64&classified=1&job-posted=0&sort=1&order=0&pg={}&src=16&srcr=1'.format(str(url)) , headers=headers, callback=self.parse)
    
    def parse(self, response):
        
        resp = response.body_as_unicode()
        #print (resp)
        pq = PyQuery(resp)
        
        for m in pq('.position-title-link'):
            item = JobstreetItem()
            item['url'] = m.attrib['href']

        
            yield item
        

    
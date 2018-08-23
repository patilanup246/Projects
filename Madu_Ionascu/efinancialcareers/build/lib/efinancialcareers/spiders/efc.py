from efinancialcareers.items import EfinancialcareersItem
import scrapy
import requests
from pyquery import PyQuery
import xmltodict
class efinancialcareers(scrapy.Spider):
    name="efinancialcareers"
    all_urls = []
    current_day = ''
    def __init__(self,*args,**kwargs):
        
        page = 1
        first_value = 0
        
        while True:
            querystring = {"page":str(page),"searchMode":"DEFAULT_SEARCH","jobSearchId":"","updateEmitter":"PAGE","filterGroupForm.includeRefreshed":"true","filterGroupForm.datePosted":"OTHER","filterGroupForm.datePosted":"ONE","tileName":"srp", "sortBy" : "POSTED_DESC"}
            print (page)
            headers = {
                'cache-control': "no-cache",
                'host': "www.efinancialcareers.sg",
                'pragma': "no-cache",
                'referer': "https://www.efinancialcareers.sg/search?page=497&searchMode=DEFAULT_SEARCH&jobSearchId=QTcxNUE5QUU2NEI2RTg3QzM3MDAyQjg5Q0M2OUNEMDUuMTUyNDU3NDM5MDQxOC4tMTQ1Mjc4ODU3NQ%3D%3D&updateEmitter=PAGE&filterGroupForm.includeRefreshed=true&filterGroupForm.datePosted=OTHER",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                'x-requested-with': "XMLHttpRequest"
                }
            
            response = requests.request("GET", "https://www.efinancialcareers.sg/getFragment", headers=headers, params=querystring)
            
            
            
            o = xmltodict.parse(response.text)
            
            for i in o['elements']['element']:
                if i['key'] == 'searchResults':
                    pq = PyQuery(i['value'])
                    break
            
            if pq('[id^="jobPreview"]'):
                for p in pq('[id^="jobPreview"]'):
                    if first_value == 0:
                        self.current_day = pq(p)('[class="updated"]').text().split(':')[-1]
                    first_value+=1
                    yesterday_date = pq(p)('[class="updated"]').text().split(':')[-1]
                    self.all_urls.append (pq(p)('h3 a').attr('href').split('?')[0])
                    
            else:
                print ('breaking 1')
                break      
            
            if not self.current_day == yesterday_date:
                print ('breaking 2')
                
                break
            
            print (self.current_day+' -- '+str(page))
            page+=1
        

    def start_requests(self):
        for url in self.all_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = EfinancialcareersItem()
        
        pq = PyQuery(response.body_as_unicode())
        
        item['source_post_id'] = response.url.split('.')[-1]
        
        try:
            item['url'] = response.url
        except:
            item['url'] = ''
            
            
        try:

            item['posted_date'] = self.current_day
        except:
            item['posted_date'] = ''
            
        try:
            item['job_title_raw'] = pq('[itemprop="title"]').text()
        except:
            item['job_title_raw'] = ''
        job_category = ''
        for jc in pq('[class="breadcrumb"] li a'):
            job_category = jc.text
        
        try:
            item['job_category'] = job_category
        except:
            item['job_category'] = ''
            
        try:
            item['job_type'] = pq('[itemprop="employmentType"]').text()
        except:
            item['job_type'] = ''
            
        try:
            item['description'] = pq('.description').text()
        except:
            item['description'] = ''
            
        try:
            item['company_raw'] = pq('.brandInfo h2').text()
        except:
            item['company_raw'] = ''
            
        if 'our client is' in pq('[itemprop="description"].description').text().lower():
            item['company_ad_type'] = 'Recruitment agency'
        else:
            item['company_ad_type'] = 'Direct employer'
            
        try:
            item['country'] = 'SG'
        except:
            item['country'] =''
            
        try:
            item['location'] = pq('[itemprop="addressLocality"]').text()
        except:
            item['location'] = ''
            
        
        if not 'isJobExpired=true' in response.url.split('.')[-1]:
            yield item
        

    
# -*- coding: utf-8 -*-
from jobstreet.items import JobstreetItem
import scrapy
import json
import requests
from pyquery import PyQuery
import re
class jobstreet(scrapy.Spider):
    name="jobstreet"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        page  = 1

        while True:
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'pragma': "no-cache",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                }
            r_m = requests.get('https://www.jobstreet.com.sg/en/job-search/job-vacancy.php?area=1&option=1&job-source=1%2C64&classified=1&job-posted=0&sort=1&order=0&pg={}&src=16&srcr=1'.format(str(page)),headers=headers)
            pq_r = PyQuery(r_m.text)
            a = []
            
            is_yesterday = 0
            for i in pq_r('[id*="job_ad"]'):
                if not 'https://www.jobstreet.com.sg/en/job/1' == pq_r(i)('.position-title-link').attr('href'):
                    if not 'Yesterday' in pq_r(i)('.job-date-text').text():
                        self.all_urls.append(pq_r(i)('.position-title-link').attr('href'))
                    else:
                        is_yesterday = 1
                    
            if is_yesterday:
                break
                    
            
#              
#             if len(pq_r('[itemprop="title"]')) < 20:
#                 break
             

            page+=1
            
            

        
        
        
#         try:        
#             
#             present_guid = []
#             
#             self.scraped_country = country
#             randstad_rss_sg = "https://www.randstad.com.sg/jobs/rss"
#             randstad_rss_uk = "https://www.randstad.co.uk/jobs/rss"
#             randstad_rss_us = "https://www.randstadusa.com/jobs/rss"
#             
#             collection_headers = {
#                 'content-type': "application/json",
#                 'authorization': "Basic MjY5NWZjNjFkMGMxNGUyYWIxMDRlMTgyNTVlN2JiYzQ6"
#             }
#             
#             last_guid = requests.get('https://storage.scrapinghub.com/collections/286560/s/randstad/{}'.format(country), headers=collection_headers).json()['value']
#             
#             
#             if country == "us":
#                 rss_json = xmltodict.parse(requests.get(randstad_rss_us).text)
#                 
#             if country == "uk":
#                 rss_json = xmltodict.parse(requests.get(randstad_rss_uk).text)
#                 
#             if country == "sg":
#                 rss_json = xmltodict.parse(requests.get(randstad_rss_sg).text)
#                 
#             
#             for i in rss_json['rss']['channel']['item']:
#                 present_guid.append(str(i['guid']))
#                 if not str(i['guid']) in last_guid:
#                     self.all_urls.append(str(i['link']))
# 
#             payload = {"_key": country, "value": present_guid}
#             sent_request = requests.request("POST", 'https://storage.scrapinghub.com/collections/286560/s/randstad'.format(country), json=payload, headers=collection_headers)
#             print ('sent_request\n\n'+sent_request.text)
#         
#         except Exception as e:
#             print (e)
        pass
        

    def start_requests(self):
        headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'pragma': "no-cache",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }
        for url in list(set(self.all_urls)):
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
    
    def parse(self, response):
        item = JobstreetItem()
        resp = response.body_as_unicode()
        pq = PyQuery(resp)
        
        job_id = ''
        min_exp = ''
        try:
            j = json.loads(re.findall('window.omniture_settings.contextData = (.*);', resp )[0])
            #print (re.findall('window.omniture_settings.contextData = (.*);', resp )[0])
            job_id= j['JobAd.Id']
            min_exp = j['JobAd.MinExp']
        except Exception as e:
            print (e)
            pass
        
        
        try:  
            item['source_post_id']  =  str(job_id)
        except Exception as e:  
            item['source_post_id']  =  ''
        try:  
            item['url']  =  str(response.url.split('?')[0])
        except Exception as e:  
                item['url']  =  ''
        try:  
            item['posted_date']  =  str(pq('[itemprop="datePosted"]').text()) 
        except Exception as e:  
            item['posted_date']  =  ''
        try:  
            item['close_date']  =  str(pq('[id="closing_date"]').text().split(' ')[-1])
        except Exception as e:  
            item['close_date']  =  ''
        try:  
            item['job_title_raw']  =  str(pq('[id="position_title"]').text())
        except Exception as e:  
            item['job_title_raw']  =  ''
        try:  
            item['job_level']  =  str(re.findall('\((.*?)\)',pq('[itemprop="experienceRequirements"]').text())[0])
        except Exception as e:  
            item['job_level']  =  ''
        try:  
            item['company_raw']  =  str(pq('[id="company_name"]').text().replace('(Recruitment Firm)', ''))
        except Exception as e:  
            item['company_raw']  =  ''
        try:  
            item['company_url']  =  str(pq('[id="company_name"] a').attr('href'))
        except Exception as e:  
            item['company_url']  =  ''
        
        company_type = ''
        company_uen = ''
        if 'RECRUITMENT FIRM' in pq('[itemprop="hiringOrganization"] [class="job-ads-h2"]').text():
            company_type = 'Recruitment agency'
            
            for p in pq('[class="col-lg-6 col-md-6 col-sm-12"]'):
                if 'EA No.' == pq(p)('h3').text():
                    company_uen = pq(p)('p').text()
                    break
        else:
            company_type = 'Direct employer'
            company_uen = str(pq('[id="company_registration_number"]').text())
        try:  
            item['company_type']  =  str(company_type)
        except Exception as e:  
            item['company_type']  =  ''

        try:  
            item['company_uen']  =  str(company_uen)
        except Exception as e:  
                item['company_uen']  =  ''

        try:  
            item['company_domain']  =  str(pq('[id="company_website"]').text())
        except Exception as e:  
            item['company_domain']  =  ''
        try:  
            item['company_size']  =  str(pq('[itemprop="numberOfEmployees"]').text().replace(' Employees','').replace(' Employee','')) 
        except Exception as e:  
            item['company_size']  =  ''
        try:  
            item['company_facebook']  =  str(pq('[id="company_facebook"]').text())
        except Exception as e:  
            item['company_facebook']  =  ''
        try:  
            item['company_phone']  =  str(pq('[itemprop="telephone"]').text())
        except Exception as e:  
                item['company_phone']  =  ''
        try:  
            item['industry_raw']  =  pq('[id="company_industry"]').text()
        except Exception as e:  
                item['industry_raw']  =  ''
        
        try:
            
            item['min_years_experience']  =  str(min_exp)
        except Exception as e:  
                item['min_years_experience']  =  ''
        try:  
            if 'Singapore' in pq('[id="single_work_location"]').text().split(' - ')[0]:
                item['country']  =  'SG'
            else:
                item['country']  =  pq('[id="single_work_location"]').text().split(' - ')[0]
        except Exception as e:  
                item['country']  =  ''
        try:  
            item['location']  =  pq('[itemprop="jobLocation"]').text() 
        except Exception as e:  
                item['location']  =  ''
        try:  
            item['description']  =  pq('[itemprop="description"]').text()  
        except Exception as e:  
                item['description']  =  ''

        
        yield item
        

    
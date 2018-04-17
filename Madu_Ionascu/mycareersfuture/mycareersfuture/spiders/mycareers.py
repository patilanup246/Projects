# -*- coding: utf-8 -*-
from mycareersfuture.items import MycareersfutureItem
import scrapy
import json
import requests
from pyquery import PyQuery
import re
class Mycareersfuture(scrapy.Spider):
    name="mycareersfuture"
    all_urls = open('out.txt').read().split('\n')[0:100]
    
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        pass
        
#         page  = 1
# 
#         while page < 382:
#             headers = {
#                 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#                 'accept-encoding': "gzip, deflate, br",
#                 'accept-language': "en-US,en;q=0.9",
#                 'cache-control': "no-cache",
#                 'connection': "keep-alive",
#                 'host': "api.mycareersfuture.sg",
#                 'pragma': "no-cache",
#                 'upgrade-insecure-requests': "1",
#                 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
#                 }
#             r_m = requests.get('https://api.mycareersfuture.sg/jobs?limit=50&page={}'.format(str(page)),headers=headers)
#             pq_r = json.loads(r_m.json())
#             a = []
#             
#             is_yesterday = 0
#             for i in pq_r('[id*="job_ad"]'):
#                 if not 'https://www.jobstreet.com.sg/en/job/1' == pq_r(i)('.position-title-link').attr('href'):
#                     if not 'Yesterday' in pq_r(i)('.job-date-text').text():
#                         self.all_urls.append(pq_r(i)('.position-title-link').attr('href'))
#                     else:
#                         is_yesterday = 1
#                     
#             if is_yesterday:
#                 break
#                     
#             
# 
#             page+=1
 
        

    def start_requests(self):
        headers = {
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }
        for url in self.all_urls:
        
            yield scrapy.Request(url='https://api.mycareersfuture.sg/job/'+str(url), headers=headers, callback=self.parse)
    
    def parse(self, response):
        item = MycareersfutureItem()
        resp = response.body_as_unicode()
        pq = PyQuery(resp)
        r = json.loads(resp)
        

            
        try:
            item['source_post_id'] = r['job_post_id']
        except Exception as e:  
            print (e)
            
        try:
            item['url'] = 'https://mycareersfuture.sg/job/'+str(r['uuid'])
        except Exception as e:  
            print (e)
            
        try:
            item['applications'] = str(r['total_number_job_application'])
        except Exception as e:  
            print (e)
        org_posting_date =  r['original_posting_date'].split('T')[0].split('-')
        try:
            item['posted_date'] = org_posting_date[2]+'-'+org_posting_date[1]+'-'+org_posting_date[0]
        except Exception as e:  
            print (e)
        close_date = r['expiry_date'].split('T')[0].split('-')
        try:
            item['close_date'] = close_date[2]+'-'+close_date[1]+'-'+close_date[0]
        except Exception as e:  
            print (e)
            
        try:
            item['job_title_raw'] = r['job_title']
        except Exception as e:  
            print (e)
        
        plevels = []
        for pl in r['position_levels']:
            plevels.append(pl)
        
        categories = []
        for cat in r['categories']:
            categories.append(cat)
        
        try:
            item['job_level'] = ', '.join(plevels)
        except Exception as e:  
            print (e)
            
        try:
            item['job_category'] = ', '.join(categories)
        except Exception as e:  
            print (e)
            
        try:
            item['job_type'] = r['employment_types'][0]
        except Exception as e:  
            print (e)
            
        try:
            item['description'] = pq(r['job_description']).text()
        except Exception as e:  
            print (e)
            
        try:
            item['job_requirements'] = pq(r['other_requirements']).text()
        except Exception as e:  
            print (e)
        

        
        skills = []
        for s in r['skills']:
            skills.append(s['skill'])
            
        try:
            item['skills_reference'] = '$'.join(skills)
        except Exception as e:  
            print (e)
             
        try:
            item['company_raw'] =r['employer_name']
        except Exception as e:  
            print (e)
             
        try:
            item['company_logo'] = r['logo_upload_path']
        except Exception as e:  
            print (e)
        
        
        comp_type = ''
        if r['posted_organization_ssic_code'] == r['hiring_organization_ssic_code']:
            comp_type = 'Direct employer'
        else:
            comp_type = 'Recruitment agency'  
        try:
            item['company_type'] = comp_type
        except Exception as e:  
            print (e)
         
        try:
            item['country'] = 'SG'
        except Exception as e:  
            print (e)
             
        try:
            item['location'] = r['building']+' '+r['block']+' '+r['street'] + ' '+ r['postal_code']
        except Exception as e:  
            print (e)
             
        try:
            item['salary_from'] = r['min_monthly_salary']
        except Exception as e:  
            print (e)
             
        try:
            item['salary_to'] = r['max_monthly_salary']
        except Exception as e:  
            print (e)
        try:
            item['salary_currency'] = 'SGD'
        except Exception as e:  
            print (e)
             
        try:
            item['salary_period'] = r['salary_type']
        except Exception as e:  
            print (e)


        
        yield item

        
        
        

    
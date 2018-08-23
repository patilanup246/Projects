# -*- coding: utf-8 -*-
from mycareersfuture.items import MycareersfutureItem
import scrapy
import json
import requests
from pyquery import PyQuery
import re
class Mycareersfuture(scrapy.Spider):
    name="mycareersfuture"
    all_urls = []
    
    scraped_country = ''
    def __init__(self, *args,**kwargs):
        
        
        collection_headers = {
                'content-type': "application/json",
                'authorization': "Basic MjY5NWZjNjFkMGMxNGUyYWIxMDRlMTgyNTVlN2JiYzQ6"
            }
            
        last_guid = requests.get('https://storage.scrapinghub.com/collections/280316/s/mycareersfuture/uuid', headers=collection_headers).json()['value']
        
        page_num = 1
        found = 0
        while True:
            if found == 0:
                r_all = requests.get('https://api.mycareersfuture.sg/jobs?limit=50&sortBy=new_posting_date&page={}'.format(str(page_num))).json()
                
                for rn in r_all['jobs']:
                    if not rn['uuid'] in last_guid:
                        self.all_urls.append(rn['uuid'])
                    else:
                        found = 1
                        break
            else:
                break
            print ('page_num')
            print (page_num)
            page_num +=1
            
            
            
        if  self.all_urls:
            payload = {"_key": 'uuid', "value": self.all_urls}
            sent_request = requests.request("POST", 'https://storage.scrapinghub.com/collections/280316/s/mycareersfuture', json=payload, headers=collection_headers)
            print ('sent_request\n\n'+sent_request.text)
        
 
        

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
            
        building = ''
        block = ''
        street = ''
        postal_code = ''
        
        if r['building']:
            building = str(r['building'])+' '
        
        if r['block']:
            block = str(r['block'])+' '
            
        if r['street']:
            street = str(r['street']) + ' '
            
        if r['postal_code']:
            postal_code = str(r['postal_code'])
        
        try:
            item['location'] = building + block + street + postal_code
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

        
        
        

    
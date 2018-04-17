# -*- coding: utf-8 -*-
from mycareersfuture.items import MycareersfutureItem
import scrapy
import json
import requests
from pyquery import PyQuery
import re
class Mycareersfuture(scrapy.Spider):
    name="mycareersfuture"
    #all_urls = open('out.txt').read().split('\n')[0:100]
    all_urls = ['2d50db7646a0ffb529d70fd61003206e',
'17e835f7d5e002f49d63e425ca067935',
'cb2b6b2036290c18558c374719f5c77e',
'20e4e21021c2bedc10ee3ff3d52d4c06',
'c2ccf1630f1cce4b1f09158193a5b325',
'31eaf203dc799503fd210d4edd09fc4a',
'3268b71233336e9a46260fb7307e0f79',
'ea98628acc3461f40c6df12f52fbe9ac',
'9eed5007098aee37ee48b707f393a84c',
'f56e464d319d501fac851e9df83faf3d',
'b639b8d4830a8dea2ca848ab0918e28b',
'e0d2386d52984aa579b8543e714879d2',
'c1fbc2712cdc0dbb134dd973f9b6c935',
'8e075534700bc95876ff158c51705ddf',
'784b58cb931ebb6f8231fb08b59e3a52',
'81ee5c4c6c85695186376b3d591f7c07',
'e1b5cf8d95e5aa66704c64008c79972d',
'11a828ef917c6c505504571167715b1e',
'b217451745a7d470b63c217196b2e27b',
'e24e0a1e7da71ce2c43872244983107f',
'1ea9b0f87f8645156e1e11fe5c724a2c',
'f9378edaf5a743b165527053b4243b44',
'2eea1cbdff6ba0d39aafff3f0334e0de',
'9747d1409d3a0c522036da43b4206f62',
'3a4b8ef2ddfb9624589d5c986d097335',
'2aed12b60d9f30bf3d772686a3285385',
'ca45e90bf330dd1cd144ae3539d7bb3e',
'e9d451541096fd56413e06c5a86a8f15',
'46e0be435afa8e72d61ef93c8cbd57b7',
'f6f6e34b8a97f0f20ceb3e52555f4efb',
'fd90ce9e859576aa90335c1e279f511d',
'228d40661cb2d382a8fba4fba94f6074',
'138fb3cdb5f83ba91d13a7e581c2bece',
'c442817d7547d2b6723e52fe7662bfed',
'd9732da75ab18766d5c8d96c77de9d51',
'e918ece307e3fd5c6925ccbf8c4fa850',
'5d2441b950b138bd2b6fc29440049f1b',
'a16e4030df5b42fadc807601a110afb4',
'58978f4377fede851e1bb7e4b091aab1',
'dfa6390e9ca181ad76bde89c90029306',
'183dc30d5b7865edbc4b366c3c4baa1c',
'336c24c164a3db72b7bbade95e231086',
'13ab0898dc404420a2f5174c498cdf2a',
'83eb17ceb906963933165a8081abd81f',
'cc1328cd3e7a40e7fffb77c6206a944a',
'50dbdb66e1f8b66e3524081193157ce5',
'ff2bd4b9c16c0bae0e5abd3794cb587a',
'ca52330325ca2c81cc48a0f21fa6f92f',
'a1c4a1a96a50d9957a57209c78bb9ee3',
'2d796ec2ad1b43f37e5e40b1c6f87fde']
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

        
        
        

    
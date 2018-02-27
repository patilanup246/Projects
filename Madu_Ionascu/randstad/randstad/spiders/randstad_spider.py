# -*- coding: utf-8 -*-
from randstad.items import RandstadItem
import scrapy
import json
import requests
import xmltodict
from pyquery import PyQuery
class randstad(scrapy.Spider):
    name="randstad"
    all_urls = []
    scraped_country = ''
    def __init__(self, country = '', *args,**kwargs):
        try:        
            
            present_guid = []
            
            self.scraped_country = country
            randstad_rss_sg = "https://www.randstad.com.sg/jobs/rss"
            randstad_rss_uk = "https://www.randstad.co.uk/jobs/rss"
            randstad_rss_us = "https://www.randstadusa.com/jobs/rss"
            
            collection_headers = {
                'content-type': "application/json",
                'authorization': "Basic MjY5NWZjNjFkMGMxNGUyYWIxMDRlMTgyNTVlN2JiYzQ6"
            }
            
            last_guid = requests.get('https://storage.scrapinghub.com/collections/286560/s/randstad/{}'.format(country), headers=collection_headers).json()['value']
            
            
            if country == "us":
                rss_json = xmltodict.parse(requests.get(randstad_rss_us).text)
                
            if country == "uk":
                rss_json = xmltodict.parse(requests.get(randstad_rss_uk).text)
                
            if country == "sg":
                rss_json = xmltodict.parse(requests.get(randstad_rss_sg).text)
                
            
            for i in rss_json['rss']['channel']['item']:
                present_guid.append(str(i['guid']))
                if not str(i['guid']) in last_guid:
                    self.all_urls.append(str(i['link']))

            payload = {"_key": country, "value": present_guid}
            sent_request = requests.request("POST", 'https://storage.scrapinghub.com/collections/286560/s/randstad'.format(country), json=payload, headers=collection_headers)
            print ('sent_request\n\n'+sent_request.text)
        
        except Exception as e:
            print (e)
        
        

    def start_requests(self):
        for url in self.all_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = RandstadItem()
        
        pq = PyQuery(response.body_as_unicode())
        
        posting_json = {}
        for i in pq('[type="application/ld+json"]'):
            temp_json = json.loads (i.text)
            if temp_json['@type'] == 'JobPosting':
                posting_json = temp_json
                break
        try:
            item['source']             =  str('randstad')
        except:
            item['source']  = ''
        
        try:
            item['country']            =  str(self.scraped_country.upper())
        except:
            item['country'] = ''
        
        try:
            item['job_title_raw']      =  str(posting_json['title'])
        except:
            item['job_title_raw'] = ''
        
        try:
            item['source_post_id']     =  str(posting_json['identifier']['value'])
        except:
            item['source_post_id'] = ''
        
        try:
            item['posted']             =  str(posting_json['datePosted'].replace('Z',''))
        except:
            item['posted']  = ''
        
        try:
            item['location']           =  str(posting_json['jobLocation']['address']['addressLocality'])
        except:
            item['location'] = ''
        
        try:
            item['category']           =  str(posting_json['industry'])
        except:
            item['category']  = ''
        
        try:
            employment_type = str(posting_json['employmentType'])
            if employment_type == 'FULL_TIME':
                item['type']               =  'permanent'
            else:
                item['type']               =  employment_type
        except:
            item['type']  = ''
        
        try:
            item['salary_from']        =  str(posting_json['baseSalary']['value']['minValue'])
        except:
            item['salary_from']  = ''
        
        try:
            item['salary_to']          =  str(posting_json['baseSalary']['value']['maxValue'])
        except:
            item['salary_to'] = ''
        
        try:
            item['salary_currency']    =  str(posting_json['baseSalary']['currency'])
        except:
            item['salary_currency'] = ''
        
        try:
            sp= str(posting_json['baseSalary']['value']['unitText'])
            if 'month' in sp.lower():
                item['salary_period']      =  'monthly'
            if 'year' in sp.lower():
                item['salary_period']      =  'annual'
        except:
            item['salary_period'] = ''
        
        try:
            item['description']        =  str(pq('[class="job-desc"]').html().encode('utf-8'))
        except Exception as e:
            print (e)
            item['description'] = ''
        
        try:
            item['url']                =  str(response.url)
        except:
            item['url'] = ''
        
        try:
            item['reference']          =  str(pq('[id$="ReferenceLabel"]').text().encode('utf-8'))
        except:
            item['reference'] = ''
        
        try:
            item['recruiter_raw']      =  str(pq('[id$="ContactLabel"]').text().split(',')[0]) 
        except:
            item['recruiter_raw'] = ''
        
        
        
        
        yield item
        

    
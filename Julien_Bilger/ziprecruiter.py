# -*- coding: utf-8 -*-
'''
Created on Aug 14, 2018

@author: tasneem
'''
import requests
from pyquery import PyQuery
import re
import csv
import sys
import time
import json
import urllib.parse
from selenium import webdriver
from openpyxl.reader.excel import load_workbook


search_queries = open(sys.argv[1]).read().split('\n')
#search_queries = [str(sys.argv[1])]
#print (search_queries)
try:
    DAYS = str(sys.argv[2])
except: 
    DAYS = '10'

try:
    SALARY = str(sys.argv[3])
except: 
    SALARY = '70000'


try:
    EMPLOYMENT = 'employment_type:'+str(sys.argv[4])
except: 
    EMPLOYMENT = ''


ALL_TEMP_RESULTS = []



OUTPUT_FILE = open('ziprecruiter_output.csv','w', encoding='utf-8', newline='')
WR = csv.writer(OUTPUT_FILE, quoting=csv.QUOTE_ALL)
WR.writerow(['Job posting URL', 'Job Description ', 'Search query', 'Job Title',  'Posted date',    'Payment',    'Employment type',    'Industry',    'Company Name',    'Location'   ])



URL = "https://www.ziprecruiter.com/candidate/search"

HEADERS = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.9",
    'referer': "https://www.ziprecruiter.com/candidate/search?search=Marketing+Manager&days=10&refine_by_salary=&refine_by_tags=&refine_by_title=&refine_by_org_name=",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    
DRIVER = webdriver.Chrome()


def get_location_file():
    try:
        wb = load_workbook('location_list.xlsx')
        sh = wb.active
        j = {}
        for row in sh.rows:
            if row[1].value:
                j[row[0].value] = row[1].value.split(',')
            else:
                j[row[0].value] = []
        return j
    except Exception as e:
        print (e)
        print ('File: location_list.xlsx does not exists')
        sys.exit()
    
def get_result_count(location,search_query):
    '''
    Based on what the input parameters are, this function will either return the count
    of results or the urls of results.
    '''

    querystring = {"include_near_duplicates":"1","days":DAYS,"location":location,"page":"1","refine_by_org_name":"","refine_by_salary":SALARY,"refine_by_tags":EMPLOYMENT,"refine_by_title":"","search":search_query,"no_header_footer":"0"}

    response = requests.request("GET", URL, headers=HEADERS, params=querystring)

    pq = PyQuery(response.text)
    
    headline = pq('#job_results_headline [class="headline"]').text()

    if headline:
        return int(re.findall(r'\d+', headline.split(' ')[0].replace(',',''))[0])
    else:
        return 0
    
    
def get_page_result(location, search_query, pagenum):
    
    querystring = {"include_near_duplicates":"1","days":DAYS,"location":location,"page":str(pagenum),"refine_by_org_name":"","refine_by_salary":SALARY,"refine_by_tags":EMPLOYMENT,"refine_by_title":"","search":search_query,"no_header_footer":"0"}

    response = requests.request("GET", URL, headers=HEADERS, params=querystring)

    pq = PyQuery(response.text)
    
    urls = pq('.job_result')
    
    if urls:
        
        jobs = []
        
        for u in urls:
            
            payment = ''
            job_type = ''
            posted_date = ''
            '''
            This will store partial data in case the link is redirected to external sites
            '''
            for perk in pq(u)('.job_characteristics section'):
                if pq(perk)('h3').text() == 'Pay':
                    payment = pq(perk)('[class="data"]').text()
                if pq(perk)('h3').text() == 'Type':
                    job_type = pq(perk)('[class="data"]').text()
            
            try:
                
                posted_date = re.findall('posted_time=(.*?)T',pq(u)('.job_tools button.job_save').attr('data-href'))[0]
            except Exception as e:
                pass

            x = (
                pq(u)('.job_link').attr('href'),
                pq(u)('[class="job_snippet"]').text(),
                search_query,
                pq(u)('.just_job_title').text(),
                posted_date,
                payment,
                job_type,
                '',
                pq(u)('.name').text(),
                pq(u)('.location').text()
                
                )
            jobs.append(x)
    
        return jobs

    
def get_alien(url1):
    
    url = "https://api.aylien.com/api/v1/extract"
    DRIVER.get(url1)
    time.sleep(10)
    r = DRIVER.current_url
    payload = "url="+urllib.parse.quote(r, safe='')
    
    headers = {
        'x-aylien-textapi-application-key': "41020fd5355e2c76046dc95988b78e37",
        'x-aylien-textapi-application-id': "2921667a",
        'content-type': "application/x-www-form-urlencoded"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    return (response.json()['article'].replace('\n','').replace('\r',''))


file_locations = get_location_file()
print (search_queries)
for sq in search_queries:
    #a variable to store all locations
    TOTAL_LOCATIONS = []
    
    '''
    Get the count of total results worldwide. This will decide if the code is 
    going to run countrywise or country+statewise
    '''
    print ('Running for : '+sq)
    world_count = get_result_count('',sq)
    
    
    print ('Total {} jobs found worldwide for {}'.format(str(world_count),sq))
    '''
    based on the defined criteria
    '''

    if world_count > 400:
        
        for country in file_locations.keys():
            
            country_count = get_result_count(country,sq)
            print ('Total {} jobs found in {} for {}'.format(str(country_count),country,sq))
            if country_count > 400:
                if file_locations.get(country):
                    TOTAL_LOCATIONS.extend(file_locations.get(country))
                else:
                    TOTAL_LOCATIONS.append(country)
                
            else:
                
                TOTAL_LOCATIONS.append(country)

    
    
    if TOTAL_LOCATIONS:
        for tloc in TOTAL_LOCATIONS:
            page_num = 1
            while True:
                print ('Getting results for : {} in {} on page {} '.format(sq,tloc,str(page_num)))
                jobs_results = get_page_result(tloc, sq, page_num)
                if jobs_results:
                    ALL_TEMP_RESULTS.extend(jobs_results)
                else:
                    break
                
                page_num+=1
                
    else:
        page_num = 1
        while True:
            print ('Getting results for : {} worldwide on page {} '.format(sq,str(page_num)))
            urls = jobs_results = get_page_result('', sq, page_num)
            if urls:
                ALL_TEMP_RESULTS.extend(urls)
            else:
                break
            
            page_num+=1



ALL_JOBS = set(ALL_TEMP_RESULTS)
job_num = 0
total_job_length = len(ALL_JOBS)
for url in ALL_JOBS:
    job_num+=1
    try:
        
        url_response = requests.get(url[0],headers=HEADERS)
        
        if 'https://www.ziprecruiter.com' in url_response.url:
            
            print ('Extracting {}/{} : {}'.format(str(job_num),str(total_job_length),url[0].split('?')[0]))
            
            pq = PyQuery(url_response.text)
            
            job_json = json.loads(pq('[type="application/ld+json"]').text())
            
            details = []
            
            details.append (url[0])
            details.append (PyQuery(job_json.get('description','')).text().replace('\n','').replace('\r',''))
            details.append (sq)
            details.append (job_json.get('title',''))
            details.append (job_json.get('datePosted','').split('T')[0])
            details.append (url[5])
            details.append (job_json.get('employmentType',''))
            details.append (job_json.get('industry',''))
            
            details.append (job_json.get('hiringOrganization',{}).get('name',''))
            
            details.append (
                job_json.get('jobLocation',{}).get('address',{}).get('streetAddress','')+' '+
                job_json.get('jobLocation',{}).get('address',{}).get('addressLocality','')+' '+
                job_json.get('jobLocation',{}).get('address',{}).get('addressRegion','')+' '+
                job_json.get('jobLocation',{}).get('address',{}).get('addressCountry','')
                )
            
            
            '''this will only work if the site is ziprecruiter'''
            #wr.writerow(details)
            
            WR.writerow(['N/A' if not v else v for v in details])
            
            
        else:
            '''this will work if the site is external. This will store partial extracted data from job list pages'''
            #print ('Extracting via aylien: {}'.format(url[0]))
            print ('Extracting via aylien: {}/{} : {}'.format(str(job_num),str(total_job_length),url[0].split('?')[0]))
            l = list(url)
            
            try:
                l[1] = get_alien(l[0])
            except Exception as e:
                print (e)
                print ('partial fail')
            
            WR.writerow(['N/A' if not v else v for v in l])
        #wr.writerow(list(url))
            
    except Exception as e:
        
        print (e)
        print ('Total fail')

DRIVER.quit()

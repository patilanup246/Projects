 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import requests 
import random
from pyquery import PyQuery
import random
import csv, sys
# opener = urllib.request.build_opener(
#     urllib.request.ProxyHandler(
#         {'http': 'http://lum-customer-salaryboard-zone-residential:7b238f06f6a0@zproxy.luminati.io:24000'}))
# print(opener.open('https://www.linkedin.com/in/sajith-thomas-8982b6148/').read())


# http_proxy  = "http://127.0.0.1:24001"
# https_proxy = "https://127.0.0.1:24001"
# ftp_proxy   = "ftp://127.0.0.1:24001"
# 
# proxyDict = { 
#               "http"  : http_proxy, 
#               "https" : https_proxy, 
#               "ftp"   : ftp_proxy
#             }
# 
# headers = {
#     'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     'accept-encoding': "gzip, deflate, br",
#     'accept-language': "en-US,en;q=0.9",
#     'cookie': "bcookie=\"v=2&a9656ce8-8b4e-460b-8dc1-afd20d574fd6\"; _ga=GA1.2.1799332824.1519133023; bscookie=\"v=1&201802231542461435e15b-b0a2-4c4e-84ee-bdcb358ecd16AQGMuKd5d-qw9MicXF8hrDxW8AUy5LEg\"; JSESSIONID=ajax:0548361057161073359; lang=\"v=2&lang=en-us\"; visit=\"v=1&G\"; SID=500330ce-fea0-4694-b71d-902eeb01a85f; VID=V_2018_02_28_08_1283; _gat=1; RT=s=1519836648557&r=https%3A%2F%2Fdeveloper.linkedin.com%2Fdocs%2Frest-api; _lipt=CwEAAAFh3VQF391GrlhkWyb2mcM9xWsxQpyMdoChI3btnnebsP28zRZEFyJkC9pNMFH9YVXHWp3vZGlMA0L36qTapacaa6Dw-B3gbLLYaKjLxD8EA_rYyp5cjzScjtMJ4YOKZ2mKraK2R5Xx6B0gJgwoP2PgpdoLGk3gc6lFjrNtP_asae6PADNSKELgRsgXqgAO_EFNooORvzL8IWr9MYhIXe8nGNz-kq7XqzucFltzozzoim1obpIsShn4PyMnbUTSSCRqkBVYVlP_IYT6vyC_pWNL_-lP3wp4i-mKELZWWHmUKdbtMurJlp8AqtyChjsN5Hh-gRYZof73RPKrQGYmcAG4S7xOGEUhX7vDv7Oi7kqZsegkWvZKoXhCGTsxMJ61UJhuSyhnBmMwApMGfK0SS9J40E_M0c67Ji8nHsAsRAGJ1iisue7IaNloQah70ItRW_7D8Wsb7A21KnIdqY9p5B0PqaUqFCXwyQDi5xE5Y6MF3ZbapOurkwWJowUBAgj96uoCvZqUIHRwhT0NBcZ3g1BqqWY; lidc=\"b=VGST07:g=630:u=1:i=1519836739:t=1519923139:s=AQFrC6cRVViNsouKc2PFrBbLcHcMpeaO\"",
#     'upgrade-insecure-requests': "1",
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
#     'cache-control': "no-cache"
#     }
# 
# r = requests.get('https://my.linkedin.com/in/b-manjeet-kaur-sidhu-a9808250', headers=headers, proxies=proxyDict)
# 
# print (r.text)

url = "http://lumtest.com/myip"
output_f1 = open('compare_results.csv','w',encoding='utf-8', newline='')
    
wr = csv.writer(output_f1, quoting=csv.QUOTE_ALL)
wr.writerow(['ID', 'candidate_href',    'name',    'headline',    'location',    'industry',    'intermediate_skills',    'certifications',    'languages',    'job_title_raw_1',    'company_raw_1',    'company_url_1',    'start_1',    'end_1',    'country_1',    'description_1',    'job_title_raw_2',    'company_raw_2',    'company_url_2',    'start_2',    'end_2',    'country_2',    'description_2',    'job_title_raw_3',    'company_raw_3',    'company_url_3',    'start_3',    'end_3',    'country_3',    'description_3',    'job_title_raw_4',    'company_raw_4',    'company_url_4',    'start_4',    'end_4',    'country_4',    'description_4',    'job_title_raw_5',    'company_raw_5',    'company_url_5',    'start_5',    'end_5',    'country_5',    'description_5',    'job_title_raw_6',    'company_raw_6',    'company_url_6',    'start_6',    'end_6',    'country_6',    'description_6',    'job_title_raw_7',    'company_raw_7',    'company_url_7',    'start_7',    'end_7',    'country_7',    'description_7',    'job_title_raw_8',    'company_raw_8',    'company_url_8',    'start_8',    'end_8',    'country_8',    'description_8',    'job_title_raw_9',    'company_raw_9',    'company_url_9',    'start_9',    'end_9',    'country_9',    'description_9',    'job_title_raw_10',    'company_raw_10',    'company_url_10',    'start_10',    'end_10',    'country_10',    'description_10',    'school_name_raw_1',    'school_url_1',    'degree_raw_1',    'education_start_1',    'education_end_1',    'school_name_raw_2',    'school_url_2',    'degree_raw_2',    'education_start_2',    'education_end_2',    'school_name_raw_3',    'school_url_3',    'degree_raw_3',    'education_start_3',    'education_end_3',    'school_name_raw_4',    'school_url_4',    'degree_raw_4',    'education_start_4',    'education_end_4',    'school_name_raw_5',    'school_url_5',    'degree_raw_5',    'education_start_5',    'education_end_5',    'school_name_raw_6',    'school_url_6',    'degree_raw_6',    'education_start_6',    'education_end_6',    'school_name_raw_7',    'institution_url_7',    'degree_raw_7',    'education_start_7',    'education_end_7',    'school_name_raw_8',    'school_url_8',    'degree_raw_8',    'education_start_8',    'education_end_8',    'school_name_raw_9',    'school_url_9',    'degree_raw_9',    'education_start_9',    'education_end_9',    'school_name_raw_10',    'school_url_10',    'degree_raw_10',    'education_start_10',    'education_end_10',])

for m in open('List of URLs v1.0.txt').read().split('\n'):
    details = []
    details.append(m.split(',')[0])
    details.append(m.split(',')[1])
    try:
        #a = random.randrange(24000,24101,1)
        a = 24000
        http_proxy  = "http://127.0.0.1:{}".format(str(a))
        https_proxy = "https://127.0.0.1:{}".format(str(a))
        ftp_proxy   = "ftp://127.0.0.1:{}".format(str(a))
    
        proxyDict = { 
                  "http"  : http_proxy, 
                  "https" : https_proxy, 
                  "ftp"   : ftp_proxy
                }
        headers = {
        'x-lpm-session': ''.join(random.choice('ABCDE') for i in range(5)),
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, sdch, br",
        'accept-language': "en-US,en;q=0.9",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        for i in range(0,5):
            response = requests.request("GET", m.split(',')[1], headers=headers, proxies=proxyDict)
            #print (response.text)
            pq = PyQuery(response.text)
            
            if pq('[id="name"]').text():
                break
        
        
        
        name = ''
        headline = ''
        location = ''
        industry = ''
        
        job_title = ['','','','','','','','','','']
        company = ['','','','','','','','','','']
        company_url = ['','','','','','','','','','']
        start_c = ['','','','','','','','','','']
        end_c = ['','','','','','','','','','']
        country = ['','','','','','','','','','']
        description_c = ['','','','','','','','','','']
        
        
        school_name = ['','','','','','','','','','']
        school_url = ['','','','','','','','','','']
        degree_raw = ['','','','','','','','','','']
        education_start = ['','','','','','','','','','']
        education_end = ['','','','','','','','','','']
        
        skills = []
        certification = []
        languages = []
        
        
        
        
        
        name =  pq('[id="name"]').text()
        headline = pq('[class="headline title"]').text()
        location = pq('[class="locality"]').text()
        industry = pq('[class="descriptor"]').text()
        
        details.append(name)
        details.append(headline)
        details.append(location)
        details.append(industry)
        
        pos_i = 0
        for pos in pq('[class="position"]'):
            if pos_i<10:
                job_title[pos_i] = pq(pos)('[class="item-title"]').text()
                company[pos_i] = pq(pos)('[class="item-subtitle"]').text()
                company_url[pos_i] = pq(pos)('[class="item-subtitle"] a').attr('href')
                #print (pq(pos)('[class="date-range"]').text())
                try:
                    start_c[pos_i] = pq(pos)('[class="date-range"]').text().split('–')[0]
                except:
                    pass
                try:
                    end_c[pos_i] = pq(pos)('[class="date-range"]').text().split('–')[1]
                except:
                    pass
                country[pos_i] = ''
                description_c[pos_i] = pq(pos)('[class="description"]').text()
                
            pos_i+=1
            
        for s in pq('.skill span'):
            skills.append(s.text)
        skills = '$'.join(skills)
        
        details.append(skills)
            
        for c in pq('.certification h4'):
            certification.append(c.text)
        certification = '$'.join(certification)
            
        details.append(certification)
        
        for l in pq('.language h4'):
            languages.append(l.text)
        languages = '$'.join(languages)
        
        details.append(languages)
        
        pos_i = 0
        for pos in pq('[class="school"] '):
            if pos_i<10:
                school_name[pos_i] = pq(pos)('[class="item-title"]').text()
                school_url[pos_i] = pq(pos)('[class="item-title"] a ').attr('href')
                degree_raw[pos_i] = pq(pos)('[class="original translation"]').text()
                try:
                    education_start[pos_i] = pq(pos)('[class="date-range"]').text().split('–')[0]
                except:
                    pass
                try:
                    education_end[pos_i] = pq(pos)('[class="date-range"]').text().split('–')[1]
                except:
                    pass
    
                
            pos_i+=1
        
        for i in range(0,10):
            details.append(job_title[i])
    
            details.append(company[i])
            details.append(company_url[i])
            details.append(start_c[i])
            details.append(end_c[i])
            details.append(country[i])
            details.append(description_c[i])
            
        for i in range(0,10):
            details.append(school_name[i])
            details.append(school_url[i])
            details.append(degree_raw[i])
            details.append(education_start[i])
            details.append(education_end[i])
            
    
            
        #print (details)
    except Exception as e:
        print (e)
    try:
        print (details)
    except:
        pass
    wr.writerow(details)
    #sys.exit()
    
            
    
    
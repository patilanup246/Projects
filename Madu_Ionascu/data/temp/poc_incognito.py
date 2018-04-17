#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 13, 2018

@author: talib
'''
from selenium import webdriver
import csv,time 
import sys
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")
#chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
#chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})
output_f1 = open('compare_results.csv','w',encoding='utf-8', newline='')
driver = webdriver.Chrome(chrome_options=chrome_options)
time.sleep(20)
wr = csv.writer(output_f1, quoting=csv.QUOTE_ALL)
wr.writerow(['ID', 'candidate_href',    'name',    'headline',    'location',    'industry',    'intermediate_skills',    'certifications',    'languages',    'job_title_raw_1',    'company_raw_1',    'company_url_1',    'start_1',    'end_1',    'country_1',    'description_1',    'job_title_raw_2',    'company_raw_2',    'company_url_2',    'start_2',    'end_2',    'country_2',    'description_2',    'job_title_raw_3',    'company_raw_3',    'company_url_3',    'start_3',    'end_3',    'country_3',    'description_3',    'job_title_raw_4',    'company_raw_4',    'company_url_4',    'start_4',    'end_4',    'country_4',    'description_4',    'job_title_raw_5',    'company_raw_5',    'company_url_5',    'start_5',    'end_5',    'country_5',    'description_5',    'job_title_raw_6',    'company_raw_6',    'company_url_6',    'start_6',    'end_6',    'country_6',    'description_6',    'job_title_raw_7',    'company_raw_7',    'company_url_7',    'start_7',    'end_7',    'country_7',    'description_7',    'job_title_raw_8',    'company_raw_8',    'company_url_8',    'start_8',    'end_8',    'country_8',    'description_8',    'job_title_raw_9',    'company_raw_9',    'company_url_9',    'start_9',    'end_9',    'country_9',    'description_9',    'job_title_raw_10',    'company_raw_10',    'company_url_10',    'start_10',    'end_10',    'country_10',    'description_10',    'school_name_raw_1',    'school_url_1',    'degree_raw_1',    'education_start_1',    'education_end_1',    'school_name_raw_2',    'school_url_2',    'degree_raw_2',    'education_start_2',    'education_end_2',    'school_name_raw_3',    'school_url_3',    'degree_raw_3',    'education_start_3',    'education_end_3',    'school_name_raw_4',    'school_url_4',    'degree_raw_4',    'education_start_4',    'education_end_4',    'school_name_raw_5',    'school_url_5',    'degree_raw_5',    'education_start_5',    'education_end_5',    'school_name_raw_6',    'school_url_6',    'degree_raw_6',    'education_start_6',    'education_end_6',    'school_name_raw_7',    'institution_url_7',    'degree_raw_7',    'education_start_7',    'education_end_7',    'school_name_raw_8',    'school_url_8',    'degree_raw_8',    'education_start_8',    'education_end_8',    'school_name_raw_9',    'school_url_9',    'degree_raw_9',    'education_start_9',    'education_end_9',    'school_name_raw_10',    'school_url_10',    'degree_raw_10',    'education_start_10',    'education_end_10',])

for m in open('List of URLs v1.0.txt').read().split('\n'):
    try:
        details = []
        details.append(m.split(',')[0])
        details.append(m.split(',')[1])
        
        
        
        driver.get('https://www.whatismyip.com/')
        driver.get(m.split(',')[1])
        
        
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
        
        
        name =  driver.find_element_by_css_selector('[id="name"]').text
        headline = driver.find_element_by_css_selector('[class="headline title"]').text
        location = driver.find_element_by_css_selector('[class="locality"]').text
        industry = driver.find_element_by_css_selector('[class="descriptor"]').text
        
        details.append(name)
        details.append(headline)
        details.append(location)
        details.append(industry)
        
        pos_i = 0
        for pos in driver.find_elements_by_css_selector('[class="position"]'):
            if pos_i<10:
                try:
                    job_title[pos_i] = pos.find_element_by_css_selector('[class="item-title"]').text
                except:
                    pass
                try:
                    company[pos_i] = pos.find_element_by_css_selector('[class="item-subtitle"]').text
                except:
                    pass
                try:
                    company_url[pos_i] = pos.find_element_by_css_selector('[class="item-subtitle"] a').get_attribute('href')
                except:
                    pass
                #print (pq(pos)('[class="date-range"]').text())
                try:
                    start_c[pos_i] = pos.find_element_by_css_selector('[class="date-range"]').text.split('–')[0]
                except:
                    pass
                try:
                    end_c[pos_i] = pos.find_element_by_css_selector('[class="date-range"]').text.split('–')[1]
                except:
                    pass
                country[pos_i] = ''
                try:
                    description_c[pos_i] = pos.find_element_by_css_selector('[class="description"]').text
                except:
                    pass
            pos_i+=1
            
        for s in driver.find_elements_by_css_selector('.skill span'):
            skills.append(s.text)
        skills = '$'.join(skills)
        
        details.append(skills)
            
        for c in driver.find_elements_by_css_selector('.certification h4'):
            certification.append(c.text)
        certification = '$'.join(certification)
            
        details.append(certification)
        
        for l in driver.find_elements_by_css_selector('.language h4'):
            languages.append(l.text)
        languages = '$'.join(languages)
        
        details.append(languages)
        
        pos_i = 0
        for pos in driver.find_elements_by_css_selector('[class="school"] '):
            if pos_i<10:
                try:
                    school_name[pos_i] = pos.find_element_by_css_selector('[class="item-title"]').text
                except:
                    pass
                try:
                    school_url[pos_i] = pos.find_element_by_css_selector('[class="item-title"] a ').get_attribute('href')
                except:
                    pass
                try:
                    degree_raw[pos_i] = pos.find_element_by_css_selector('[class="original translation"]').text
                except:
                    pass
                try:
                    education_start[pos_i] = pos.find_element_by_css_selector('[class="date-range"]').text.split('–')[0]
                except:
                    pass
                try:
                    education_end[pos_i] = pos.find_element_by_css_selector('[class="date-range"]').text.split('–')[1]
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
            
    
            
    
            print (details)
            wr.writerow(details)
            time.sleep(5)
            driver.delete_all_cookies()
            #driver.quit()
            #sys.exit()
    except Exception as e:
        time.sleep(5)
        pass
    
    
        
'''
Created on Feb 22, 2018

@author: talib
'''

import scrapy
import json
import datetime
import requests
import xmltodict
from pyquery import PyQuery

r = requests.get('https://www.randstad.com.sg/jobs/product-executive-personal-gi-lines_singapore_14755915/').text

pq = PyQuery(r)
posting_json = {}
for i in pq('[type="application/ld+json"]'):
    temp_json = json.loads (i.text)
    if temp_json['@type'] == 'JobPosting':
        posting_json = temp_json
        break
    
print ('randstad')
print (posting_json['jobLocation']['address']['addressCountry'])
print (posting_json['title'])
print (posting_json['identifier']['value'])
print (posting_json['datePosted'])
print (posting_json['jobLocation']['address']['addressLocality'])
print (posting_json['industry'])
print (posting_json['employmentType'])
print (posting_json['baseSalary']['value']['minValue'])
print (posting_json['baseSalary']['value']['maxValue'])
print (posting_json['baseSalary']['currency'])
print (posting_json['baseSalary']['value']['unitText'])
print (posting_json['description'])
print (pq('[id$="ReferenceLabel"]').text())
print (pq('[id$="ContactLabel"]').text().split(',')[0])



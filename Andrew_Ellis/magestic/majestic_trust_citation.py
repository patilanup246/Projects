# -*- coding: utf-8 -*-
'''
Created on May 3, 2018

@author: talib
'''
import requests
import re
import urllib3
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {
    'origin': "https://majestic.com",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "_ga=GA1.2.2082427430.1523663013; STOK=R90aCJs3Pyb1rSFfs1OzKxfmk7; _gid=GA1.2.650315579.1524976007; _gat=1"
    }
output_f = open('trust_citation.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['URL','Trust Score','Citation Score'])

for u in open('urls.txt').read().split('\n'):
    details = []
    details.append(u)
    try:
        u = u.replace('http://','').replace('https://','').replace('/','').replace('\\','')
        url = 'https://majestic.com/reports/site-explorer?folder=&q={}&IndexDataSource=F'.format(u)
        r = requests.get(url,headers=headers,verify=False)
        trust_scrore = re.findall('var trustFlow = (.*?);', r.text)[0]
        citation_score = re.findall('var citationFlow = (.*?);', r.text)[0]
        
        details.append(str(trust_scrore))
        details.append(str(citation_score))
        
    except Exception as e:
        print (e)
    wr.writerow(details)
    print (details)
        
# -*- coding: utf-8 -*-
'''
Created on Jul 27, 2018

@author: tasneem
'''
import requests

url = "https://www.starbucks.com/bff/locations"

locations = open('location.txt').read().split('\n')
import csv
output_f = open('starbucks.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Name',    'Store Number',    'Phone Number',    'Address'])


for l in locations:
    querystring = {"place":str(l)}
    
    headers = {
        'accept': "application/json",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'x-requested-with': "XMLHttpRequest"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        for loc in response.json()['stores']:
            details = []
            details.append( loc['name'])
            details.append( loc['storeNumber'])
            details.append( loc['phoneNumber'])
            details.append( ', '.join(loc['addressLines']))
            print (details)
            wr.writerow(details)
    except Exception as e:
        print (e)
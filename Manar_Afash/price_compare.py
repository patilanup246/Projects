# -*- coding: utf-8 -*-
'''
Created on 06-Feb-2018

@author: Administrator
'''
import requests, csv, os, re, json
from datetime import datetime







inputs = []
readCSV1 = csv.reader(open('input_file.csv',encoding='utf-8'), delimiter=',')

for c in readCSV1:
    inputs.append(c)



output_f1 = open('compare_results_{}.csv'.format(str(datetime.now()).replace(':','')),'w',encoding='utf-8', newline='')
wr1 = csv.writer(output_f1, quoting=csv.QUOTE_ALL)
wr1.writerow(['SKU', 'URL', 'Old Price', 'new Price', 'Stock'])

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    'referer': "https://www.toysrus.com/subcat?categoryid=119271406",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    
i = 0
for c in inputs:
    if not i == 0:
        print (c[0])
        if 'walmart' in c[1]:
            try:
                pwid = str(c[1].split('?')[0].split('/')[-1])
                rw = requests.get('http://api.walmartlabs.com/v1/items/{}?apiKey=x4ucjjdxmfn8ghw5963je835&format=json'.format(pwid)).json()
                
                if not str(c[2]) == str(rw['salePrice']):
                    issue = []
                    issue.append(str(c[0]))
                    issue.append(str(c[1]))
                    issue.append(str(c[2]))
                    issue.append(str(rw['salePrice']))
                    issue.append(str(rw['stock']))
                    wr1.writerow(issue)
                    
            except Exception as e:
                print (e)
        if 'toysrus' in c[1]:
            try:
                rw = requests.get(str(c[1]),headers=headers).text
                print (str(c[1]))
                j = json.loads (re.findall(r'window.__INITIAL_STATE__ = (.*)',rw)[0])
                if not str(c[2]) == str(j['productDetails']['product']['price']):
                    issue = []
                    issue.append(str(c[0]))
                    issue.append(str(c[1]))
                    issue.append(str(c[2]))
                    issue.append(str(j['productDetails']['product']['price']))
                    if str(j['productDetails']['product']['isOutOfStock']) == 'False':
                        try:
                            issue.append(str(j['productDetails']['SKUsList'][0]['shipping']['shipToHome']['onlineStore']['productInventory']['quantity']))
                        except:
                            issue.append('Available')
                    else:
                        issue.append('Not Available')
                    wr1.writerow(issue)
                    
                
            except Exception as e:
                print (e)
            
                
    i+=1
    
        


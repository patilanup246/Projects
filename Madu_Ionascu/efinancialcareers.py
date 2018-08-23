# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery
url = "https://www.efinancialcareers.sg/getFragment"
import xmltodict
page = 1
first_value = 0
current_day = ''
while True:
    querystring = {"page":str(page),"searchMode":"DEFAULT_SEARCH","jobSearchId":"","updateEmitter":"PAGE","filterGroupForm.includeRefreshed":"true","filterGroupForm.datePosted":"OTHER","filterGroupForm.datePosted":"ONE","tileName":"srp"}
    print (page)
    headers = {
        'cache-control': "no-cache",
        'host': "www.efinancialcareers.sg",
        'pragma': "no-cache",
        'referer': "https://www.efinancialcareers.sg/search?page=497&searchMode=DEFAULT_SEARCH&jobSearchId=QTcxNUE5QUU2NEI2RTg3QzM3MDAyQjg5Q0M2OUNEMDUuMTUyNDU3NDM5MDQxOC4tMTQ1Mjc4ODU3NQ%3D%3D&updateEmitter=PAGE&filterGroupForm.includeRefreshed=true&filterGroupForm.datePosted=OTHER",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'x-requested-with': "XMLHttpRequest"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    
    
    o = xmltodict.parse(response.text)
    
    for i in o['elements']['element']:
        if i['key'] == 'searchResults':
            pq = PyQuery(i['value'])
            break
    
    if pq('[id^="jobPreview"]'):
        for p in pq('[id^="jobPreview"]'):
            if first_value == 0:
                current_day = pq(p)('[class="updated"]').text().split(':')[-1]
            first_value+=1
            yesterday_date = pq(p)('[class="updated"]').text().split(':')[-1]
            print (pq(p)('[class="updated"]').text())
            print (pq(p)('h3 a').attr('href'))
            
    else:
        print ('breaking 1')
        break      
    
    if not current_day == yesterday_date:
        print ('breaking 2')
        
        break

    
    page+=1
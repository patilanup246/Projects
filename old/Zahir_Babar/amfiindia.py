'''
Created on 02-Jan-2018

@author: Administrator
'''
import requests
from pyquery import PyQuery
import csv
import urllib.parse

cities = []
output_f = open('amfi.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
for p in PyQuery(requests.get('https://www.amfiindia.com/locate-your-nearest-mutual-fund-distributor-details').text)('#NearestFinAdvisorsCity option'):
    city = p.attrib['value']
    if city:
        cities.append (city)
        
cities = list(set(cities))

for city in cities:
    print (city)
    url = "https://www.amfiindia.com/modules/NearestFinancialAdvisorsDetails"
    print (urllib.parse.quote_plus(city))
    #payload = "nfaType=Corporate&nfaARN=&nfaARNName=&nfaAddress=&nfaCity={}&nfaPin=".format(urllib.parse.quote_plus(city))
    payload = "nfaType=Individual&nfaARN=&nfaARNName=&nfaAddress=&nfaCity={}&nfaPin=".format(urllib.parse.quote_plus(city))
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.request("POST", url, data=payload, headers=headers)
    pq = PyQuery(response.text)
    for n in pq('table tr'):
        details = []
        for row in pq(n)('td'):
            details.append(str(row.text))
        wr.writerow(details)
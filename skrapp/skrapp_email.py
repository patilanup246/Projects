'''
Created on Feb 25, 2018

@author: talib
'''

import csv
import requests



url = "https://api.skrapp.io/api/v2/find"



headers = {
    'x-access-key': "1048168428FAgfKvbx62eHVZbqRYSNRtN9fohRNw7c",
    'cache-control': "no-cache"
    }






output_f = open('output_results.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)

cs1 = []
readCSV1 = csv.reader(open('input_csv.csv',encoding='utf-8'), delimiter=',')

for row in readCSV1:
    cs1.append(row)
i = 0
for c in cs1:
    details = c
    if i > 3417:
        
        try:
            querystring = {"firstName":c[4],"lastName":c[5],"domain":c[7]}
            response = requests.request("GET", url, headers=headers, params=querystring)
            
            #print()
            details[10]=response.json()['email']
            print (response.json()['email'])
        except Exception as e:
            print (response)
    wr.writerow(details)
    i+=1
    

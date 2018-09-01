# -*- coding: utf-8 -*-
'''
Created on Aug 10, 2018

@author: tasneem
'''

import csv
import requests
import urllib.parse
import sys

output_f = open('concepts_output.csv','w', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Concept', 'No. of times it appeared'  ])



url = "https://api.aylien.com/api/v1/concepts"
headers = {
    'x-aylien-textapi-application-key': "41020fd5355e2c76046dc95988b78e37",
    'x-aylien-textapi-application-id': "2921667a",
    'content-type': "application/x-www-form-urlencoded"
    }

#x = json.loads(open('sec1.txt').read())



readCSV1 = csv.reader(open(sys.argv[1],encoding='ISO-8859-1'), delimiter=',')




concepts_store = []
all_concepts = []
row_num = 1
for row in readCSV1:
    print ('Extracting concept : '+ str(row_num))
    try:
        
        payload = "text="+urllib.parse.quote(row[1], safe='')
    
        response = requests.request("POST", url, data=payload, headers=headers)
        x = response.json()
        
        concepts = []
        for a in x['concepts'].keys():
            concept = x['concepts'][a]['surfaceForms'][0]['string']
            concepts.append (concept.lower())
            all_concepts.append(concept.lower())
            
        concepts_store.append('~~'.join(set(concepts)))
    except Exception as e:
        print (e)

    row_num += 1

for ac in set(all_concepts):
    i = 0
    for cs in concepts_store:
        if ac.lower() in cs.split('~~'):
            i+=1
    wr.writerow([ac,str(i)])
    
    


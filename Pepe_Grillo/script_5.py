'''
Created on Jun 14, 2018

@author: tasneem
'''

import xmltodict
import requests
import json
import csv

readCSV1 = csv.reader(open('linkedin_messages.csv',encoding='utf-8'), delimiter=',')
cc = []
for row in readCSV1:
    cc.append (row)
output_f = open('linkedin_messages.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
for c in cc:
    if c[2]:
        try:
            to_send_message = 'Hi {}, saw a few job postings come in that made me think of you:'.format(c[1])+'\n\n'
            for j in xmltodict.parse(requests.get(c[2]).text)['rss']['channel']['item']:
                to_send_message += j['link']+'\n'
            c[5] = to_send_message
        except Exception as e:
            print (e)
    wr.writerow(c)
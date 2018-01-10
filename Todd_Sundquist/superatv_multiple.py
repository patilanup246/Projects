'''
Created on 03-Jan-2018

@author: Administrator
'''
import requests
import re
from pyquery import PyQuery
import json
import xmltodict, json
import csv
output_f = open('superatv_export_new.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
for jj in open('superatv.txt').read().split('\n'):
    try:
        r = requests.get(jj).text
        output_f.write(r)
        print (len(re.findall(r'jsonConfig: (.*),',r)))
        json.loads (re.findall(r'jsonConfig: (.*),',r)[0])
    except Exception as e:
        print (e)
        
    break
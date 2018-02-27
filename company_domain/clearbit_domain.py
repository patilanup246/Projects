'''
Created on Feb 25, 2018

@author: talib
'''
import requests
o = open('output.txt','w',encoding="utf-8")
url = "https://company.clearbit.com/v1/domains/find"


headers = {
    'authorization': "Basic c2tfNTA5NmIyMWNmNTdjZTg4ZWFjYWI4NDZkOTIwZTgyYzM6",
    'cache-control': "no-cache"
    }

for i in open('input.txt',encoding="utf-8").read().split('\n'):
    querystring = {"name":i}
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        print (response.json()['domain'])
        o.write(response.json()['domain'])
    except:
        o.write('')
        
    o.write('\n')
    o.flush()
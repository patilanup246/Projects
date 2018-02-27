'''
Created on Feb 19, 2018

@author: talib
'''
import requests, csv, os
from pyquery import PyQuery

from glob import glob

output_f = open('extrememetalproducts.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['id',    'title',    'company',    'biography',    'user_id',    'tags',    'birth_date',    'website_url',    'linkedin_url',    'facebook_url',    'twitter_username',    'weight',    'country',    'avatar',    'cover',    'type',    'name',    'bookmarked'])

headers = {
    'x-client-id': "41cbd877e282b1a0c3349df1d0de8d9be5f0217e65e5e0c66cfa8cdb32d1b24f",
    'if-none-match': "W/\"2ab0d2dcb286f0ba3b9c4624385e239c\"",
    'x-user': "UYPh93g-JC7hEq9t3mxs",
    'accept-language': "en-US",
    'host': "api.eventtus.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.9.0",
    'cache-control': "no-cache"
    }
for i in range(1,10):
    print (i)
    r = requests.get('https://api.eventtus.com/api/events/d4v19kyq9zhkswg3rnzgk2l25zeom9cm/speakers?page={}&per_page=50'.format(str(i)), headers= headers, verify=False).json()
    
    for user in r:
        details = []
        
        details.append(user['id'])
        details.append(user['title'])
        details.append(user['company'])
        details.append(user['biography'])
        details.append(user['user_id'])
        tags = []
        for tag in user['tags']:
            tags.append(tag)
        details.append(', '.join(tags))
        details.append(user['birth_date'])
        details.append(user['website_url'])
        details.append(user['linkedin_url'])
        details.append(user['facebook_url'])
        details.append(user['twitter_username'])
        details.append(user['weight'])
        details.append(user['country'])
        details.append(user['avatar']['large'])
        details.append(user['cover']['large'])
        details.append(user['type'])
        details.append(user['name'])
        details.append(user['bookmarked'])
        
        

        
        wr.writerow(details)
    
    
'''
Created on May 4, 2018

@author: talib
'''


import requests
import json

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

for s in states:
    
    r = requests.get('http://doppler.finra.org/doppler-lookup/api/v1/search/individuals?hl=true&includePrevious=true&nrows=12&r=25&sort=score+desc&state={}&wt=json'.format(s)).json()
    #print (json.dumps(r))
    
    for p in r['results']['BROKER_CHECK_REP']['results']:
        print (p['fields']['bc_source_id'])
    
    #print (s+'\t'+str(r['results']['BROKER_CHECK_REP']['totalResults']))
    
#     r = requests.get('http://doppler.finra.org/doppler-lookup/api/v1/search/firms?hl=true&includePrevious=true&nrows=12&r=25&sort=score+desc&state={}&wt=json'.format(s)).json()
#     print (json.dumps(r))
#     print (s+'\t'+str(r['results']['BROKER_CHECK_FIRM']['totalResults']))
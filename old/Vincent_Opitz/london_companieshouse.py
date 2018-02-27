'''
Created on 07-Nov-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery

starting_url = "https://beta.companieshouse.gov.uk/search/companies"

output_file = open('london_output.txt','w')

for url in open('london.txt').read().split('\n'):
    querystring = {"q":url}
    response = requests.request("GET", starting_url, params=querystring)

    pq = PyQuery(response.text)
    
    a =  (str(pq('.type-company:nth-child(1) a').text().strip())+'\t'+str(pq('.type-company:nth-child(1) a').attr('href'))+'\t'+str(pq('.type-company:nth-child(1) p:nth-child(3)').text().strip()))
    print (a)
    output_file.write(a+'\n')
    output_file.flush()
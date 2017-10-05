'''
Created on May 20, 2017

@author: Mukadam
'''
from pyquery import PyQuery
import requests
file_company_input = open('file_company_input.txt','r').read().split('\n')
file_company_output = open('file_company_output.txt','a')
for site in file_company_input:
    
    try:
        url = "https://www.bing.com/search"
    
        querystring = {"q":'"https://www.linkedin.com/company/" '+site.split('\t')[0],"go":"Search","qs":"bs","form":"QBRE"}
    
    
        response = requests.request("GET", url, params=querystring)    
        pq = PyQuery(response.text)
        
        linkedin_url = pq('.b_algo h2 a')[0].attrib['href']
        #print linkedin_url
    
        
        file_company_output.write(site.split('\t')[0]+'\t'+linkedin_url+'\t'+ site.split('\t')[1]+'\n')
        file_company_output.flush()
    except:
        file_company_output.write(site.split('\t')[0]+'\t'+'\t'+ site.split('\t')[1]+'\n')
        file_company_output.flush()
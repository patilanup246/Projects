
'''
Created on May 19, 2018

@author: talib
'''

# from selenium import webdriver
import time
# options = webdriver.ChromeOptions() 
# options.add_argument("user-data-dir=C:\\Users\\talib\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
# driver = webdriver.Chrome(chrome_options=options)
# 
# f = open('sgp_out.txt','a')
# 
# driver.get('https://www.sgpbusiness.com/browse/A/after/815860/')
# 
# while True:
#     try:
#         for l in driver.find_elements_by_css_selector('.list-group a'):
#             #print (l.get_attribute('href'))
#             f.write(l.get_attribute('href')+'\n')
#             f.flush()
#         time.sleep(20)
#         print (driver.find_element_by_css_selector('[class="next"] a').get_attribute('href'))
#         
#         driver.find_element_by_css_selector('[class="next"] a').click()
#     
# 
#     except Exception as e:
#         print (e)
#     
#     


import requests
from pyquery import PyQuery
url = "https://www.sgpbusiness.com/search"


headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded",
    'origin': "https://www.sgpbusiness.com",
    #'cookie': "__cfduid=dbd33060d5ca8c09500f853a22ccafcc11526030630; _ga=GA1.2.1937662851.1526030632; _gid=GA1.2.412763831.1526710953; sgpbizsess=a2504243407a7eb0a29ef82e447a5b0a43f37d1a; _gat=1",
    'referer': "https://www.sgpbusiness.com/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    }
f = open('sgp_out.txt','a')
li = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    for j in li:
        for k in li:
            payload = "search_val={}".format(i+j+k)
            response = requests.request("POST", url, data=payload, headers=headers)
            
            pq = PyQuery(response.text)
            
            
            links = pq('.list-group a')
            print (i+j+k+' - '+str(len(links)))
            for l in links:
                #print (l.attrib['href'])
                f.write(l.attrib['href']+'\n')
                f.flush()
                
            #time.sleep(2)


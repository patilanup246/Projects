# -*- coding: utf-8 -*-
'''
Created on 27-Jan-2018

@author: Administrator
'''
import requests, csv
from pyquery import PyQuery

#driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')


output_f = open('urls.txt','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow([])
products_url = ''
##tjp-control-paging li[class] a

year = ['2013','2014','2015','2016','2017']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
headers = {
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'Accept-Encoding': "gzip, deflate",
                'Accept-Language': "en-US,en;q=0.9",
                'Cache-Control': "no-cache",
                'Connection': "keep-alive",
                'Host': "www.thejakartapost.com",
                'Pragma': "no-cache",
                'Upgrade-Insecure-Requests': "1",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
            }

# for y in year:
#     for m in months:
#         for d in days:
#             print (d+'-'+m+'-'+y)
#             url = "http://www.thejakartapost.com/paper/todays-paper/page/{}/{}/{}".format(m,d,y)
#             response = requests.request("GET", url, headers=headers)
#             pq = PyQuery(response.text)
#             for p in pq('#tjp-control-paging li[class] a'):
#                 output_f.write(p.attrib['href']+'\n')
#                 output_f.flush()

for i in range(1,3505):
    print (i)
    url = "http://www.thejakartapost.com/news/index/page/{}".format(str(i))
    response = requests.request("GET", url, headers=headers)
    pq = PyQuery(response.text)
    for p in pq('.detail-latest a:nth-child(2)'):
        #print (p.attrib['href'])
        output_f.write(p.attrib['href']+'\n')
        output_f.flush()
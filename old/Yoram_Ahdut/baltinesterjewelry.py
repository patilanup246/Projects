'''
Created on 19-Dec-2017

@author: Administrator
'''

import requests
from pyquery import PyQuery

store_results = open('results.txt','w')

for i in range(1,7):
    page_num = 1
    while True:
        print (str(i)+'--'+str(page_num))
        resp = requests.get('http://www.baltinesterjewelry.com/searchresults.aspx?q=&artistid=0&budgetchoice={}&categoryid=0&subcategoryid=0&p={}'.format(str(i),str(page_num))).text
        pq = PyQuery(resp)
        if len(pq('[class="leftext"] a')) == 0:
            break
        for p in pq('[class="leftext"] a'):
            store_results.write(p.attrib['href']+'\n')
            store_results.flush()
        page_num+=1
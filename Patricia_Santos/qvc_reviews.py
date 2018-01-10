# -*- coding: utf-8 -*-
'''
Created on 06-Jan-2018

@author: Administrator
'''
import requests
from pyquery import PyQuery
import csv,re,json
output_f = open('qvc_output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Product name','Product URL','User Name','Title','Review Text','Rating','Date','Avatar'])


products_url = 'https://www.qvc.com/catalog/search.html?langId=-1&storeId=10251&catalogId=10151&keyword=volition+beauty'

pq_p = PyQuery(requests.get(products_url).text)
for product in pq_p('.galleryItem'):
    product_id = pq_p(product)('a').attr('href').replace('.html','').split('.')[-1]
    product_link = pq_p(product)('a').attr('href')
    product_name = pq_p(product)('.productDesc').text()
    print (product_id)
    
    page = 1
    while True:
        r = requests.get('http://qvc.ugc.bazaarvoice.com/1689wcs-en_us/{}/reviews.djs?format=embeddedhtml&page={}&scrollToTop=true'.format(product_id,str(page)))        
        pq = PyQuery(json.loads(re.findall(r'materials=(.*),',r.text)[0])['BVRRSourceID'])
        for p in pq('#BVSubmissionPopupContainer'):
            details = []
            details.append(product_name)
            details.append(product_link)
            details.append(pq(p)('.BVRRNickname').text())
            #print (pq(p)('.BVRRNickname').text())
            details.append(pq(p)('.BVRRReviewTitle').text())
            details.append(pq(p)('.BVRRReviewTextContainer').text())
            details.append(pq(p)('.BVRRRatingNumber').text())
            details.append(pq(p)('[itemprop="datePublished"]').attr('content'))
            details.append('')
            wr.writerow(details)
            #print (p.text)
        
        if len(pq('[class="BVRRValue BVRRReviewTitle"]')) < 8:
            break
        
        page+=1
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery
import requests
import csv
# f = open('info.txt','w')
# for i in range(90,160):
#     r = requests.get('https://websta.me/category?page={}&sort='.format(str(i)))
#     pq = PyQuery(r.text)
#     print (i)
#     for p in pq('tbody tr'):
#         f.write(pq(p)('.username a').attr('href')+'\t'+pq(p)('.username div').text()+'\n')
#         f.flush()


f = open('info.txt','r').read()
output_f = open('insta_output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
for pro in f.split('\n'):
    try:
        details = []
        ig_handle =  pro.split('\t')[1]
        print (ig_handle)
        details.append (ig_handle)
        r = requests.get('https://websta.me'+pro.split('\t')[0])
        pq = PyQuery(r.text)
        a = pq('.count.col-xs-4 strong').text().split(' ')
        details.append(pq('p.userinfo-xs').text())
        posts = a[0]
        followers = a[1]
        followings =  a[2]
        details.append(posts)
        details.append(followers)
        details.append(followings)
        details.append(pq('.small-box.bg-red h3').text())
        details.append(pq('.small-box.bg-yellow h3').text())
        print (a)
        last_update_likes = pq('[class^="likesCount_"]').text()
        
        for p in (pq('[class="media-attr"]')):
            lc = pq(p).text().split(' ')
            details.append(lc[0])
            details.append(lc[2])
            
        
        #print (details)
        
        wr.writerow(details)
    except Exception as e:
        print (e)
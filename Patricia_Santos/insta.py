#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery
import requests

# f = open('info.txt','w')
# for i in range(90,160):
#     r = requests.get('https://websta.me/category?page={}&sort='.format(str(i)))
#     pq = PyQuery(r.text)
#     print (i)
#     for p in pq('tbody tr'):
#         f.write(pq(p)('.username a').attr('href')+'\t'+pq(p)('.username div').text()+'\n')
#         f.flush()


f = open('info.txt','r').read()
f1 = open('info_final.txt','w')
for pro in f.split('\n'):
    ig_handle =  (pro)
    print (pro)
    r = requests.get('https://websta.me'+pro.split('\t')[0])
    pq = PyQuery(r.text)
    a = pq('.count.col-xs-4 strong').text().split(' ')
    posts = a[0]
    followers = a[1]
    followings =  a[2]
    print (a)
    last_update_likes = pq('[class^="likesCount_"]').text()
    for p in (pq('[class="media-attr"]')):
        b = pq(p).text().split(' ')
        break
    
    print (b)
    
    f1.write(pro.split('\t')[1]+'\t'+pq('.count.col-xs-4:nth-child(1) strong').text()+'\t'+pq('.count.col-xs-4:nth-child(2) strong').text()+'\t'+pq('.count.col-xs-4:nth-child(3) strong').text()+'\t'+pq('.userinfo-xs').text()+'\n')
    f1.flush()
# -*- coding: utf-8 -*-
'''
Created on 19-Dec-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
from queue import Queue
store_results = open('output.txt','w',encoding='utf-8')
input_file = open('results.txt').read().split('\n')

#for inp in input_file:
def worker(q):
    while not q.empty():
        try:
            inp = q.get() 
            print (inp)
            output  = ''
            
            url = 'http://www.baltinesterjewelry.com/'+inp
            resp = requests.get(url).text
            pq = PyQuery(resp)
            output+= (url)+'\t'
            output+= (pq('[class="PVcatNumber"]').text().strip())+'\t'
            output+= (pq('#divPVtextWrapper').text().strip())+'\t'
            output+= (pq('[class="productSec desc"]').text().strip())+'\t'
            
            
            if pq('option:contains("Select Ring Inscription")'):
                output+= ('Yes')+'\t'
            else:
                output+= ('No')+'\t'
            
            if pq('option:contains("Comfort Fit (+$275)")'):
                output+= ('Yes')+'\t'
            else:
                output+= ('No')+'\t'
                
            if pq('option:contains("[#GW] My Ring Size is")'):
                output+= ('Yes')+'\t'
            else:
                output+= ('No')+'\t'
                
            if pq('option:contains("[YL] Add a Gold Chain to the pendant?")'):
                output+= ('Yes')+'\t'
            else:
                output+= ('No')+'\t'
                
            if pq('div:contains("Desired Name: (We will spell it for you)")'):
                output+= ('Yes')+'\t'
            else:
                output+= ('No')+'\t'
                
            output+= (pq('[class="attributeName"]:contains("Width")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Thickness")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Diamond Weight")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Diamond Color/Clarity")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Height")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Ruby Weight")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Diamond Cut")').parent()('[class="attributeValue"]').text().strip())+'\t'
            output+= (pq('[class="attributeName"]:contains("Gold Purity")').parent()('[class="attributeValue"]').text().strip())+'\t'
            try:
                output+= (pq('[class="itemRecDetails"]:nth-child(3)')[0].text.strip().replace('\n','').replace('\r', ''))+'\t'
            except:
                output+='\t'
            try:
                output+= (pq('[class="itemRecDetails"]:nth-child(3)')[1].text.strip().replace('\n','').replace('\r', ''))+'\t'
            except:
                output+='\t'
            images = []
            for img in pq('[rel="prettyPhoto[pp_gal]"]'):
                images.append('http://www.baltinesterjewelry.com'+img.attrib['href'])
            
            output+= (', '.join(images))+'\n'
                
            store_results.write(output)
            store_results.flush()
        except Exception as e:
            pass
        finally:
            q.task_done()
    
q = Queue()
for i in input_file:
    q.put(i)

from threading import Thread
for i in range(1):
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
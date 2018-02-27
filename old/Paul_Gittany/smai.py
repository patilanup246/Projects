'''
Created on May 10, 2017

@author: Mukadam
'''
#.site-nav__dropdown li a.site-nav__link
import requests, re, json
from threading import Thread
from Queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


all_collection_links = []

main_page = requests.get('https://www.smai.com.au/sitemap_products_0.xml',verify=False).text

    
matcher = re.findall('<loc>(.*?)</loc>', main_page)

#print matcher[1::]
file_smai_export = open('file_smai_export.txt','w')
#for site in matcher[1::]:
#file_transaction_list = open('file_t.txt','w')
def worker(q):
    while not q.empty():
        try:
            site = q.get()
            print site+'\n'
            resp = requests.get(site,verify=False).text
            category = re.findall('"type":"(.*?)"', resp)[0]
            print category
            #print re.findall('{"product":(.*?),"page":', resp)[0]
            for variant in eval(re.findall('{"product":(.*?),"page":', resp)[0].replace('null,','"null",'))['variants']:
                #print site+'?variant='+str(variant['id'])
                #print PyQuery(resp)('[itemprop="description"]').text()
                #print 'variant_discounts['+str(variant['id'])+'][\'vip\'] = { type: "product", value: "(.*?)"'
                info = ''
                info += variant['sku'] + '\t' + variant['name'] + '\t' +  PyQuery(resp)('[itemprop="description"]').text().replace('\n','') + '\t'+category+'\t' 
                matcher1 = re.findall('variant_discounts\['+str(variant['id'])+'\]\[\'vip\'\] = { type: "product", value: "(.*?)"', resp)
                #print matcher1
                if '|' in matcher1[0]:
                    info += str(float(matcher1[0].split('|')[0].split('::')[1])*1.1)
                else:
                    info += str(float(matcher1[0].split('::')[1])*1.1)
                file_smai_export.write(info.encode('ascii','ignore') +'\n')
            file_smai_export.flush()
        except Exception,e:
            print e
        finally:
            q.task_done()
            
q = Queue()
map(q.put, matcher[1::])
 
startime = time.time()
for i in range(2):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print endtime-startime
    
    


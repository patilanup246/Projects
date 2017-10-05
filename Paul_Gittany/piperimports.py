'''
Created on May 21, 2017

@author: Mukadam
'''
import requests
from pyquery import PyQuery
from threading import Thread
from Queue import Queue
import time

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

resp_main = requests.get("https://www.piperimports.com.au/index.php/online-catalogue/results,1-500").text
pq = PyQuery(resp_main)

urls = []

for item in pq('.vm-product-descr-container-1  a'):
    urls.append('https://www.piperimports.com.au'+item.attrib['href'])
    
print urls

def worker(q):
    while not q.empty():
        try:
            url = q.get()

        except Exception,e:
            print e
        finally:
            q.task_done()

q = Queue()
map(q.put, urls)
 
startime = time.time()
for i in range(50):
    print i
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print endtime-startime
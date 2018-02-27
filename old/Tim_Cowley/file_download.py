'''
Created on May 5, 2017

@author: Mukadam
'''
import urllib
from openpyxl import load_workbook
import time,sys
import requests
from urlparse import urlparse
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests, re, json
from threading import Thread
from Queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
images_file = open('Input_files/before_women.txt','r').read().split('\n')


def worker(q):
    while not q.empty():
        item = q.get()
        print images_file.index(item)
        #print images_file.index(image)
        urllib.urlretrieve(item, 'Images/before_women/'+item.replace('http://images.modelmydiet.com/i/',''))

# for image in images_file:
#     print images_file.index(image)
#     urllib.urlretrieve(image.replace('http://sandbox-compositor.modelmydiet.com/i/','http://images.modelmydiet.com/i/'), 'Images/After_men/'+image.replace('http://sandbox-compositor.modelmydiet.com/i/',''))
#     
#     
q = Queue()
map(q.put, images_file)
 
startime = time.time()
for i in range(50):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print endtime-startime
from threading import Thread
from Queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
urls = []
from datetime import datetime

ids = open('file_product_ids.txt','r').read().split('\n')

for id in ids:
    for page in xrange(1,51):
        urls.append(str(id)+'#'+str(page))

#print urls
#urls = urls[:5000]
file_transaction_list = open('file_t.txt','w')
def worker(q):
    while not q.empty():
        try:
            url = q.get()
            #print url.split('#')[0]
            print str(urls.index(url))
            r = requests.get('https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId=32712489059&type=default&page=16'.format(url.split('#')[0],url.split('#')[1])).json()
            for item in r['records']:
                product_id = str(url.split('#')[0])
                name = str(item['name']).encode('ascii','ignore')
                country = str(item['countryName'])
                timestamp = str(item['date'])
                pieces = str(item['quantity'])
                customer_member_level = str(item['buyerAccountPointLeval'])
                time_scraped = str(datetime.now())
                
                all_data = product_id +'\t' + name + '\t' + country + '\t' + timestamp + '\t' + pieces + '\t' + customer_member_level + '\t' + time_scraped +'\n'
                file_transaction_list.write(all_data)
                file_transaction_list.flush()
            #pq = PyQuery(r.text)
            #print len(pq('.atwl-button '))
            #print r.json()+'\n'
            # do something with data
            #q.task_done()
        except Exception,e:
            print e
        finally:
            q.task_done()
 
# Create a queue and fill it
q = Queue()
map(q.put, urls)
 
startime = time.time()
for i in range(50):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print endtime-startime
file_transaction_list.close()
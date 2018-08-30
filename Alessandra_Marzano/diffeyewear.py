import requests
import re
from pyquery import PyQuery
import json
import threading
from queue import Queue
from pyquery import PyQuery
import requests, time

o = open('output.txt','w')


# url = "https://www.ray-ban.com/usa/store-locator/LoadStores"
# def worker(q):

#     while not q.empty():
#         try:
#             payload = "ctryId=27&form_CP="+str(q)
#             headers = {
#                 'accept': "*/*",
#                 'accept-encoding': "gzip, deflate, br",
#                 'accept-language': "en-US,en;q=0.9",
#                 'cache-control': "no-cache",
#                 'content-length': "136",
#                 'content-type': "application/x-www-form-urlencoded",
#                 'origin': "https://www.ray-ban.com",
#                 'pragma': "no-cache",
#                 'referer': "https://www.ray-ban.com/usa/store-locator",
#                 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
#                 'x-requested-with': "XMLHttpRequest"
#                 }

#             response = requests.request("POST", url, data=payload, headers=headers)
#             r = re.findall('var arrStores=(.*),',response.text)[0]
#             j = json.loads(r)
#             print (str(q)+' : '+str(len(j)))
#             for a in j:
#                 o.write(str(a['Name'])+'\t'+str(a['Address'])+'\t'+str(a['Address2'])+'\t'+str(a['City'])+'\t'+str(a['Zip'])+'\t'+str(a['Telephone'])+'\n')
#         except Exception as e:
#             print (e)
#         finally:
#             q.task_done()

url = "https://www.alainmikli.com/content/themes/alainmikli/inc/ajax-get-locations.php"
def worker(q):

    while not q.empty():
        try:
            t = q.get()
            payload = "cmr=false&location="+str(t)
            headers = {
                'accept': "application/json, text/javascript, */*; q=0.01",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache",
                'connection': "keep-alive",
                'content-length': "24",
                'content-type': "application/x-www-form-urlencoded",
                'host': "www.alainmikli.com",
                'origin': "https://www.alainmikli.com",
                'pragma': "no-cache",
                'referer': "https://www.alainmikli.com/store-locator/",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                'x-requested-with': "XMLHttpRequest"
                }

            response = requests.request("POST", url, data=payload, headers=headers)
            #r = re.findall('var arrStores=(.*),',response.text)[0]
            j = json.loads(response.text)
            print (str(t)+' : '+str(len(j)))
            for a in j:
                try:
                    
                    o.write(str(a['name'])+'\t'+str(a['address_1'])+'\t'+str(a['address_2'])+'\t'+str(a['city'])+'\t'+str(a['state'])+'\t'+str(a['zip'])+'\t'+str(a['country'])+'\t'+str(a['website'])+'\t'+str(a['email'])+'\t'+str(a['phone'])+'\n')
                    o.flush()
                except Exception as e:
                    pass
        except Exception as e:
            print (e)
        finally:
            q.task_done()

q = Queue()
for i in open('input.txt').read().split('\n'):
    q.put(i)
 
startime = time.time()
for i in range(10):
    #print i
    t = threading.Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print (endtime-startime)
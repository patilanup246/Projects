from threading import Thread
from Queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
urls = []
from datetime import datetime
import json
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.39 Safari/537.36"
    }

urls = open('urls2.txt', 'r').read().split('\n')
f_andrew_output = open('f_andrew_output.txt', 'w')
def worker(q):
    while not q.empty():
        try:
            url = q.get()
            
            url_id = url.rsplit('-->')[0]
            site = url.rsplit('-->')[1]
            
            #response = requests.get("https://api.similarweb.com/SimilarWebAddon/"+site.replace('\n','').strip()+"/all",proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
            response = requests.get("https://api.similarweb.com/SimilarWebAddon/"+site.replace('\n','').strip()+"/all", headers=headers)
            website_details =''
            try:
                j = json.loads(response.text)
                
               
                #print len(j.keys())
                website_details = (url_id + '\t' +site+'\t'+
                str(int(j['Engagments']['Visits'])) + '\t' +
                str(j['Engagments']['PagePerVisit']) + '\t' +
                str(j['Engagments']['BounceRate'] * 100) + '\t' +
                str(j['TrafficSources']['Direct'] * 100) + '\t' +
                str(j['TrafficSources']['Referrals'] * 100) + '\t' +
                str(j['TrafficSources']['Search'] * 100) + '\t' +
                str(j['TrafficSources']['Social'] * 100) + '\t' +
                str(j['TrafficSources']['Paid Referrals'] * 100) + '\t' +
                str(j['TrafficSources']['Mail'] * 100) + '\t' +
                str(j['PaidSearchShare'] * 100) + '\t')
                
                
                #f_andrew_output.write()
                website_details+=('"')
                for a in j['TopCategoriesAndFills']:
                    website_details+=(a['Category'] + ', ')
                website_details+=('"\t')
                website_details+=('"')
                for a in j['TopAlsoVisited']:
                    website_details+=(a + ', ')
                website_details+=('"\t')
                website_details+=('"')
                for a in j['TopReferring']:
                    website_details+=(a['Site'] + ' ' + str(a['Value'] * 100) + ',')
                website_details+=('"\t')
        
        
                
                #website_details+=(str(j['EstimatedMonthlyVisits']['2016-12-01']) + '\t')
                website_details+=(str(j['EstimatedMonthlyVisits']['2017-02-01']) + '\t')
                website_details+=(str(j['EstimatedMonthlyVisits']['2017-03-01']) + '\t')
                website_details+=(str(j['EstimatedMonthlyVisits']['2017-04-01']) + '\t')
                website_details+=(str(j['EstimatedMonthlyVisits']['2017-05-01']) + '\t')
                website_details+=(str(j['EstimatedMonthlyVisits']['2017-06-01']) + '\t')
                website_details+=(str(j['EstimatedMonthlyVisits']['2017-07-01']) + '\t')
                website_details+=(str(datetime.now())+'\n')
        
                print 'Count :'+ url_id+'\t'+site +'\t\t : Successful\n'
        
        
        
            except Exception, e:
                print 'Count :'+ url_id+'\t'+site +'\t\t : No info found\n'
                website_details = (url_id+'\t'+site+'\n')
            finally:
                response.close()
            f_andrew_output.write(website_details)
            f_andrew_output.flush()
        except Exception,e:
            print e
        finally:
            q.task_done()

q = Queue()
map(q.put, urls)
 
startime = time.time()
for i in range(2):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print endtime-startime
    
    
    
    

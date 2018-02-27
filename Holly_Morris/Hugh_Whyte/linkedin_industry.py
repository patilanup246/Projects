'''
Created on May 9, 2017

@author: Mukadam
'''
from threading import Thread
from Queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
urls = []
from datetime import datetime
import json
headers = {
    'accept': "application/vnd.linkedin.normalized+json",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "bcookie=\"v=2&a1d7253d-8c43-4111-875c-3c55464f0104\"; visit=\"v=1&M\"; lang=v=2&lang=en-us; li_at=AQEDAQdhrlYE3i_ZAAABW-3R9eIAAAFb-tNfVlEAKjU5grWaNCVDzpWDIwJDGr0ubmS42DP74CpvtZVp1sfrwzYL7ByXsqpGcFr59Aui_R4PDhJI0cfD1xXuhKTIQNDEwKSYiAgN4RW9TDyBUupMFp0U; liap=true; sl=\"v=1&0OUm9\"; JSESSIONID=\"ajax:7915392322747889298\"; _ga=GA1.2.605608648.1494343608; _gat=1; lidc=\"b=SB34:g=8:u=100:i=1494533052:t=1494619408:s=AQEoh1BJgiKa864nzVu7Won1YKdnG2IB\"; bscookie=\"v=1&20170511200735712db34d-5eee-438c-8e2b-24c2683a972aAQHrPDgENpAjjujISiVfvU5WCV4hkr7L\"; _lipt=CwEAAAFb-SDwR0Pu_M4FqpeeSmC4QFKD2T9Yo2YWS-GTMNclPMWSYR9Vyh4oDwiAElTVnrpsH9UvapaArEybF7cJVAvdxwZsBCxsLWlf7NSjDbKisjPO8l7CP1JC0mlH3MtT2-t-xecZKQBpZJ9Jp99uvP8ZO-33sJavRSiaEAyssW7U_1Xoocl6myxw8C9__op16_DuTHgWiRHKpqzOPWuXpdSDhwds_46ffrmLvVlj35IsiFqssbKG7QY7jIJ3SgSfcsGUNks-P2xIAa70SecY0MMQmbga5sl9XK-Vr188blKJ9DbhzmFBvoVET4YXUdGymbRiZmaOtosvUuSdbVk33Q00aW_YIYa2yjUb_SV9UP75C7uhJ-GBBSyebawWnzhZiumwzhx0FJzh9KyumoVOGIHL8y1NEiPym-c7_Zs4-9F4vovwYPLyXLRGpUH7zKM4cw",
    'csrf-token': "ajax:7915392322747889298",
    'referer': "https://www.linkedin.com/",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'x-li-lang': "en_US",
    'x-li-page-instance': "urn:li:page:d_flagship3_search_srp_people;iOwaaEyjTtSSu0FijI9E9A==",
    'x-li-track': "{\"clientVersion\":\"1.0.*\",\"osName\":\"web\",\"timezoneOffset\":5.5,\"deviceFormFactor\":\"DESKTOP\"}",
    'x-requested-with': "XMLHttpRequest",
    'x-restli-protocol-version': "2.0.0",
    'cache-control': "no-cache"
    }
industry = 1

linkedin_profile_urn = open('linkedin_profile_urn.txt','w')

urls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149]

def worker(q):
    while not q.empty():
        try:
            url = str(q.get())
            i=0
            while True:
                resp = requests.get('https://www.linkedin.com/voyager/api/search/cluster?count=10&guides=List(v-%3EPEOPLE,facetGeoRegion-%3Egd%3A0,facetIndustry-%3E{})&origin=FACETED_SEARCH&q=guided&searchId=1494339567305&start={}'.format(str(url),str(i*10)),headers=headers,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')).json()
                print resp
                if not resp['included']:
                    break
                
                for item in resp['included']:
                    try:
                        if 'urn:li:fs_memberBadges:' in item['entityUrn']:
                            linkedin_profile_urn.write(item['entityUrn'].replace('urn:li:fs_memberBadges:','')+'\n')
                    except KeyError,e:
                        pass
                linkedin_profile_urn.flush()
                print str(url)+' --> '+str(i)
                i+=1

        except Exception,e:
            print e
        finally:
            q.task_done()



# for industry in range (1,149):
#             i=0
#             while True:
#                 resp = requests.get('https://www.linkedin.com/voyager/api/search/cluster?count=10&guides=List(v-%3EPEOPLE,facetGeoRegion-%3Egd%3A0,facetIndustry-%3E{})&origin=FACETED_SEARCH&q=guided&searchId=1494339567305&start={}'.format(str(industry),str(i*10)),headers=headers).json()
#                 if not resp['included']:
#                     break
#                 
#                 for item in resp['included']:
#                     try:
#                         if 'urn:li:fs_memberBadges:' in item['entityUrn']:
#                             linkedin_profile_urn.write(item['entityUrn'].replace('urn:li:fs_memberBadges:','')+'\n')
#                     except KeyError,e:
#                         pass
#                 linkedin_profile_urn.flush()
#                 print str(industry)+' --> '+str(i)
#                 i+=1
        
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
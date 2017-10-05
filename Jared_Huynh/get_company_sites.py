import requests,re
import urllib
import requests, re, json
from threading import Thread
from Queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

headers = {
    'accept': "application/vnd.linkedin.normalized+json",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': 'bcookie="v=2&c08f52ef-f4e2-4fce-89e5-9c43955f8071"; bscookie="v=1&20170521043018b70a9bbe-8b2e-4691-826c-0d2768393ec9AQH6y-5f0Y9YsV8Tg5WaIGMkiiCwC34O"; visit="v=1&G"; _gat=1; sl="v=1&hQSx6"; lang="v=2&lang=en-us"; liap=true; li_at=AQEDASLSVMEBBYFBAAABXCtIxFsAAAFcLQA4W1EAtfooShnXkUEKWN0RQ13i4T5WyTsLq_Z0ISfSBumC7kscSxSKd7THUB3zfrFGWpzt5t8QI8J8jj9IANR6vkDRD1DtDp9pEmbAhAshaopCfxoJFIM-; JSESSIONID="ajax:4247241944476466052"; RT=s=1495374807189&r=https%3A%2F%2Fwww.linkedin.com%2F; _ga=GA1.2.690901640.1495374784; _lipt=CwEAAAFcK0jpw6vOK_xiv_El2tA7s9tO1RT00ovevBPMZ_3NmFfdcGbo9FzTbnlOuSHaDvVmzSuuDyYbKLSE6wsMe-RUrvtkUOEwAqGia-cBHFy3K-RyBfjurDc; lidc="b=TB01:g=983:u=2:i=1495374834:t=1495461208:s=AQGEB-KoEPTl3aYfCJdHC9hkLrC4N42L"',
    'csrf-token': "ajax:4247241944476466052",
    'referer': "https://www.linkedin.com/",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'x-li-lang': "en_US",
    'x-li-page-instance': "urn:li:page:d_flagship3_search_srp_people;+WK//s8zTkKKEM/gYGUkQA==",
    'x-li-track': "{\"clientVersion\":\"1.0.*\",\"osName\":\"web\",\"timezoneOffset\":5.5,\"deviceFormFactor\":\"DESKTOP\"}",
    'x-requested-with': "XMLHttpRequest",
    'x-restli-protocol-version': "2.0.0",
    'cache-control': "no-cache"
    }
file_company_output = open('file_company_output.txt','w')
file_company_input = open('file_company_input.txt','r').read().split('\n')

    
def worker(q):
    while not q.empty():

        try:
            details = q.get().encode('ascii','ignore')
            company = details.split('\t')[0].encode('ascii','ignore')
            index_no = str(details.split('\t')[1])
            print index_no
            response = requests.request("GET", "https://www.linkedin.com/voyager/api/typeahead/hits?types=List(COMPANY)&q=federated&query="+urllib.quote(company, safe=''), headers=headers)
            companyid = ''
            #print file_company_input.index(company)
            try:
                response.json()['included']
            except Exception,e:
                a1= company+'\t'+companyid+'\t'+''+'\t'+''+'\t'+index_no+'\n'
                print a1
                file_company_output.write(a1)
                file_company_output.flush()
                
                continue    
            
            for data in response.json()['included']:
                try:
                    if data['name'].lower() == company.lower():
                        companyid = data['objectUrn'].encode('ascii','ignore').replace('urn:li:company:','')
                        
                        
                        
                        response1 = requests.request("GET", "https://www.linkedin.com/company-beta/"+str(companyid), headers=headers,verify=False)
                        companysite = ''
                        company_loc = ''
                        company_size =''
            #print file_company_input.index(company)
                        try:
                            companysite = re.findall('companyPageUrl&quot;:&quot;(.*?)&quot;', response1.text.encode('ascii','ignore'))[0].encode('ascii','ignore')
                            company_loc = re.findall('city&quot;:&quot;(.*?)&quot;', response1.text.encode('ascii','ignore'))[0].encode('ascii','ignore')
                            company_size = re.findall('start&quot;:(.*?),&quot;', response1.text)[0]+'-'+re.findall('end&quot;:(.*?),&quot;', response1.text.encode('ascii','ignore'))[0].encode('ascii','ignore')
                        except Exception,e:
                            pass
        
                        
                        
                        
                        break
                except Exception,e:
                    pass
            a2 = company+'\t'+companysite+'\t'+'\t'+company_loc+'\t'+company_size+'\t'+index_no+'\n'
            print a2
            file_company_output.write(a2)
            file_company_output.flush()
        except Exception,e:
            print e
        finally:
            q.task_done()
                        
            
            
            
q = Queue()
map(q.put, file_company_input)
 
startime = time.time()
for i in range(1):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print endtime-startime
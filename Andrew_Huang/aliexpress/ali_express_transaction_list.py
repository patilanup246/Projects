import requests.packages.urllib3
from datetime import datetime
requests.packages.urllib3.disable_warnings()
from requests_futures.sessions import FuturesSession
requests.packages.urllib3.disable_warnings()
session = FuturesSession()
import json


file_product_ids = open('file_product_ids.txt','r').read().split('\n')
file_transaction_list = open('file_transaction_list.txt','w')


def bg_cb(sess, response1):
    try:
        product_id = str(response1.url.rsplit('#')[1])
        response = json.loads(response1.text.encode('ascii','ignore'))
        
        for item in response['records']:
            #product_id = str(product)
            name = str(item['name']).encode('ascii','ignore')
            country = str(item['countryName'])
            timestamp = str(item['date'])
            pieces = str(item['quantity'])
            customer_member_level = str(item['buyerAccountPointLeval'])
            time_scraped = str(datetime.now())
            
            file_transaction_list.write(product_id + '\t' + name + '\t' + country + '\t' + timestamp + '\t' + pieces + '\t' + customer_member_level + '\t' + time_scraped +'\n')
                
        
    except Exception,e:
        print e
    finally:
        response1.close()
        
    file_transaction_list.flush()


for product in file_product_ids:
    print file_product_ids.index(product)
    for i in range(1,51):        
        future = session.get('https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId={}&type=default&page={}#{}'.format(str(product),str(i),str(product)),background_callback=bg_cb)
    future.result()
    
        
        
        
        
        
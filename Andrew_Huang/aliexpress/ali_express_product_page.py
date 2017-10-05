'''
Created on Apr 29, 2017

@author: Mukadam
'''
from threading import Thread
from Queue import Queue
import time,re,json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery
urls = []
from datetime import datetime



file_product_list = open('file_product_list.txt','w')
file_store_list = open('file_store_list.txt','w')
url1 = "https://www.aliexpress.com/wholesale"

file_product_ids = open('file_product_ids.txt','r').read().split('\n')
#urls=[]

for product in file_product_ids:
    urls.append(str(product))



def worker(q):
    while not q.empty():
        try:
            product = q.get()
            #print url.split('#')[0]
            print str(urls.index(product))

            querystring = {"SearchText":str(product)}
            try:
                response = requests.request("GET", url1,params=querystring)
                response_shipping = requests.request("GET", "https://freight.aliexpress.com/ajaxFreightCalculateService.htm?f=d&productid={}&count=1&currencyCode=USD&sendGoodsCountry=&country=IN&province=&city=&abVersion=1".format(str(product))).text[1:-1]
                response_last_6_months = requests.request('GET', 'https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId={}&type=default&page=1'.format(product)).json()
            
            except Exception, e:
                print 'skipped'
                continue
            #print(response.text)
            
            product_id = ''
            store_id = ''
            product_title = ''
            product_image_urls = []
            price = ''
            currency = ''
            unit = ''
            discount_price = ''
            discount_currency = ''
            discount_unit = ''
            rating = ''
            votes = ''
            rating_5 = ''
            rating_4 = ''
            rating_3 = ''
            rating_2 = ''
            rating_1 = ''
            category = []
            shipping = ''
            estimated_delivery_time = ''
            pieces_available = ''
            orders = ''
            transaction_last_6_months = ''
            shipping_options = []
            product_handle = ''
            time_scraped = ''
    
            pq = PyQuery(response.text)
            
            
            product_id =                str(product).strip()
            store_id =                  pq('.store-number').text().strip()
            product_title =             pq('.product-name').text()
            product_image_urls = []
            for image in pq('.img-thumb-item img'):
                product_image_urls.append(image.attrib['src'].replace('jpg_50x50.jpg','jpg_640x640.jpg'))
            price =                     pq('#j-sku-price').text()
            currency =                  pq('.p-del-price-detail .p-symbol').text()
            unit =                      pq('.p-del-price-detail .p-unit').text()
            discount_price =            pq('#j-sku-discount-price').text()
            discount_currency =         pq('.p-current-price [itemprop="priceCurrency"]').text()
            discount_unit =             pq('.p-current-price .p-unit').text()
            rating =                    pq('.product-customer-reviews [itemprop="ratingValue"]').text()
            votes =                     pq('.product-customer-reviews [itemprop="reviewCount"]').text()
            rating_5 =                  pq('.detail .rate-list [data="5 Stars"]').text()
            rating_4 =                  pq('.detail .rate-list [data="4 Stars"]').text()
            rating_3 =                  pq('.detail .rate-list [data="3 Stars"]').text()
            rating_2 =                  pq('.detail .rate-list [data="2 Stars"]').text()
            rating_1 =                  pq('.detail .rate-list [data="1 Stars"]').text()
            category = []
            for cat in pq('.ui-breadcrumb a'):
                category.append(re.sub("\D", "", cat.attrib['href']))
            
            
            response_shipping = json.loads(response_shipping)
            if response_shipping['freight']:
                if response_shipping['freight'][0]['status']:
                    shipping = "Free Shipping to United States via Seller's Shipping Method"
                else:
                    shipping = "{} to United States via {}".format(response_shipping['freight'][0]['totalFreightFormatStr'],response_shipping['freight'][0]['companyDisplayName'])
                
                #response_shipping.close()
                estimated_delivery_time = response_shipping['freight'][0]['time']
            pieces_available = str(re.search('window.runParams.totalAvailQuantity=(.*?);',response.text).group(1))
            orders = pq('#j-order-num').text()
            transaction_last_6_months = response_last_6_months['range']['transactions']
            shipping_options = []
            for info in response_shipping['freight']:
                info_obj = {}
                info_obj['Shipping Company'] = info['companyDisplayName']
                info_obj['Estimated Delivery Time'] = info['time']
                info_obj['Shipping Cost'] = info['totalFreightFormatStr']
                if info['isTracked']:
                    info_obj['Tracking Information'] = 'Available'
                else:
                    info_obj['Tracking Information'] = 'Not Available'
                shipping_options.append(info_obj)
            shipping_options = json.dumps(shipping_options)
            product_handle = response.url.replace('https://www.aliexpress.com/item/','').replace('/{}.html'.format(str(product)),'')
            time_scraped = str(datetime.now())
            
            
            output_data = str(product_id)+'\t'+str(store_id)+'\t'+str(product_title)+'\t'+str(product_image_urls)+'\t'+str(price)+'\t'+str(currency)+'\t'+str(unit)+'\t'+str(discount_price)+'\t'+str(discount_currency)+'\t'+str(discount_unit)+'\t'+str(rating)+'\t'+str(votes)+'\t'+str(rating_5)+'\t'+str(rating_4)+'\t'+str(rating_3)+'\t'+str(rating_2)+'\t'+str(rating_1)+'\t'+str(category)+'\t'+str(shipping)+'\t'+str(estimated_delivery_time)+'\t'+str(pieces_available)+'\t'+str(orders)+'\t'+str(transaction_last_6_months)+'\t'+str(shipping_options)+'\t'+str(product_handle)+'\t'+str(time_scraped)+'\n'
            file_product_list.write(output_data) 
            file_product_list.flush()
            
            
            response_store_feedback = requests.get('https://m.aliexpress.com/store/sellerInfo.htm?sellerAdminSeq={}'.format(str(pq('.s-mail .send-mail-btn').attr('data-id1'))))
            pq_store = PyQuery(response_store_feedback.text)
            
            
            store_name = pq('.shop-name a').text()
            try:
                positive_feedback = str(re.search('sellerScore":(.*?),', response_store_feedback.text).group(1))
                feeback_score = str(re.search('feedbackRating":"(.*?)"', response_store_feedback.text).group(1))
                
                date_opened = str(re.search('"since":"(.*?)"', response_store_feedback.text).group(1))
                item_as_described = str(re.search('"proDescEval":"(.*?)"', response_store_feedback.text).group(1))
                
                communication =     str(re.search('"sellerServiceEval":"(.*?)"', response_store_feedback.text).group(1))
                shipping_speed =    str(re.search('"shippingServiceEval":"(.*?)"', response_store_feedback.text).group(1))
            except Exception,e:
                continue
            time_scraped = str(datetime.now())
            store_details = store_id + '\t' + store_name + '\t' +  positive_feedback + '\t' +  feeback_score + '\t' +  date_opened + '\t' +   item_as_described + '\t' +  communication + '\t' +  shipping_speed + '\t' +  time_scraped + '\n'
            file_store_list.write(store_details)
            
            response_store_feedback.close()
            response.close()
            file_store_list.flush()
        except Exception,e :
            print ' Skipping '
        finally:
            q.task_done()
            
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
    
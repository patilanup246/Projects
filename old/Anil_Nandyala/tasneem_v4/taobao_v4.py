'''
Created on May 19, 2017

@author: Mukadam

Notes:
For Chinese locations: Use https://www.urlencoder.org/ to encode Chinese text, replace %252C with %2C, and then paste it in location.txt 
Example: Guangdong = %E5%B9%BF%E5%B7%9E%2C%E6%B7%B1%E5%9C%B3%2C%E4%B8%AD%E5%B1%B1%2C%E7%8F%A0%E6%B5%B7%2C%E4%BD%9B%E5%B1%B1%2C%E4%B8%9C%E8%8E%9E%2C%E6%83%A0%E5%B7%9E

'''
import requests
import re, json, urllib
#from selenium import webdriver
import webbrowser
from pyquery import PyQuery
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tkinter





total_pages = 1

url = "https://s.taobao.com/search"

headers = {
    'cache-control': "no-cache"
    }
file_output_taobao = open('taobao_log.txt','w')
file_output_taobaoUnsorted = open('taobao_logUnsorted.txt','w')
file_output_tmall = open('tmall_log.txt','w')
file_output_tmallUnsorted = open('tmall_logUnsorted.txt','w')
file_output_taobao_price_rating = open('file_output_taobao_price_rating.txt','w')
file_output_tmall_price_rating = open('file_output_tmall_price_rating.txt','w')
taobao_items = []
tmall_items = []




headers_tmall_price = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'referer': "https://world.tmall.com/",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'cache-control': "no-cache"
    }

for page in range(0,total_pages):
    #querystring = {"data-key":"s","ajax":"true","q":open('keywords.txt','r').read(),"imgfile":"","commend":"all","sort":"sale-desc","search_type":"item","data-value":str(page*44)
    #response = requests.request("GET", url, headers=headers, params=querystring)
    print ('https://s.taobao.com/search?sort=sale-desc&data-key=s&ajax=true&q={}&loc={}&data-value={}'.format(open('keywords.txt','r').read(),open('location.txt','r').read(),str(page*44)))
    response = requests.get('https://s.taobao.com/search?sort=sale-desc&data-key=s&ajax=true&q={}&loc={}&data-value={}'.format(open('keywords.txt','r').read(),open('location.txt','r').read(),str(page*44)))
    
    #file_output.write(response.text.encode('ascii','ignore'))

    for item in response.json()['mods']['itemlist']['data']['auctions']:
        item_page_link = item['detail_url']
        mod_item_page_link = item_page_link.replace('//world.','')
        #item_id = re.findall(r'\d+', item_page_link)[0]
        item_id = str(item['nid'])
        print ('Scraping Page - '+str(page+1) +', item - '+str(response.json()['mods']['itemlist']['data']['auctions'].index(item)+1))
        try:
            taobao_obj = {}
            tmall_obj ={}
            if 'tmall' in item_page_link:
                neg_count_store = []
                print ('stage - 1')
                print ('https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(item_id))
                resp_tmall = requests.get('https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(item_id)).text.replace('jsonp128','')[3:-2]
                print (resp_tmall)
                print ('stage - 2')
                j_tmall = json.loads(resp_tmall)
                print ('stage - 3')
                tmall_obj['link'] = mod_item_page_link

                #Added by Anil-START
                tmall_obj['gradeAvgRating'] = j_tmall['dsr']['gradeAvg']
                tmall_obj['rateTotalRating'] = j_tmall['dsr']['rateTotal']
                #Added by Anil-END
                tmall_obj['rating'] = int(j_tmall['dsr']['gradeAvg']*j_tmall['dsr']['rateTotal'])
                
                '''
                    Added - Negative count
                    @author: Tasneem
                '''
                print ('stage - 4')
                print ('https://rate.tmall.com/listTagClouds.htm?isAll=true&callback=jsonp937&isInner=true&itemId='+str(item_id))
                resp_tmall_neg_count = requests.get('https://rate.tmall.com/listTagClouds.htm?isAll=true&callback=jsonp937&isInner=true&itemId='+str(item_id)).text.replace('jsonp937(','')[1:-1]
                print (resp_tmall_neg_count)
                j_neg_count = json.loads(resp_tmall_neg_count)
                print ('stage - 5')
                for tag_cloud in j_neg_count['tags']['tagClouds']:
                    if not tag_cloud['posi']:
                        #print tag_cloud['count']
                        neg_count_store.append(str(tag_cloud['count']))
                tmall_obj['neg_rating'] = '\t'.join(neg_count_store)
                #print tmall_obj['neg_rating']
                tmall_items.append(tmall_obj)
                
                
                
                '''
                added price and rating for tmall 29/05/17
                Author - Tasneem
                '''
                print ('https://world.tmall.com/item/{}.htm'.format(str(item_id)))
                resp_rating_tmall = requests.get('https://world.tmall.com/item/{}.htm'.format(str(item_id))).text
                
                pq_tmall = PyQuery(resp_rating_tmall)
                file_output_tmall_price_rating.write(str(item_id)+'\t')
                for rating in pq_tmall('a span.down'):
                    file_output_tmall_price_rating.write(str(rating.text)+'\t')
                    
                url = "https://mdskip.taobao.com/core/initItemDetail.htm"

                querystring = {
                        "itemId":str(item_id)
                        }
                print (url)
                response_tmall_price = requests.request("GET", url, headers=headers_tmall_price, params=querystring).json()
                
                tmall_price_keys = response_tmall_price['defaultModel']['itemPriceResultDO']['priceInfo'].keys()

                for key in tmall_price_keys:
                    file_output_tmall_price_rating.write(str(response_tmall_price['defaultModel']['itemPriceResultDO']['priceInfo'][key]['promotionList'][0]['price'])+'\t')
                file_output_tmall_price_rating.write('\n')
                file_output_tmall_price_rating.flush()
                
                
                
            
            if 'taobao' in item_page_link:
                print ('https://rate.taobao.com/detailCommon.htm?auctionNumId='+str(item_id))
                resp_taobao = requests.get('https://rate.taobao.com/detailCommon.htm?auctionNumId='+str(item_id)).text[3:-1]
                
                j_taobao = json.loads(resp_taobao)
                
                taobao_obj['link'] = mod_item_page_link

                #Added by Anil-START
                taobao_obj['goodRating'] = j_taobao['data']['count']['good']
                taobao_obj['normalRating'] = j_taobao['data']['count']['normal']
                taobao_obj['badRating'] = j_taobao['data']['count']['bad']
                #Added by Anil-END
                                                     
                taobao_obj['rating'] = int(j_taobao['data']['count']['good'] - j_taobao['data']['count']['normal'] - j_taobao['data']['count']['bad'])
                taobao_items.append(taobao_obj)
                
                
                # Added by Tasneem 23/05/17
                # This code will get price, seller rating and number of stars
                print ('https://item.taobao.com/item.htm?id='+str(item_id))
                resp_taobao_page = requests.get('https://item.taobao.com/item.htm?id='+str(item_id)).text
                
                pq_tao = PyQuery(resp_taobao_page)
                
                taobao_price_rating = str(item_id)+'\t'+pq_tao('.tb-rmb-num').text().replace('\n','').replace('\r','').strip()+'\t'
                #print pq_tao('.tb-rmb-num').text()
                ratings =[]
                for rating in pq_tao('.tb-rate-higher a'):
                    ratings.append(rating.text.replace('\n','').replace('\r','').strip())
                taobao_price_rating += '\t'.join(ratings) +'\t'
                taobao_price_rating +=  str(len(pq_tao('.tb-shop-rank i'))) + '\t'
                if pq_tao('.tb-shop-rank'):
                    taobao_price_rating += pq_tao('.tb-shop-rank').attr('class').replace('tb-shop-rank','').replace('tb-rank-','')
                file_output_taobao_price_rating.write(taobao_price_rating+'\n')
                file_output_taobao_price_rating.flush()
        except Exception as e:
            print (e)
            
for item in sorted(taobao_items, key=lambda k: int(k['rating']), reverse = True):
    file_output_taobao.write(item['link']+'\t'+ str(item['rating'])+'\n')
for item in sorted(tmall_items, key=lambda k: int(k['rating']), reverse = True):
    file_output_tmall.write(item['link']+'\t'+ str(item['rating'])+'\n')
file_output_taobao.close()
file_output_tmall.close()

#Added by Anil-START
for item in taobao_items:
    file_output_taobaoUnsorted.write(item['link']+'\t'+ str(item['goodRating'])+'\t'+ str(item['normalRating'])+'\t'+ str(item['badRating'])+'\n')
for item in tmall_items:
    file_output_tmallUnsorted.write(item['link']+'\t'+ str(item['gradeAvgRating'])+'\t'+ str(item['rateTotalRating'])+'\t'+item['neg_rating']+'\n')
file_output_taobaoUnsorted.close()
file_output_tmallUnsorted.close()
#Added by Anil-END
 
'''
    open chrome and first 10 pages of taobao:
  
'''

tabs= 0
for url in open('taobao_log.txt','r').read().split('\n'):
    if tabs > 10:
        break
    #driver = webdriver.Chrome()
    print ('http://'+url.split('\t')[0].replace('//item','item'))
    webbrowser.open('http://'+url.split('\t')[0].replace('//item','item'))
    tabs+=1

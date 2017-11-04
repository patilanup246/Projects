'''
Created on May 19, 2017

@author: Mukadam

Notes:
For Chinese locations: Use https://www.urlencoder.org/ to encode Chinese text, replace %252C with %2C, and then paste it in location.txt 
Example: Guangdong = %E5%B9%BF%E5%B7%9E%2C%E6%B7%B1%E5%9C%B3%2C%E4%B8%AD%E5%B1%B1%2C%E7%8F%A0%E6%B5%B7%2C%E4%BD%9B%E5%B1%B1%2C%E4%B8%9C%E8%8E%9E%2C%E6%83%A0%E5%B7%9E

'''
import requests
import re, json, urllib

total_pages = 7

url = "https://s.taobao.com/search"

headers = {
    'cache-control': "no-cache"
    }
file_output_taobao = open('taobao_log.txt','w')
file_output_taobaoUnsorted = open('taobao_logUnsorted.txt','w')
file_output_tmall = open('tmall_log.txt','w')
file_output_tmallUnsorted = open('tmall_logUnsorted.txt','w')

taobao_items = []
tmall_items = []


for page in xrange(total_pages):
    #querystring = {"data-key":"s","ajax":"true","q":open('keywords.txt','r').read(),"imgfile":"","commend":"all","sort":"sale-desc","search_type":"item","data-value":str(page*44)
    #response = requests.request("GET", url, headers=headers, params=querystring)
    response = requests.get('https://s.taobao.com/search?sort=sale-desc&data-key=s&ajax=true&q={}&loc={}&data-value={}'.format(open('keywords.txt','r').read(),open('location.txt','r').read(),str(page*44)))
    #file_output.write(response.text.encode('ascii','ignore'))

    for item in response.json()['mods']['itemlist']['data']['auctions']:
        item_page_link = item['detail_url']
        mod_item_page_link = item_page_link.replace('//world.','')
        #item_id = re.findall(r'\d+', item_page_link)[0]
        item_id = str(item['nid'])
        print 'Scraping Page - '+str(page+1) +', item - '+str(response.json()['mods']['itemlist']['data']['auctions'].index(item)+1)
        try:
            taobao_obj = {}
            tmall_obj ={}
            if 'tmall' in item_page_link:
                neg_count_store = []
                resp_tmall = requests.get('https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(item_id)).text.replace('jsonp128','')[1:-2]
                #print resp_tmall
                j_tmall = json.loads(resp_tmall)

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
                resp_tmall_neg_count = requests.get('https://rate.tmall.com/listTagClouds.htm?isAll=true&callback=jsonp937&isInner=true&itemId='+str(item_id)).text.replace('jsonp937(','')[1:-1]
                #print resp_tmall_neg_count.encode('ascii','ignore')
                j_neg_count = json.loads(resp_tmall_neg_count)
                
                for tag_cloud in j_neg_count['tags']['tagClouds']:
                    if not tag_cloud['posi']:
                        #print tag_cloud['count']
                        neg_count_store.append(str(tag_cloud['count']))
                tmall_obj['neg_rating'] = '\t'.join(neg_count_store)
                #print tmall_obj['neg_rating']
                

                tmall_items.append(tmall_obj)
            
            if 'taobao' in item_page_link:
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
        except Exception,e:
            print e
            
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
 


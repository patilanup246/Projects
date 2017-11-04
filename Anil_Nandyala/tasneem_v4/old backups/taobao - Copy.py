'''
Created on May 19, 2017

@author: Mukadam
'''
import requests
import re, json

total_pages = 3

url = "https://s.taobao.com/search"

headers = {
    'cache-control': "no-cache"
    }
file_output = open('log.txt','a')

for page in xrange(total_pages):
    #querystring = {"from":"tbsearch","_input_charset":"utf-8","navigator":"all","json":"on","q":open('keywords.txt','r').read(),"data-key":"s","data-value":str(page*60),"data-action":"","module":"page","nid":"","type":"","uniqpid":""}
    querystring = {"data-key":"s","ajax":"true","q":open('keywords.txt','r').read(),"imgfile":"","commend":"all","sort":"sale-desc","search_type":"item","data-value":str(page*44)}
    response = requests.request("GET", url, headers=headers, params=querystring)
    #file_output.write(response.text.encode('ascii','ignore'))
    for item in response.json()['mods']['itemlist']['data']['auctions']:
        item_page_link = item['detail_url']
        mod_item_page_link = item_page_link.replace('//world.','')
        #item_id = re.findall(r'\d+', item_page_link)[0]
        item_id = str(item['nid'])
        print 'Scraping Page - '+str(page+1) +', item - '+str(response.json()['mods']['itemlist']['data']['auctions'].index(item)+1)
        try:
            if 'tmall' in item_page_link:
                resp_tmall = requests.get('https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(item_id)).text.replace('jsonp128','')[1:-2]
                #print resp_tmall
                j_tmall = json.loads(resp_tmall)
                
                #print resp_tmall
                file_output.write(mod_item_page_link+'\t'+ str(j_tmall['dsr']['gradeAvg']*j_tmall['dsr']['rateTotal'])+'\n')
            
            if 'taobao' in item_page_link:
                resp_taobao = requests.get('https://rate.taobao.com/detailCommon.htm?auctionNumId='+str(item_id)).text[3:-1]
                j_taobao = json.loads(resp_taobao)
                #print resp_taobao
                file_output.write(mod_item_page_link+'\t'+ str(j_taobao['data']['count']['good'] - j_taobao['data']['count']['normal'] - j_taobao['data']['count']['bad'])+'\n')
            file_output.flush()
        except Exception,e:
            print e



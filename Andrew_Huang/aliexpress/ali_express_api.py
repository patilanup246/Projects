'''
Created on Apr 28, 2017

@author: Mukadam
'''

import requests
file_categories_list = open('ali_express_categories.txt','r').read().split('\n')
url = "https://m.aliexpress.com/search/mainsearch/asy/GetMainSearchDataJson.do"
file_product_ids = open('file_product_ids.txt','w')
for category in file_categories_list:
    for i in range(0,501):
        #querystring = {"keyword":"","start":str(i*20),"freeShipping":"false","ignoreSPU":"true","onePiece":"","pinProductIds":"","pop":"false","scene":"","secondSort":"","categoryId":"200000707","shipFromCity":"","shipFromCountry":"","shipFromProvince":"","shipToCity":"","shipToCountry":"","shipToProvince":"","attributes":"","maxPrice":"","minPrice":"","spuId":"","shoppingCoupon":"","firstSort":"","pageSize":"20","isBigSale":"false"}
        querystring = {"keyword":"","start":str(i*20),"freeShipping":"false","ignoreSPU":"true","onePiece":"false","pinProductIds":"","pop":"false","scene":"","secondSort":"","shipFromCity":"","shipFromCountry":"","shipFromProvince":"","shipToCity":"","shipToCountry":"","shipToProvince":"","categoryId":str(category),"attributes":"","maxPrice":"","minPrice":"","spuId":"","shoppingCoupon":"","firstSort":"TC_D","pageSize":"20","isBigSale":"false"}
        print 'Count : Current Category - '+ str(category)+'\t --> \tCurrent Page - '+str(i)
        response = requests.request("GET", url, params=querystring)
        tradecount = 1
        
        for item in response.json()['items']:
            try:               
                file_product_ids.write(str(item['productId'])+'\n')
                tradecount = item['trade']['tradeCount']
            except Exception, e:
                pass
        file_product_ids.flush()  
        if tradecount == 0:
            break
        response.close()
        
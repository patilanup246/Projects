'''
Created on 05-Jan-2018

@author: Administrator
'''
import requests
import csv
output_f = open('sephora_output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Product name','Product URL','User Name','Title','Review Text','Rating','Date','Avatar'])
products_url = 'https://www.sephora.com/rest/products/?keyword=volition%20beauty&mode=all&pageSize=-1&include_categories=true&include_refinements=true'

r = requests.get(products_url).json()

for p in r['products']:
    product_name    = p['display_name']
    product_url     = 'https://www.sephora.com'+p['product_url']
    print (product_name)
    offset = 0
    while True:
        #print (offset)
        r_rev = requests.get('https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId%3A{}&Sort=Helpfulness%3Adesc&Limit=100&Offset={}&Include=Products%2CComments&Stats=Reviews&passkey=rwbw526r2e7spptqd2qzbkp7&apiversion=5.4'.format(str(p['id']),str(offset))).json()
        
        for rev in r_rev['Results']:
            details = []
            details.append(product_name)
            details.append(product_url)
            details.append(rev['UserNickname'])
            details.append(rev['Title'])
            details.append(rev['ReviewText'])
            details.append(rev['Rating'])
            details.append(rev['SubmissionTime'])
            avatar = ''
            try:
                avatar = rev['AdditionalFields']['sociallockup']['Value'].split('?')[0].replace('avatar=','')
            except Exception as e:
                pass
            details.append(avatar)
            wr.writerow(details)
            #print (rev['UserNickname'])
        
        
        if (offset+100 > r_rev['TotalResults']):
            break
        
        offset += 100
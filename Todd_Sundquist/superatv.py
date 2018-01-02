'''
Created on 31-Dec-2017

@author: Administrator
'''
import requests
import re
from pyquery import PyQuery
import json
import xmltodict, json
import csv
#output_file = open('superatv.txt','w',encoding='utf-8')
output_f = open('superatv_export.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
for jj in open('superatv.txt').read().split('\n'):
#for jj in ['https://www.superatv.com/can-am-commander-800-1000-long-travel-axles-3-4-5-rhino']:
    try:
        
            site = jj
            
            r = requests.get(site).text
            pq = PyQuery(r)
            if not pq('[class="product-options-wrapper"]'):
                print ('Simple '+site)
                sku             = ''
                try:
                    sku         = pq('[class="product attribute sku"]').text()
                except:
                    pass
                name            = ''
                try:
                    name = pq('[itemprop="name"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                category        = 'UTV Accessories'
                fitment         = ''
                try:
                    fitment         = pq('[class="stacked fitment"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                fitment_html    = ''
                try:
                    fitment_html    = pq('[class="stacked fitment"]').html().replace('\n','').replace('\r','').strip()
                except:
                    pass
                url             = site
                price           = ''
                try:
                    price = pq('[class="price"]').text()
                except:
                    pass
                features        = ''
                try:
                    features        = pq('[class="stacked features"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                features_html   = ''
                try:
                    features_html   = pq('[class="stacked features"]').html().replace('\n','').replace('\r','').strip()
                except:
                    pass
                details         = ''
                try:
                    details         = pq('[class="stacked details"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                
                details_html    = ''
                try:
                    details_html    = pq('[class="stacked details"]').html().replace('\n','').replace('\r','').strip()
                except:
                    pass
                images = []
                for p in pq('[type="text/x-magento-init"]'):
                    try:
                        j = json.loads(p.text)
                        for i in (j['[data-gallery-role=gallery-placeholder]']['mage/gallery/gallery']['data']):
                            images.append(i['full'])
                        break
                    except:
                        pass
                images          = ', '.join(images)
                options         = ''
                out = []
                out.append(sku           )
                out.append(name          )
                out.append(category      )
                out.append(fitment       )
                out.append(fitment_html  )
                out.append(url           )
                out.append(price         )
                out.append(features      )
                out.append(features_html )
                out.append(details       )
                out.append(details_html  )
                out.append(images        )
                out.append(options       )
                wr.writerow(out)
                #print (out)
            else:
                sku             = ''
                name            = ''
                print ('Variants '+site)
                try:
                    name = pq('[itemprop="name"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                category        = 'UTV Accessories'
                fitment         = ''
                try:
                    fitment         = pq('[class="stacked fitment"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                fitment_html    = ''
                try:
                    fitment_html    = pq('[class="stacked fitment"]').html().replace('\n','').replace('\r','').strip()
                except:
                    pass
                url             = site
                price           = ''
                features        = ''
                try:
                    features        = pq('[class="stacked features"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                features_html   = ''
                try:
                    features_html   = pq('[class="stacked features"]').html().replace('\n','').replace('\r','').strip()
                except:
                    pass
                details         = ''
                try:
                    details         = pq('[class="stacked details"]').text().replace('\n','').replace('\r','').strip()
                except:
                    pass
                
                details_html    = ''
                try:
                    details_html    = pq('[class="stacked details"]').html().replace('\n','').replace('\r','').strip()
                except:
                    pass
                images          = ''
                options         = ''
                for p in pq('[type="text/x-magento-init"]'):
                    try:
                         
                        j = json.loads(p.text)
                        j = (j['#product_addtocart_form']['js/configurable-update']['spConfig'])
                        
                        skus = json.loads(re.findall(r'window.configurableSimpleSku = (.*?);',r)[0])
                 
                         
                         
                        for sku in skus.keys():
                            temp = j['index'][sku]
                            options = []
                            for a in temp.keys():
                                 
                                for c in j['attributes'][a]['options']:
                                    if c['id'] == temp[a]:
                                        #print (str(skus[sku])+' : '+str(j['attributes'][a]['label'])+' : '+str(c['label']))
                                        options.append(str(j['attributes'][a]['label'])+' : '+str(c['label']))
                                        break
                            images = []
                            for i in j['images'][sku]:
                                images.append(i['full'])
                             
                            price = j['optionPrices'][sku]['finalPrice']['amount']
                            sku = str(skus[sku])
                            options = '\n'.join(options)
                            images = ', '.join(images)
                         
                            out = []
                            out.append(sku           )
                            out.append(name          )
                            out.append(category      )
                            out.append(fitment       )
                            out.append(fitment_html  )
                            out.append(url           )
                            out.append(price         )
                            out.append(features      )
                            out.append(features_html )
                            out.append(details       )
                            out.append(details_html  )
                            out.append(images        )
                            out.append(options       )
                            wr.writerow(out)
                            #print (out)
                        break
                    except Exception as e:
                        #print (e)
                        pass
         
#         output_file.write(str(sku)+'\t'+str(name)+'\t'+str(category)+'\t'+str(fitment)+'\t'+str(fitment_html)+'\t'+str(url)+'\t'+str(price)+'\t'+str(features)+'\t'+str(features_html)+'\t'+str(details)+'\t'+str(details_html)+'\t'+str(images)+'\t'+str(options)+'\n')
#         output_file.flush()
    except Exception as e:
        print (e)
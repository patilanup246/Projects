# -*- coding: utf-8 -*-
'''
Created on 31-Dec-2017

@author: Administrator
'''
import requests
import re
from pyquery import PyQuery
import json
import csv


def crawl_site():
    links = []
    r = requests.get('https://www.superatv.com').text
    p = PyQuery(r)
    
    for c in p('[class="level0 nav-2 level-top full-width not-enhanced parent"] .level1 a'):
        r1 = requests.get(c.attrib['href']+'?product_list_limit=all').text
        cat_name = p(c)('span').text()
        p1 = PyQuery(r1)
        print ('Extracting category : '+str(cat_name)+'. \nItems : '+str(len(p1('[class="product name product-item-name"] a'))))
        #print (len(p1('[class="product name product-item-name"] a')))
        
        for l in p1('[class="product name product-item-name"] a'):
            #print (l.attrib['href'])
            links.append(l.attrib['href'])
            print (l.attrib['href'])
           
    print (len(list(set(links))) )
    return list(set(links))




#output_file = open('superatv.txt','w',encoding='utf-8')
output_f = open('superatv_export.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Product Type',    'Quantity',    'Collection',    'Vendor',    'Tags',    'meta descr',    'meta title',    'H1',    'SKU',    'Name',    'Category',    'Fitment',    'Fitment HTMl',    'URL',    'Price',    'Features',    'Features HTML',    'Details',    'Details HTMl',    'H2',    'Images',    'Option: 1',    'Option: 2',    'Option: 3'])
#o = xmltodict.parse(requests.get('https://www.superatv.com/sitemap.xml').text)
#for jj in ['https://www.superatv.com/4500lb-synthetic-rope-atv-winch-with-wireless-remote-1']:
for jj in crawl_site():
#for jj in ['https://www.superatv.com/can-am-commander-800-1000-long-travel-axles-3-4-5-rhino']:
    try:
        is_done = 0
        site = jj
        print (site)
        r = requests.get(site).text
        pq = PyQuery(r)
        
        try:
            t = json.loads (re.findall(r'jsonConfig: (.*),',r)[0])
            is_done = 1
            print ('Caught here')
            sku             = ''
            name            = ''
            #print ('Variants '+site)
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
            
            j = (t)
            #print (json.dumps(j))
            skus = json.loads(re.findall(r'window.configurableSimpleSku = (.*?);',r)[0])
            print (skus)
             
             
            for sku in skus.keys():
                try:
                    temp = j['index'][sku]
                    print (temp)
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
                    #options = '\t'.join(options)
                    images = ', '.join(images)
                 
                    out = []
                    out.append('')
                    out.append('')
                    out.append('')
                    out.append('')
                    out.append('')
                    out.append('')
                    out.append('')
                    out.append('<h1>'+name+'</h1>')
                    out.append(sku)
                    out.append(name)
                    out.append(category)
                    out.append(fitment.replace('Read More','.'))
                    out.append(fitment_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                    out.append(url)
                    out.append(price)
                    out.append(features.replace('Read More','.'))
                    out.append(features_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                    out.append(details.replace('Read More','.'))
                    out.append(details_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                    out.append('<h2>'+name+'</h2>')
                    out.append(images)
                    for b in options:
                        out.append(b)
                    wr.writerow(out)
                except Exception as e:
                    pass
                #print (out)
            
        except Exception as e:
            #is_done = 0
            #print ('First'+str(e))
            print (e)
            pass
    #except Exception as e:
    #    
        
        if is_done == 0:
            if not pq('[class="product-options-wrapper"]'):
                print ('Simple '+site)
                sku             = ''
                try:
                    for b in pq('[class="product attribute sku"] div'):
                        sku         = b.text
                        print (sku)
                        break
                except:
                    pass
                if sku == '':
                    continue
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
                    price = pq('[itemprop="price"] [class="price"]').text()
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
                out.append('')
                out.append('')
                out.append('')
                out.append('')
                out.append('')
                out.append('')
                out.append('')
                out.append('<h1>'+name+'</h1>')
                out.append(sku)
                out.append(name)
                out.append(category)
                out.append(fitment.replace('Read More','.'))
                out.append(fitment_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                out.append(url)
                out.append(price)
                out.append(features.replace('Read More','.'))
                out.append(features_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                out.append(details.replace('Read More','.'))
                out.append(details_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                out.append('<h2>'+name+'</h2>')
                out.append(images)
                out.append(options)
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
                            images = ['']
                            try:
                                for i in j['images'][sku]:
                                    images.append(i['full'])
                            except Exception as e:
                                pass
                             
                            price = j['optionPrices'][sku]['finalPrice']['amount']
                            sku = str(skus[sku])
                            #options = '\t'.join(options)
                            images = ', '.join(images)
                         
                            out = []
                            out.append('')
                            out.append('')
                            out.append('')
                            out.append('')
                            out.append('')
                            out.append('')
                            out.append('')
                            out.append('<h1>'+name+'</h1>')
                            out.append(sku)
                            out.append(name)
                            out.append(category)
                            out.append(fitment.replace('Read More','.'))
                            out.append(fitment_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                            out.append(url)
                            out.append(price)
                            out.append(features.replace('Read More','.'))
                            out.append(features_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                            out.append(details.replace('Read More','.'))
                            out.append(details_html.replace('<a href="javascript:void(0);" class="view-more hidden"><span>Read More</span></a>',''))
                            out.append('<h2>'+name+'</h2>')
                            out.append(images)
                            for b in options:
                                out.append(b)
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
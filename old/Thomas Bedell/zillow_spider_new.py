'''
Created on Jun 4, 2017

@author: Tasneem
'''

import requests
from pyquery import PyQuery
import csv
import re
import datetime
from threading import Thread
from Queue import Queue


file_input = open('urls_for_zillow_spider.txt').read().split("\n")


product_rows_all = []

main_url = 'https://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/globalrelevanceex_sort/33.14675,-73.970948,22.075459,-93.658448_rect/5_zm/0_mmm/'
headers_1 = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
    }
print headers_1
urls = []
file_export = open('data/csv/Zillow_Listing_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')


resp_ssl = requests.get('https://www.sslproxies.org').text
pq_ssl = PyQuery(resp_ssl)

proxy_list = []
for p in pq_ssl('table tr'):
    proxy_list.append(pq_ssl(p)('td:nth-child(1)').text()+':'+pq_ssl(p)('td:nth-child(2)').text())


proxy_count = 0
def get_new_proxy():
    #get_proxy = requests.get('https://api.proxicity.io/v2/4b1e125a576c9afa9effe8dad6c8feaf05c2956580f03c2a33db1c2b1c0e7cf7/proxy?httpsSupport=false&country=US&isAnonymous=false&userAgentSupport=true').json()['ipPort']
    global proxy_count
    proxy_count =proxy_count + 1
    get_proxy = proxy_list[proxy_count]
    print get_proxy
    proxyDict = {
        "http": "http://" + get_proxy,
        "https": "https://" + get_proxy
    }
    return proxyDict

wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Address','Street Address','City','State','Zip Code','Property URL','Property Owner','Price','Zestimate','Property Description','Zillow ID','Beds','Baths','sq_ft','HOA_Fee','Rental Value','Image URL']
wr.writerow(headers)

proxyDict = get_new_proxy()


def get_all_urls():
    for url_to_scrap in file_input:
        page=1
        while True:
            print url_to_scrap.replace('/0_mmm','/{}_p/0_mmm'.format(str(page)))
            max_tries = 20
            while True:
                print 'max-tries -' + str(max_tries)
                if max_tries == 0:
                    break
                try:
                    
                    resp = requests.get(url_to_scrap.replace('/0_mmm','/{}_p/0_mmm'.format(str(page))),headers=headers_1,proxies=proxyDict)

                    break
                except Exception:
                    proxyDict = get_new_proxy()
                    max_tries -= 1

            pq = PyQuery(resp.text)
            #print resp.text
            for listing in pq('div.zsg-photo-card-content.zsg-aspect-ratio-content > a'):
                print listing.attrib['href']
                urls.append('https://www.zillow.com'+listing.attrib['href'])
            page+=1
            if not pq('.off'):
                if not "Please verify you're a human to continue." in pq('h5').text():
                    #print resp.text
                    #print 'breaking'
                    break
    return urls

def worker(q):
#for url in get_all_urls():
    while not q.empty():
        try:

            #get_proxy = '35.196.34.212:80'
            url = q.get()

            print url
            max_tries = 20
            while True:
                print 'max-tries -'+str(max_tries)
                if max_tries == 0:
                    break
                try:
                    proxyDict = get_new_proxy()
                    resp = requests.get(url,proxies=proxyDict,headers=headers_1)
                    #print resp.text
                    pq = PyQuery(resp.text)
                    try:
                        #print 'trying'
                        address = pq('h1.notranslate').text()
                        #print address
                    except Exception, e:
                        #print e
                        max_tries -= 1
                        address = ''
                    if address:
                        break
                except Exception,e:
                    print e
                    proxyDict = get_new_proxy()
                    max_tries -= 1


            try:
                address = pq('h1.notranslate').text()
            except Exception,e:
                address = ''

            try:
                street_address = address.split(',')[0]
            except Exception,e:
                street_address = ''

            try:
                city = pq('.zsg-h2.addr_city').text().split(',')[0]
            except Exception,e:
                city = ''

            try:
                state = pq('.zsg-h2.addr_city').text().split(',')[1].strip().split(' ')[0]
            except Exception,e:
                state=''

            try:
                zipcode = pq('.zsg-h2.addr_city').text().split(',')[1].strip().split(' ')[1]
            except Exception,e:
                zipcode=''

            try:
                property_url = url
            except Exception,e:
                property_url=''

            try:
                property_owner = pq('form#lead-form_contact-tall span:contains("Property Owner")').parent()('.snl.phone').text()
            except Exception,e:
                property_owner=''

            try:
                price = pq('.estimates .main-row.home-summary-row span').text()
            except Exception,e:
                price=''

            try:
                zestimate = pq('span:contains("Zestimate")').parent()('span[class=""]').text()
            except Exception,e:
                zestimate=''

            try:
                property_description = pq('.hdp-header-description [class="zsg-content-component"]').text()
            except Exception,e:
                property_description=''

            try:
                zillow_id = url.split('/')[-2].replace('_zpid','')
            except Exception,e:
                zillow_id=''

            try:
                bed = pq('.zsg-content-header.addr h3 span:nth-child(2)').text()
            except Exception,e:
                bed=''

            try:
                bath = pq('.zsg-content-header.addr h3 span:nth-child(4)').text()
            except Exception,e:
                bath=''

            try:
                sqft = pq('.zsg-content-header.addr h3 span:nth-child(6)').text()
            except Exception,e:
                sqft=''

            try:
                hoa_fees = pq('span:contains("HOA Fee: ")').parent()('span:nth-child(2)').text()
            except Exception,e:
                hoa_fees=''

            try:
                rental_value = pq('.zest-content div:contains("Rent Zestimate ")').parent()('.zest-value').text()
            except Exception,e:
                rental_value=''

            try:
                image = pq('.lg-tile.current img').attr('src')
            except Exception,e:
                image=''

            product_row = []

            product_row.append( address.encode('ascii','ignore') )
            product_row.append( street_address.encode('ascii','ignore')    )
            product_row.append( city.encode('ascii','ignore') )
            product_row.append( state.encode('ascii','ignore') )
            product_row.append( zipcode.encode('ascii','ignore') )
            product_row.append( property_url.encode('ascii','ignore') )
            product_row.append( re.sub("\D", "", property_owner.replace(',', '')) )
            product_row.append( re.sub("\D", "", price.replace(',', '')) )
            product_row.append( re.sub("\D", "", zestimate.replace(',', '')) )
            product_row.append( property_description.encode('ascii','ignore') )
            product_row.append( zillow_id )
            product_row.append( re.sub("\D", "", bed.replace(',', '')) )
            product_row.append( re.sub("\D", "", bath.replace(',', '')) )
            product_row.append( re.sub("\D", "", sqft.replace(',', '')) )
            product_row.append( re.sub("\D", "", hoa_fees.replace(',', '')) )
            product_row.append( re.sub("\D", "", rental_value.split(' ')[0].replace(',', '')) )
            product_row.append( image )

            #wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
            wr.writerow(product_row)
            #file_export.write
        except Exception,e:
            print e
    



q = Queue()
map(q.put, list(set(get_all_urls())))
for i in range(1):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()


#file_export.close()
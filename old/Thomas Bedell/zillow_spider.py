'''
Created on Jun 4, 2017

@author: Tasneem
'''

from pyquery import PyQuery
import csv
import re
import datetime
import requests
from time import sleep, time
start_time = time()


file_input = open('urls_for_zillow_spider-50-states.txt').read().split("\n")

product_rows_all = []

main_url = 'https://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/globalrelevanceex_sort/33.14675,-73.970948,22.075459,-93.658448_rect/5_zm/0_mmm/'
headers_1 = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    #'referer': "https://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/globalrelevanceex_sort/30.481817,-78.887329,24.941238,-88.731079_rect/6_zm/0_mmm/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    'cookie': "JSESSIONID=A08C5392748719908ACF2947D560EDCF; abtest=3|DB1zz5Cx4rWpWiECpA; zguid=23|%246241df5a-2efb-4bcd-81cc-b55e0e01c2ea; search=6|1504969145918%7Crect%3D26.970579%252C-79.999952%252C26.889311%252C-80.153761%26zm%3D12%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D1%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%09%01%09%09%09%09%090%09US_%09; AWSALB=1YMSgdwAlBODkRT/GE0uAdD2ebjYh0bFPJE8SZI+gkzTPFjglOcyKykr4CWbeHP407dqFKz7/9K/TfsfyABZiOBdTwkUcs9ES9Wer8dsV8ZGvvIIjBjBz+bEnoYH"
    }

headers_2 = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    #'referer': "https://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/globalrelevanceex_sort/30.481817,-78.887329,24.941238,-88.731079_rect/6_zm/0_mmm/",
    #'cookie': "JSESSIONID=A08C5392748719908ACF2947D560EDCF; abtest=3|DB1zz5Cx4rWpWiECpA; zguid=23|%246241df5a-2efb-4bcd-81cc-b55e0e01c2ea; search=6|1504969145918%7Crect%3D26.970579%252C-79.999952%252C26.889311%252C-80.153761%26zm%3D12%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D1%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%09%01%09%09%09%09%090%09US_%09; AWSALB=1YMSgdwAlBODkRT/GE0uAdD2ebjYh0bFPJE8SZI+gkzTPFjglOcyKykr4CWbeHP407dqFKz7/9K/TfsfyABZiOBdTwkUcs9ES9Wer8dsV8ZGvvIIjBjBz+bEnoYH",
    'upgrade-insecure-requests': "1",
    'user-agent': "motherofallbots"
    }



# file_export = open('data/csv/Zillow_Listing_' + str(datetime.datetime.today().strftime('%Y-%m-%d')) + '.csv', 'wb')

proxy_count = 0

key = '470293534c3539ee56bf985d49435ca1'
def get_by_2cap(site_key, url1):
    global key
    url = "http://2captcha.com/in.php?key=" + key + "&method=userrecaptcha&googlekey=" + site_key + "&pageurl=" + url1
    resp = requests.get(url)
    print resp.text
    if resp.text[0:2] != 'OK':
        quit('Error. Captcha is not received')
    captcha_id = resp.text[3:]

    fetch_url = "http://2captcha.com/res.php?key=" + key + "&action=get&id=" + captcha_id
    for i in range(1, 600):
        sleep(1)  # wait 5 sec.
        resp = requests.get(fetch_url)
        if resp.text[0:2] == 'OK':
            break

    print('Time to solve: ', time() - start_time)

    submit_url = url1

    payload = {'submit': 'submit', 'g-recaptcha-response': resp.text[3:]}
    resp = requests.post(submit_url, headers=headers_2, data=payload)
    #print resp.text
    return resp





def get_all_urls(num):
    urls = []
    url_to_scrap = file_input[num]
    page = 1
    while True:
        print url_to_scrap.replace('/0_mmm', '/{}_p/0_mmm'.format(str(page)))
        try:
            headers_2 = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.8",
                'cache-control': "no-cache",
                'pragma': "no-cache",
                # 'referer': "https://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/globalrelevanceex_sort/30.481817,-78.887329,24.941238,-88.731079_rect/6_zm/0_mmm/",
                # 'cookie': "JSESSIONID=A08C5392748719908ACF2947D560EDCF; abtest=3|DB1zz5Cx4rWpWiECpA; zguid=23|%246241df5a-2efb-4bcd-81cc-b55e0e01c2ea; search=6|1504969145918%7Crect%3D26.970579%252C-79.999952%252C26.889311%252C-80.153761%26zm%3D12%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D1%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%09%01%09%09%09%09%090%09US_%09; AWSALB=1YMSgdwAlBODkRT/GE0uAdD2ebjYh0bFPJE8SZI+gkzTPFjglOcyKykr4CWbeHP407dqFKz7/9K/TfsfyABZiOBdTwkUcs9ES9Wer8dsV8ZGvvIIjBjBz+bEnoYH",
                'upgrade-insecure-requests': "1",
                'user-agent': "motherofallbots"+str(page)
            }

            resp = requests.get(url_to_scrap.replace('/0_mmm', '/{}_p/0_mmm'.format(str(page))),
                                headers=headers_2)
            pq = PyQuery(resp.text)
            if "Please verify you're a human to continue." in pq('h5').text():
                resp = get_by_2cap(pq('.g-recaptcha').attr('data-sitekey'),url_to_scrap.replace('/0_mmm', '/{}_p/0_mmm'.format(str(page))))
                pq = PyQuery(resp.text)
            else:
                pass
            for listing in pq('div.zsg-photo-card-content.zsg-aspect-ratio-content > a'):
                print listing.attrib['href']
                urls.append('https://www.zillow.com' + listing.attrib['href'])
            page += 1
        except Exception,e:
            print e
        if not pq('.off'):
            break
    return urls




for i in range(0,50):
    file_export = open('data/csv_all/Zillow_Listing_' + str(i) + '.csv',
                       'wb')
    wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
    headers = ['Address', 'Street Address', 'City', 'State', 'Zip Code', 'Property URL', 'Property Owner', 'Price',
               'Zestimate', 'Property Description', 'Zillow ID', 'Beds', 'Baths', 'sq_ft', 'HOA_Fee', 'Rental Value',
               'Image URL']
    wr.writerow(headers)
    url_num = 1
    for url in list(set(get_all_urls(i))):

        try:

            url_num+=1
            print url

            try:
                headers_2 = {
                    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    'accept-encoding': "gzip, deflate, br",
                    'accept-language': "en-US,en;q=0.8",
                    'cache-control': "no-cache",
                    'pragma': "no-cache",
                    # 'referer': "https://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/globalrelevanceex_sort/30.481817,-78.887329,24.941238,-88.731079_rect/6_zm/0_mmm/",
                    # 'cookie': "JSESSIONID=A08C5392748719908ACF2947D560EDCF; abtest=3|DB1zz5Cx4rWpWiECpA; zguid=23|%246241df5a-2efb-4bcd-81cc-b55e0e01c2ea; search=6|1504969145918%7Crect%3D26.970579%252C-79.999952%252C26.889311%252C-80.153761%26zm%3D12%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D1%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%09%01%09%09%09%09%090%09US_%09; AWSALB=1YMSgdwAlBODkRT/GE0uAdD2ebjYh0bFPJE8SZI+gkzTPFjglOcyKykr4CWbeHP407dqFKz7/9K/TfsfyABZiOBdTwkUcs9ES9Wer8dsV8ZGvvIIjBjBz+bEnoYH",
                    'upgrade-insecure-requests': "1",
                    'user-agent': "motherofallbots"+str(url_num)
                }
                resp = requests.get(url, headers=headers_2)
                pq = PyQuery(resp.text)
                if "Please verify you're a human to continue." in pq('h5').text():
                    resp = get_by_2cap(pq('.g-recaptcha').attr('data-sitekey'),url)
                    pq = PyQuery(resp.text)
                else:
                    pass
                address = pq('h1.notranslate').text()
            except Exception, e:
                address = ''




            try:
                address = pq('h1.notranslate').text()
            except Exception, e:
                address = ''

            try:
                street_address = address.split(',')[0]
            except Exception, e:
                street_address = ''

            try:
                city = pq('.zsg-h2.addr_city').text().split(',')[0]
            except Exception, e:
                city = ''

            try:
                state = pq('.zsg-h2.addr_city').text().split(',')[1].strip().split(' ')[0]
            except Exception, e:
                state = ''

            try:
                zipcode = pq('.zsg-h2.addr_city').text().split(',')[1].strip().split(' ')[1]
            except Exception, e:
                zipcode = ''

            try:
                property_url = url
            except Exception, e:
                property_url = ''

            try:
                property_owner = pq('form#lead-form_contact-tall span:contains("Property Owner")').parent()(
                    '.snl.phone').text()
            except Exception, e:
                property_owner = ''

            try:
                price = pq('.estimates .main-row.home-summary-row span').text()
            except Exception, e:
                price = ''

            try:
                zestimate = pq('span:contains("Zestimate")').parent()('span[class=""]').text()
            except Exception, e:
                zestimate = ''

            try:
                property_description = pq('.hdp-header-description [class="zsg-content-component"]').text()
            except Exception, e:
                property_description = ''

            try:
                zillow_id = url.split('/')[-2].replace('_zpid', '')
            except Exception, e:
                zillow_id = ''

            try:
                bed = pq('.zsg-content-header.addr h3 span:nth-child(2)').text()
            except Exception, e:
                bed = ''

            try:
                bath = pq('.zsg-content-header.addr h3 span:nth-child(4)').text()
            except Exception, e:
                bath = ''

            try:
                sqft = pq('.zsg-content-header.addr h3 span:nth-child(6)').text()
            except Exception, e:
                sqft = ''

            try:
                hoa_fees = pq('span:contains("HOA Fee: ")').parent()('span:nth-child(2)').text()
            except Exception, e:
                hoa_fees = ''

            try:
                rental_value = pq('.zest-content div:contains("Rent Zestimate ")').parent()('.zest-value').text()
            except Exception, e:
                rental_value = ''

            try:
                image = pq('.lg-tile.current img').attr('src')
            except Exception, e:
                image = ''

            product_row = []

            product_row.append(address.encode('ascii', 'ignore'))
            product_row.append(street_address.encode('ascii', 'ignore'))
            product_row.append(city.encode('ascii', 'ignore'))
            product_row.append(state.encode('ascii', 'ignore'))
            product_row.append(zipcode.encode('ascii', 'ignore'))
            product_row.append(property_url.encode('ascii', 'ignore'))
            product_row.append(re.sub("\D", "", property_owner.replace(',', '')))
            product_row.append(re.sub("\D", "", price.replace(',', '')))
            product_row.append(re.sub("\D", "", zestimate.replace(',', '')))
            product_row.append(property_description.encode('ascii', 'ignore'))
            product_row.append(zillow_id)
            product_row.append(re.sub("\D", "", bed.replace(',', '')))
            product_row.append(re.sub("\D", "", bath.replace(',', '')))
            product_row.append(re.sub("\D", "", sqft.replace(',', '')))
            product_row.append(re.sub("\D", "", hoa_fees.replace(',', '')))
            product_row.append(re.sub("\D", "", rental_value.split(' ')[0].replace(',', '')))
            product_row.append(image)

            # wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
            wr.writerow(product_row)
            # file_export.write

        except Exception, e:
            print e

fout=open("data/csv_all/zillow_merged_file.csv","a")
# first file:
for line in open("data/csv_all/Zillow_Listing_0.csv"):
    fout.write(line)
# now the rest:
for num in range(1,50):
    f = open("data/csv_all/Zillow_Listing_"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()


    # q = Queue()
    # map(q.put, list(set(get_all_urls())))
    # for i in range(10):
    #     #print i
    #     t = Thread(target=worker, args=(q, ))
    #     t.start()


            # file_export.close()
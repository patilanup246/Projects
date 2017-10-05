import requests
from pyquery import PyQuery
import csv
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
file_export = open('lonely_planet_output.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "www.lonelyplanet.com",
    'pragma': "no-cache",
    'referer': "https://www.lonelyplanet.com/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
    }

all_countries = 'https://www.lonelyplanet.com/places'

response = requests.request("GET", all_countries, headers=headers)

pq_all = PyQuery(response.text)

for country in pq_all('.card.card--list.media'):
    country_href = country.attrib['href']
    print country_href
    #country_href = '/brazil'
    country_main = 'https://www.lonelyplanet.com'+country_href
    country_essential = 'https://www.lonelyplanet.com'+ country_href + '/essential-information'
    country_child = 'https://www.lonelyplanet.com'+ country_href + '/travelling-with-children'

    resp_main = requests.request("GET", country_main, headers=headers)
    resp_essential = requests.request("GET", country_essential, headers=headers)
    resp_child = requests.request("GET", country_child, headers=headers)

    pq_main = PyQuery(resp_main.text)
    pq_essential = PyQuery(resp_essential.text)
    pq_child = PyQuery(resp_child.text)

    row = []

    row.append(pq_main('.masthead__title').text().strip().replace('\n',''))
    row.append(pq_essential('.flip-chart').text().strip().replace('\n','').replace(' ',','))
    row.append('')
    low = re.findall(r'\d+',pq_essential('.has-heading .budget__price').text().strip().replace('\n',''))
    if low:
        if len(low) == 1:
            row.append(low[0])
        else:
            row.append(low[0]+'-'+low[1])
    else:
        row.append('')

    midrange = re.findall(r'\d+',pq_essential('.budget__container--col__title--midrange .budget__price').text().strip().replace('\n',''))
    if midrange:
        if len(midrange) == 1:
            row.append(midrange[0])
        else:
            row.append(midrange[0]+'-'+midrange[1])
    else:
        row.append('')

    top = re.findall(r'\d+',pq_essential('.budget__container--col__title--top .budget__price').text().strip().replace('\n',''))
    if top:
        if len(top) == 1:
            row.append( top[0])
        else:
            row.append( top[0]+'-'+top[1])
    else:
        row.append('')

    row.append( pq_essential('.budget__container--col.col--one-whole.mv--col--one-half.wv--col--one-quarter .copy--feature').text().strip().replace('\n',''))
    row.append( pq_essential('.seasonal__col-header--low .seasonal__col__time').text().strip().replace('\n',''))
    row.append( pq_essential('.seasonal__col-header--shoulder .seasonal__col__time').text().strip().replace('\n',''))
    row.append( pq_essential('.seasonal__col-header--high .seasonal__col__time').text().strip().replace('\n',''))
    row.append( pq_child('.card--page__content .copy--body:nth-child(1)').text().strip().replace('\n',''))

    for interest in pq_main('.interests__card__link'):
        row.append( interest.text.strip().replace('\n',''))

    wr.writerow(row)
file_export.close()




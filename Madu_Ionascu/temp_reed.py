'''
Created on Jul 4, 2018

@author: talib
'''
import xmltodict, requests, json

all_urls = []
urls = [
    
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0000.xml',
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0001.xml',
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0002.xml',
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0003.xml',
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0004.xml',
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0005.xml',
    'https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_0006.xml'
    
    ]
x = xmltodict.parse(requests.get('https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_index.xml').text)
last_mod = ''
for m in reversed(x['sitemapindex']['sitemap']):
    print (m['loc'])
    last_mod = m['lastmod'].split('T')[0]
    
#https://www.totaljobs.com/jobs-sitemaps/01.xml
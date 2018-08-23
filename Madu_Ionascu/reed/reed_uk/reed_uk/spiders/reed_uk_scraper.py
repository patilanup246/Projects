# -*- coding: utf-8 -*-


from reed_uk.items import ReedUkItem
import scrapy
import requests
import xmltodict
import re
from pyquery import PyQuery

class reeduk(scrapy.Spider):
    name="reed_uk"
    all_urls = []
    
    def __init__(self,*args,**kwargs):
        
        link_urls = []
        x = xmltodict.parse(requests.get('https://www.reed.co.uk/sitemaps/livejobs/sitemap_livejobs_index.xml').text)
        last_mod = ''
        for m in reversed(x['sitemapindex']['sitemap']):
            link_urls.append (m['loc'])
            last_mod = m['lastmod'].split('T')[0]
        is_done = 0
        for u in link_urls:
            x = xmltodict.parse(requests.get(u).text)
            print (u)
            for m in reversed(x['urlset']['url']):
                
                if last_mod in m['lastmod']:
                    self.all_urls.append (m['loc'])
                    print (m['loc'],m['lastmod'])
                else:
                    
                    is_done = 1
                    break
            
            if is_done:
                break
        
        
        
        
        

    def start_requests(self):
        headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'cache-control': "no-cache",
            'pragma': "no-cache",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        for url in self.all_urls:
            
                
            request =  scrapy.Request(url=url, headers=headers, callback=self.parse)
            
            yield request
    
    def parse(self, response):
        item = ReedUkItem()
        resp_html = response.body_as_unicode()
        pq = PyQuery(resp_html)
        
        
       
                        
        try:
            item['source_post_id']= re.findall("jobId: '(.*?)'", resp_html)[0]
        except Exception as e:
            pass
        item['url']=response.url
        item['posted_date']=pq('[itemprop="datePosted"]').attr('content')
        item['close_date']=str(pq('[itemprop="validThrough"]').attr('content')).split('T')[0]
        item['location']= 'UK'
        item['city']= pq('[itemprop="addressLocality"]').text()
        item['state']=pq('[itemprop="addressRegion"]').attr('content')
        item['country']=pq('[itemprop="addressCountry"]').attr('content')
        item['job_title_raw']=pq('.job-details h1').text()
        try:
            item['category']=re.findall("jobKnowledgeDomain: '(.*?)'", resp_html)[0]
        except Exception as e:
            pass
        item['type']=pq('[itemprop="workHours"]').attr('content')
        item['company_raw']=pq('[itemprop="hiringOrganization"] [itemprop="name"]').text()
        item['company_url']=str(pq('[itemprop="hiringOrganization"] [itemprop="url"]').attr('content')).split('?')[0]
        item['company_type']=''
        item['company_logo']=str(pq('[itemprop="logo"]').attr('content')).split('?')[0]
        item['industry_raw']=pq('[itemprop="industry"]').attr('content')
        item['salary_from']=pq('[itemprop="minValue"]').attr('content')
        item['salary_to']=pq('[itemprop="maxValue"]').attr('content')
        item['salary_currency']=pq('[itemprop="currency"]').attr('content')
        item['salary_period']=pq('[itemprop="unitText"]').attr('content')
        item['description'] = pq('[itemprop="description"]').text()
        
        
        
        yield item
        

    
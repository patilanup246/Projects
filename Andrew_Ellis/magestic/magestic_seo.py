# coding=utf-8
# import requests
#
# url = "https://majestic.com/reports/site-explorer/referring-domains"
#
# querystring = {"folder":"","q":"https://www.google.com","oq":"https://www.google.com","IndexDataSource":"F"}
#
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
#     'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     'accept-language': "en-US,en;q=0.5",
#     'accept-encoding': "gzip, deflate, br",
#     'referer': "https://majestic.com/reports/site-explorer?q=https%3A%2F%2Fwww.google.com&oq=https%3A%2F%2Fwww.google.com&IndexDataSource=F",
#     'cookie': "_ga=GA1.2.1268750394.1504579310; STOK=xzIVUuO1acQrsSTuqn1GbCias6; _gid=GA1.2.1628048600.1505221883; _gat=1",
#     'dnt': "1",
#     'proxy-authorization': "Basic Z3JvdXBidXlzZW90b29sczpTZTBUbzBMczJTNA==",
#     'connection': "keep-alive",
#     'upgrade-insecure-requests': "1"
#     }
#
# #response = requests.request("GET", url, headers=headers, params=querystring,verify=False)
#
# #print(response.text)


import requests
import urllib
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv

output_f = open('output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Site','Title',    'Domain',    'RefDomains',    'AlexaRank',    'Matches',    'MatchedLinks',    'ExtBackLinks',    'IndexedURLs',    'CrawledURLs',    'FirstCrawled',    'LastSuccessfulCrawl',    'IP',    'SubNet',    'CountryCode',    'TLD',    'TrustFlow',    'CitationFlow',    'BackLinks_https://www.quora.com',    'FirstLinkDate_https://www.quora.com',    'LastLinkDate_https://www.quora.com',    'TopicalTrustFlow_Topic_0',    'TopicalTrustFlow_Value_0',    'TopicalTrustFlow_Topic_1',    'TopicalTrustFlow_Value_1',    'TopicalTrustFlow_Topic_2',    'TopicalTrustFlow_Value_2',    'TopicalTrustFlow_Topic_3',    'TopicalTrustFlow_Value_3',    'TopicalTrustFlow_Topic_4',    'TopicalTrustFlow_Value_4',    'TopicalTrustFlow_Topic_5',    'TopicalTrustFlow_Value_5',    'TopicalTrustFlow_Topic_6',    'TopicalTrustFlow_Value_6',    'TopicalTrustFlow_Topic_7',    'TopicalTrustFlow_Value_7',    'TopicalTrustFlow_Topic_8',    'TopicalTrustFlow_Value_8',    'TopicalTrustFlow_Topic_9',    'TopicalTrustFlow_Value_9',    'LinksPerCrawledUrl',    'OutlinkCheckedPages',    'AverageInternalOutlinksPerPage',    'AverageExternalOutlinksPerPage',    'AverageTotalOutlinksPerPage',    'AverageExternalDomainsPerPage',    'DomainLanguage_0',    'DomainLanguage_PageRatio_0',    'DomainLanguage_1',    'DomainLanguage_PageRatio_1',    'DomainLanguage_2',    'DomainLanguage_PageRatio_2'])


url = "https://majestic.com/data-output"

read_input = open('urls.txt','r').read().split('\n')

for input_url in read_input:
    print (input_url)
    print ('waiting for 10 seconds')
    
    payload = "OrderBy1=11&OrderBy2=1&OrderDir1=1&OrderDir2=0&RefDomain=&UsePrefixScan=0&format=Csv&index_data_source=Fresh&item="+urllib.parse.quote_plus(input_url.strip())+"&request_name=ExplorerReferringDomains"
    headers = {
        'origin': "https://majestic.com",
        'upgrade-insecure-requests': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'cookie': "_ga=GA1.2.929496905.1521231313; STOK=3meVWSIpSsIFsCm0rXueIFBar6; _gid=GA1.2.1990622334.1523633053; _gat=1"
        }

    response = requests.request("POST", url.strip(), data=payload, headers=headers,verify=False)
    
    i = 0
    reader = csv.reader(response.text, delimiter=',')
    for r in reader:
        
        details = []
        if i > 0:
            print (r)
            
            wr.writerow(r)
            
        i+=1
    #time.sleep(10)
    
    break
    
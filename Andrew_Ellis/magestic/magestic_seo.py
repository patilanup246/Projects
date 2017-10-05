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
url = "https://majestic.com/data-output"
file_write = open('output.tsv','w',encoding='utf-8')
read_input = open('urls.txt','r').read().split('\n')
head ='URL'+'\t'+'Position'+'\t'+'Title'+'\t'+'Domain'+'\t'+'RefDomains'+'\t'+'AlexaRank'+'\t'+'Matches'+'\t'+'MatchedLinks'+'\t'+'ExtBackLinks'+'\t'+'IndexedURLs'+'\t'+'CrawledURLs'+'\t'+'FirstCrawled'+'\t'+'LastSuccessfulCrawl'+'\t'+'IP'+'\t'+'SubNet'+'\t'+'CountryCode'+'\t'+'TLD'+'\t'+'TrustFlow'+'\t'+'CitationFlow'+'\t'+'BackLinks'+'\t'+'FirstLinkDate'+'\t'+'LastLinkDate'+'\t'+'TopicalTrustFlow_Topic_0'+'\t'+'TopicalTrustFlow_Value_0'+'\t'+'TopicalTrustFlow_Topic_1'+'\t'+'TopicalTrustFlow_Value_1'+'\t'+'TopicalTrustFlow_Topic_2'+'\t'+'TopicalTrustFlow_Value_2'+'\t'+'TopicalTrustFlow_Topic_3'+'\t'+'TopicalTrustFlow_Value_3'+'\t'+'TopicalTrustFlow_Topic_4'+'\t'+'TopicalTrustFlow_Value_4'+'\t'+'TopicalTrustFlow_Topic_5'+'\t'+'TopicalTrustFlow_Value_5'+'\t'+'TopicalTrustFlow_Topic_6'+'\t'+'TopicalTrustFlow_Value_6'+'\t'+'TopicalTrustFlow_Topic_7'+'\t'+'TopicalTrustFlow_Value_7'+'\t'+'TopicalTrustFlow_Topic_8'+'\t'+'TopicalTrustFlow_Value_8'+'\t'+'TopicalTrustFlow_Topic_9'+'\t'+'TopicalTrustFlow_Value_9'+'\n'
file_write.write(head)
for input_url in read_input:
    print (input_url)
    print ('waiting for 10 seconds')
    time.sleep(10)
    payload = "OrderBy1=11&OrderBy2=1&OrderDir1=1&OrderDir2=0&RefDomain=&UsePrefixScan=0&format=Tsv&index_data_source=Fresh&item="+urllib.parse.quote_plus(input_url.strip())+"&request_name=ExplorerReferringDomains"
    headers = {
        'origin': "https://majestic.com",
        'upgrade-insecure-requests': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'cookie': "RURI=reports%2Fsite-explorer%2Freferring-domains; STOK=xzIVUuO1acQrsSTuqn1GbCias6; _ga=GA1.2.1418919426.1505222058; _gid=GA1.2.2101991413.1505222058; _gat=1; _pk_id.2.c4b1=e2b2cacd5fba6801.1505222060.1.1505223662.1505222060.; _pk_ses.2.c4b1=*"
        }

    response = requests.request("POST", url, data=payload, headers=headers,verify=False)
    i = 0
    for r in response.text.split('\n'):

        if i > 0:
            file_write.write(input_url+r)
        i+=1
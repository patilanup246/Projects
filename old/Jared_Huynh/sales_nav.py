'''
Created on May 13, 2017

@author: Mukadam
'''
import requests
import csv,time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

myfile = open('sales_nav_export.csv', 'a')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)


url = "https://www.linkedin.com/sales/search/results"


headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': 'JSESSIONID=ajax:2554699527436527216; bcookie="v=2&8e12d4fe-385d-4713-8cd2-37e833d3ce15"; bscookie="v=1&20170503171146a1f8a61f-6940-4571-8bed-a751e1031436AQH6QTGggVn8CGlpf9lu1xgMEqmOmVPZ"; _ga=GA1.2.371711646.1493831506; visit="v=1&M"; _lipt=CwEAAAFcAKIEqVhKotmJTic0IQuAirhksxhxNlByp18hnSOG87zAaOYMEXUa5l1Aqd-9aMdrEx1kthDUTHDAPf2XOwCMW4UJsri6aP7Mp6Rvv6bXCGdurvoKrEk; lang="v=2&lang=en-us"; sdsc=48%3A1%2C1494659384744%7ECAOR%2C0%7ECAST%2C-182204%7ECATG%2C-182021nmlckTyw%2B%2BEzMjMpGyNJ1faxxwg%3D; lidc="b=SGST07:g=2:u=1:i=1494659087:t=1494745487:s=AQHFH2ZuOfdRMUbB7x-b1AC_Nhcei3aD"; mst="v=1&yzk2G"; onboarding_session=052f360d-5558-4ffd-84f8-9cd188b0edd9; RT=s=1494659396987&r=https%3A%2F%2Fwww.linkedin.com%2Fsales%2Fhome%3FwithModule%3DNUX_ONBOARDING_V2%26syncedCrm%3Dfalse; li_at=AQEDASKhZAYCPjZDAAABXACfvFwAAAFcAlcwXFEAzXkQs5mehIrOor2ZIyWek3mXoqPrAhXL4lAtGxvVpajdeq-qjafJkLvORMuI4maHSxRL4tSb0OJAtO-5TLfCS-432_P64GaiWL5QKhbj40UaaXYj; sl=v=1&kLRyD; liap=true; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4MDQ5MDgwOSUzQSUzQTgzMzQwODA59aNFxd78ZUQMEnY_aIMgEaf0E8s',
    #'referer': "https://www.linkedin.com/sales/search?facet=G&facet=I&facet=CS&facet.G=au%3A4910&facet.I=96&facet.CS=C&titleScope=CURRENT&jobTitleEntities=CEO_8&count=25&start=25&updateHistory=true&searchHistoryId=1298964655&trackingInfoJson.contextId=FEE1F4492FDFBD14001A2264A72B0000",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache"
    }

#industry_types = ['1','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140','141','142','143','144','145','146','147','148','149']
#industry_types = ['1','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40']
#industry_types = ['41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80']
#industry_types = ['81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140','141','142','143','144','145','146','147','148','149']
industry_types = ['57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140','141','142','143','144','145','146','147','148','149']



#company_size = 'C'
company_size = 'D'




#title = 'CEO_8'
title = 'Director_5'
#title = 'Owner_1'


for industry_type in industry_types:
    start = 0
    while True:
        querystring = {"facet":["G","I","CS"],"facet.G":"au:4910","facet.I":industry_type,"facet.CS":company_size,"titleScope":"CURRENT","jobTitleEntities":title,"count":"25","start":start,"updateHistory":"true","searchHistoryId":"1298964655","trackingInfoJson.contextId":"FEE1F4492FDFBD14001A2264A72B0000","trackingInfoJson.requestId":"d53d7c97-e959-4c81-8669-37dffa7b881b","_":"1494614122023"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print response.text
        print 'industry_type - {}. start - {}. searchResults - {}'.format(industry_type,str(start),str(len(response.json()['searchResults'])))
        
        if not len(response.json()['searchResults']):
            break
        for profile in response.json()['searchResults']:
            mylist = []
            try:
                mylist.append(profile['member']['formattedName'])
            except Exception,e:
                mylist.append('')
            try:
                mylist.append(profile['member']['title'].replace('<b>','').replace('</b>',''))
            except Exception,e:
                mylist.append('')
            try:
                mylist.append(profile['company']['companyName'])
            except Exception,e:
                mylist.append('')
            wr.writerow(mylist)
        if len(response.json()['searchResults'])<25:
            break
        #time.sleep(5)
                
            #print(profile['member']['formattedName'])
        start+=25
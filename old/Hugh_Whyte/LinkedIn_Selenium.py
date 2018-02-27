import requests

url = "https://www.linkedin.com/voyager/api/search/cluster?count=10&guides=List(v-%3EPEOPLE,facetGeoRegion-%3Egd%3A0)&origin=GLOBAL_SEARCH_HEADER&q=guided&searchId=1493626303847&start=10"


headers = {
    'accept': "application/vnd.linkedin.normalized+json",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': 'bcookie="v=2&3305621b-454a-4b33-87fa-9e84211d0a91"; bscookie="v=1&201702191051039e5509a6-2e5c-4ec5-8393-5355b3b38ebfAQHSoBj6f11H5LmW_aL9-ow_qnlRt2gQ"; visit="v=1&M"; VID=V_2017_03_27_09_199; pushPermState=default; lang="v=2&lang=en-us"; _ga=GA1.2.501110755.1487515805; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; lidc="b=SB92:g=35:u=123:i=1493731311:t=1493817709:s=AQEXu17pqUccE2ws2DNin5GiRxtIiBo0"; li_at=AQEDAQXQY1ADfxAJAAABW8L8vloAAAFbyyQWllEAtPKHft7X-mLTwZnxd5QVZRo4iYNvvgAwwVeHme71h8b2i_rY1hzflsvQMab0i7EytClEcSTBaO2mAHs8mfnphsX04r271REPqGxqBL0YANspz8H_; liap=true; sl="v=1&qOOdP"; JSESSIONID="ajax:7630642286208202409"; _lipt=CwEAAAFbyYT9LfWYPtnGfatFe8KH1qlH2Ofq4k9Vm3B3QgoCKYxq-7Dy7reol9OhAnhHYifKH2rVA_K2_AOT7iGTpDPRlT6kKN7l8SHBnFKex6eqEFnhEEE6EvUhNzCLd4BQZE6jXVkeamKHflWPSUSDV759djnhJ2fGc-KXtFWNcbPGqDczkPw9pYqRJ-670afjmPRguqmnZXOGHTm0ty5JDtLCtHJ4hgk9-rNsA2633gUyzcEUK51UHCnKjWJ7dedz6WRgs00H44Z_OoRHBv9FELNWqemGBI2eQXz1LD8JhlkZ0BdJxjMEnPl_E8E7pT4JwPaJqpA0KXv6gssvlerF6du4q-jjlJNkyhFTM53Cst5NiuZvYxdwDDJGOflejy0FcFugni1U7lbpFTrm7_9Ow9z-Gt5PA-OS6oM8-TstxIc6WuXUlLRSKYasjLAHVpoWkzAf1d64Sr7lfdIaoenwZ4MWq2CEEWjG1Vnlh5Lg6AZ4vy2hDv4ciGDuTxW_W8X6WIalhKkLU1Qml0LDxqPrCBXlhVsFnUp-xTnESi21rTjw6rK0qA4AW3kDNF6cWw2WAKjUqwbHNlmXvRqJtyMaTVC56w',
    'csrf-token': "ajax:7630642286208202409",
    'referer': "https://www.linkedin.com/",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'x-li-lang': "en_US",
    'x-li-page-instance': "urn:li:page:d_flagship3_search_srp_people;/P2/McPcSr6b881uLajz7g==",
    'x-li-track': "{\"clientVersion\":\"1.0.*\",\"osName\":\"web\",\"clientTimestamp\":1493625745706,\"timezoneOffset\":5.5,\"deviceFormFactor\":\"DESKTOP\"}",
    'x-requested-with': "XMLHttpRequest",
    'x-restli-protocol-version': "2.0.0",
    'cache-control': "no-cache"
    }
file_output = open('file_output.txt','w')
listers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for list_item in listers:
    for list_item1 in listers:
        print list_item+list_item1
        i=0
        while True:
            count = 0
            response = requests.request("GET", url = "https://www.linkedin.com/voyager/api/search/cluster?count=10&guides=List(v-%3EPEOPLE,facetGeoRegion-%3Egd%3A0)&origin=GLOBAL_SEARCH_HEADER&keywords="+list_item+list_item1+"&q=guided&start="+str(i*10), headers=headers)
            #file_output_2.write(response.text.encode('utf-8').strip()+'\n')
            #print response.text
            print(str(i*10))
            
            for item in response.json()['included']:
                try:
                    firstName = item['firstName'].replace('\n',' ')+'\t'
                    lastName = item['lastName'].replace('\n',' ')+'\t'
                    occupation = item['occupation'].replace('\n',' ')+'\t'
                    objectUrn = item['objectUrn'].replace('\n',' ')+'\t'
                    publicIdentifier =  item['publicIdentifier'].replace('\n',' ')
                    file_output.write(firstName + lastName + occupation + objectUrn + publicIdentifier+'\n')
                    count = 1
                except Exception,e:
                    pass
                file_output.flush()
            i+=1
            if count == 0:
                break
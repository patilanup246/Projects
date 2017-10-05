'''
Created on May 13, 2017

@author: Mukadam
'''
import requests
import urllib

url = "https://www.linkedin.com/voyager/api/typeahead/hits"

file_queries = open('queries.txt','r').read().split('\n')
file_queries_output = open('file_queries_output.txt','a')
headers = {
    'accept': "application/vnd.linkedin.normalized+json",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "bcookie=\"v=2&d317d340-a9ac-4092-87a1-417fdbd2374a\"; SID=a1a68976-9e88-444b-85bb-653dd188c511; VID=V_2017_05_12_13_988; __utma=226841088.421627762.1494621445.1494622131.1494622131.1; __utmc=226841088; __utmz=226841088.1494622131.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); join_wall=v=2&AQEdFu8uEDQb5AAAAVv-bGEdIHMxa6RVSJchM41qDIyyH7j9359dVjbbmb0zXt4h-FWXtfdbYMN1Onucc2bTORLC_TaG1sWlaA1qRxTkGOk_lyH6f1nwvYLP4M6uASn72thfkK_7wKFB-5IllLV_zbj6JJOBzgvO3TRrU3Tbukv0Es8-pt810fIP; _gid=GA1.2.1467234368.1494622168; visit=\"v=1&M\"; ELOQUA=GUID=71FCF295D13B445AAEE24EDB9E32E4B2; _cb_ls=1; _chartbeat2=D0udO2DKiV87CoIgID.1493737937723.1494624305653.100000000011; PLAY_SESSION=efa9e1da5f821e7dc407437b5cec3c04157b7c45-profinderFlowId=J561BXz3R9aR94nMt-hIIg%3D%3D; _bizo_bzid=3c7171c0-734c-41ce-a0b7-dc211fdc9468; _bizo_cksm=6FF629091DC5DB50; _bizo_np_stats=155%3D344%2C; bscookie=\"v=1&20170513001734443eda5f-3645-43af-801f-876a43437dcfAQE5iq7vKtIWXnrazjxiaPB0bBnInULq\"; sl=\"v=1&b7zMV\"; li_at=AQEDAQdhrlYCNpiTAAABXABYSq0AAAFcAg--rVEAHif6hZAnrr8ESveQYWOTEQYvtkJXPxxo02hRMgBOfiZkzt3hFfaUUK3jeipPntzhHEr9citmuoW1LY-xM3N7aNPTIhmxH0ThDBU_Yxh2YauyIiNR; liap=true; JSESSIONID=\"ajax:8557900745652950925\"; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4MDQ5MDgwOSUzQSUzQTgzMjQ4MzA5O2U8pEHplu8ngdyCn37OBDE-oyo; lang=\"v=2&lang=en-us\"; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; _ga=GA1.2.421627762.1494621445; lidc=\"b=SB34:g=8:u=102:i=1494671301:t=1494717472:s=AQEzAm8G483hPet9lHYtdqo_vuee2cgB\"; _lipt=CwEAAAFcAWP-i1mqXH9SI2nEHl3-mzpdDJuIYTX4YD5xXO0gbbLi5j04kr_gAc1gFJwjmPCasO1veUyc-MO5zT_S34a5EzXBMhqgj5hrkl5vlXgIClS5vyw9TeVHrKy3Y3YSYj82mvarFZI1nbDX2NOBFo7L1eXyMg0QRKwptXt1-860QI-XB1JFQEAbR2F5KLezIjthVLJ-OEd7cVlMyNak6DYI5efNRktx6Fh25tvpDB3fa8_3WzaKOoikDdcpKWyAObi6C7CEsZjhga3dg3swMyhmSbDewew2MOrgVKMHyINWXO96Deq6BiS-6q7OgtF3nDmbjXOrkg4V6eAKygncWf9z1YXvVt6e3qoO-_koLMoEsHT5UTjh9V2BgAA0ruWsOpzwD3xMToQw5758nXGrAGx3ux2TfGkMofAVLR9aQIZrWkk9YUbi7zCwOWnKUvO4Rg",
    'csrf-token': "ajax:8557900745652950925",
    'referer': "https://www.linkedin.com/",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'x-li-lang': "en_US",
    'x-li-page-instance': "urn:li:page:d_flagship3_search_srp_people;+WK//s8zTkKKEM/gYGUkQA==",
    'x-li-track': "{\"clientVersion\":\"1.0.*\",\"osName\":\"web\",\"timezoneOffset\":5.5,\"deviceFormFactor\":\"DESKTOP\"}",
    'x-requested-with': "XMLHttpRequest",
    'x-restli-protocol-version': "2.0.0",
    'cache-control': "no-cache"
    }
for query in file_queries:
    #urllib.quote('(Title: "CEO" at "Morrell Professional Consulting")', safe='')
    response = requests.request("GET", "https://www.linkedin.com/voyager/api/search/cluster?count=10&guides=List(v-%3EPEOPLE)&origin=GLOBAL_SEARCH_HEADER&q=guided&keywords="+urllib.quote(query, safe=''), headers=headers)
    print response.text
    
    
    print str(file_queries.index(query))+'\t'+str(len(response.json()['included']))
    for item in response.json()['included']:
        try:
            if 'urn:li:fs_memberBadges:' in item ['entityUrn']:
                file_queries_output.write(item ['entityUrn'].replace('urn:li:fs_memberBadges:','')+'\n')
        except Exception,e:
            pass
    file_queries_output.flush()
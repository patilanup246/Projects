'''
Created on 27-Nov-2017

@author: Administrator
'''
import requests
headers = {'cookie': 'bcookie=\"v=2&bf5d593b-f4b0-4064-8f8b-a642adfe883f\"; bscookie=\"v=1&20170917100954452ef775-63a0-4ebc-8052-5a8d083da439AQFaboY9Dt1grq_eU9krgpUgIfw8Zueg\"; visit=\"v=1&M\"; _ga=GA1.2.1857355097.1507901499; JSESSIONID=\"ajax:3842491371537359757\"; lang=\"v=2&lang=en-us\"; lidc=\"b=SB92:g=55:u=289:i=1511791260:t=1511852026:s=AQGlb7N9L05W3DckHWgtZCNL7BfTscaF\"; sl=\"v=1&omnRu\"; li_at=AQEDAQXQY1AEkBHDAAABX_3H8HkAAAFgIdR0eVEAjeMNSHkJ79y7RIneeKw8H-xelRml6prXXWF6QdXzX52sf0NM-akfpavI4I4vxKh3gXpoRQo04j6cMyeAhfiQbjUiXirbp13xZ0cO8K-zV3d2E_om; liap=true; sdsc=22%3A1%2C1511791271883%7ECAOR%2C0sDdJAy9scgBVn0I%2BDu4T0ekIoD0%3D; li_a=AQJ2PTEmc2FsZXNfY2lkPTMyNTM3MTUwOSUzQSUzQTg1OTA4NDA5ixz5i8aBIsKQGVDYZG-gp8n5NOc'}
url = "https://www.linkedin.com/sales/search/results/companies"
output_f =  open('output_f','w')
locs = ['tx','ny','il','fl','ca']
for l in locs:

    keywords =  requests.get('https://www.linkedin.com/sales/search/ta/locations?query='+l, headers=headers).json()
    for k in keywords:
        querystring = querystring = {"":"","geoScope":"BY_REGION","facet":["CCR","I","CS"],"facet.CCR":k['id'],"facet.I":"80","facet.CS":["C","D"],"REV":"USD","count":"1000","start":"0"}
        
        
        
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        print (l+'\t'+k['id'] + '-- '+ str(len(response.json()['searchResults'])))
        for j in response.json()['searchResults']:
            location = ''
            try:
                location = j['location']
            except Exception as e:
                #print e
                pass
            try:
                output_f.write (str(j['companyId'])+'\t'+
                            str(j['name'])+'\t'+
                            str(location)+'\t'+
                            str(j['size'])+ '\t'+k['id']+'\n')
                output_f.flush()
            except Exception as e:
                print (e)
                pass
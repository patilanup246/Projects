'''
Created on 04-Dec-2017

@author: Administrator
'''
import requests

url = "https://www.linkedin.com/sales/search/results/companies"
locations = ['ak']
output_f = open('linkedin_by_state_output','w',encoding='utf-8')
for l in locations:
    #["C","D","E","F","G","H","I"]
    querystring = {"geoScope":"BY_REGION","facet":["CCR","I","CS"],"facet.CCR":"us:{}".format(l),"facet.I":"80","facet.CS":["C"],"REV":"USD","count":"1000","start":"0"}
    
    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'cookie': "bcookie=\"v=2&d645143d-3695-4f65-86e3-6886744ba025\"; bscookie=\"v=1&20171130153556624b5296-29a8-4229-8f36-772f6078772fAQHMZyLmLgcMJLwZaen6QCk56AKHqxbS\"; visit=\"v=1&M\"; _ga=GA1.2.1366213987.1512058776; lang=\"v=2&lang=en-us\"; JSESSIONID=\"ajax:6275721117727319136\"; sl=\"v=1&knepZ\"; liap=true; li_at=AQEDAQXQY1ABnt48AAABYBx8dccAAAFgQIj5x1YANODrqfxw_ZyfmeS96XgW9P3mdcUSb0u3oKbyl2EGTuz84UQ-_wrs85desW8yx2-WiZ1hTH7aDnWpOzQCBh_S5lJo9WvUzXrC839rW9WNSTsfrPg3; lidc=\"b=SB92:g=56:u=295:i=1512394348:t=1512476935:s=AQFm0tnb9YwtoF0FLc0A_hKJsk9rLKKc\"; _lipt=CwEAAAFgIbpcGxhlvVOjHwMjg0PN1_KbyDjGVtmxzm8Y5CgMCSwdqvQXjGt3l_9biEF_qknPPbZOLVJbEVGm4KD2eMSnL3h3lPbcbSbwvnJ6mlUUe4DopQmIjkGZriWqXkprEaerWHwQeICmHypeiH89BzZJYWGwSl2hrm_ZEBzTSydJHu6bflt0FFex2KcArRnkZjnhBFiMS6xxt2xf1M6psg8DWbQoCjlAYrP6RDOaTFk4XfopsKpIGztpVKsxOc1VigGocpMjNurTgXhOt9WnJEXNeXJEtCeGLNzC4S88vpRAI4rIgcprtOrMc9bjaVbI6CW88gnplTDLXX9yVUFy6u50JM9drOm8qToQSnhBKcS6lcRhiMvcz4OtyVNjhELuQYcKG9vmNgrmDfyKv13tVpmOa44J-l4hP0n7zew_hOgzmNMGbSeFySSURHN3_qU4bGWM3xRuWD5OoT-2vJJCiQFlLNNrSqsKdJNHnzcNfduOcn-ORHRrn0a8OU9zri9l5O4Xx20NiHO3o1yg4KjFFofk; li_a=AQJ2PTEmc2FsZXNfY2lkPTMyNTM3MTUwOSUzQSUzQTg1OTA4NDA5bU8U7nlUzvxInPa0URzp6y-R8J0; sdsc=22%3A1%2C1512394607907%7ECAOR%2C0FBlLE8Me%2Fr9JM%2FscEXCGjLUFlLQ%3D",
        'referer': "https://www.linkedin.com/sales/search/companies?geoScope=BY_REGION&facet=CCR&facet=I&facet=CS&facet.CCR=us%3Atx&facet.I=80&facet.CS=D&REV=USD&count=25&start=25&trackingInfoJson.contextId=0A0473C2BF1AFD1440E9D1C75E2B0000",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.70 Safari/537.36",
        'x-li-identity': "dXJuOmxpOm1lbWJlcjo5NzU0Mjk5Mg",
        'x-requested-with': "XMLHttpRequest"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    
    total_results = response.json()['searchResults']
    print (l + '\t'+str(len(total_results)))
    for j in total_results:
        location = ''
        try:
            location = j['location']
        except Exception as e:
            #print (e)
            pass
        try:
            output_f.write (str(j['companyId'])+'\t'+
                        str(j['name'])+'\t'+
                        str(location)+'\t'+
                        str(j['industry'])+'\t'+
                        str(l)+'\t'+
                        str(j['size'])+'\n')
            output_f.flush()
        except Exception as e:
            print (e)
            pass
            
    
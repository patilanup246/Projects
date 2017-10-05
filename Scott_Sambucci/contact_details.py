'''
Created on May 18, 2017

@author: Mukadam
'''
import requests
from pyquery import PyQuery

url = "http://irce.a2zinc.net/IRCE2017/Public/attendeeDetails.aspx"

querystring = {"from":"p2p","nav":"false","ContactId":"448147"}

headers = {
    'host': "irce.a2zinc.net",
    'connection': "keep-alive",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'x-wap-profile': "http://218.249.47.94/Xianghe/MTK_Phone_KK_UAprofile.xml",
    'user-agent': "Mozilla/5.0 (Linux; Android 4.4.2; Hol-U19 Build/HUAWEIHol-U19) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
    'referer': "http://irce.a2zinc.net/IRCE2017/Public/PeerConnect.aspx?nav=False",
    'accept-encoding': "gzip,deflate",
    'accept-language': "en-US",
    'cookie': "ASP.NET_SessionId=31zusgfvocnhwrb0jebi4cg2; ckAttendee=ECode=ckAttendee&LoginType=1&Email=chelsea@ibeccreative.com&ContactId=477950&ContactPassword=&BadgeID=; _mkto_trk=id:902-CIM-866&token:_mch-a2zinc.net-1495074676412-70900; __utmt=1; __utmt_~1=1; __utma=184420478.611610211.1495074682.1495074682.1495116838.2; __utmb=184420478.2.10.1495116838; __utmc=184420478; __utmz=184420478.1495074682.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    'x-requested-with': "a2z.Mobile.Event3582",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


#print(response.text)
pq = PyQuery(response.text)
#print pq('strong')


headers = {
    'host': "irce.a2zinc.net",
    'connection': "keep-alive",
    'content-length': "296",
    'origin': "http://irce.a2zinc.net",
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36",
    'content-type': "text/plain",
    'accept': "*/*",
    'referer': "http://irce.a2zinc.net/IRCE2017/Public/PeerConnect.aspx?nav=False",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US",
    'cookie': "ASP.NET_SessionId=bdj1t2u4fhmyna3o21tfdrid; ckAttendee=ECode=ckAttendee&LoginType=1&Email=chelsea@ibeccreative.com&ContactId=477950&ContactPassword=&BadgeID=; _mkto_trk=id:902-CIM-866&token:_mch-a2zinc.net-1495215420484-29093; __utmt=1; __utmt_~1=1; __utma=184420478.596462644.1495215421.1495215421.1495215421.1; __utmb=184420478.2.10.1495215421; __utmc=184420478; __utmz=184420478.1495215421.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    'x-requested-with': "a2z.Mobile.Event3582",
    'cache-control': "no-cache"
    }



file_attendees_details = open('file_attendees_details.txt','w')
for i in xrange(20):
    payload = "ctl00_RadScriptManager1_TSM=&ctl00_RadStyleSheetManager1_TSSM=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=WDG%2FQf4bMMAJPNj%2BlePFYIKYlawAI0CGtDPm0YTDo7vSjhgeab%2BSvE6OwdhoTk0XrjGOuRnVqfTZ8p0JGzcSwUQ3S5XTcX%2BygFX4iUJlt4YV3HTQN48kV%2BvanQYCy4DxzGC20cbWuEBid2mXWUt6wYKpFLTETCPelUGoSSLQdJkLLXHl2xRVeYOLc8GEchO8UB%2F5Vl20KU8DTwuLgtY285bRfAZnYUyLmf8I433IGHqPX1wP6MUWwnTn0cBxAXE0Yaa1IHNN61E80mlObsoqoGRPaZ8%2B2GWxYwP%2Bnu%2F1USVeqctZzfAMC7YyNYlUwP2q3pBlNr3aDhXp%2FbjdvRA9AOXG42n%2BiaFIs9Yvi6CAFHvJNrRx4UWgDPMCYvOf%2BnaFRb1tb6kGEavTlaPxhUVeCuJ%2Bl96Ti2AT53fsiHOUn%2F1STyJL4Zqy3HOR%2BjURTXdsNRFhIzzw4TmxjPGr1pABGHk1goLVPEBcYPZ24z8njCnXYrI84u3bzUimnnZUp5t9AEFLk3tFg9pihz7NUXEm28mh4185LU13gVMuiCPacYKZHvOSH%2FRazkDqaqWbgjrjXeLUIl0sq51ekyV3YElP%2F2WpGCKZsUEeUNq8jBBJrv3Zw3rYy5iV3rVlXB05kdpFeMaQZOCCajDPVT4%2BHfdMDynl%2BBER9OcOE%2FDyQfoSQEMKtOuoCLXu99TEWrtaXbyYUwszkqL7MM4Px50tWKqg6P2hdK3wvy1WKf2oWJx0%2Bnj6%2FNnNYCOxi%2FF6MDQXMxW6stnwzUoB3kTgkjL2BRvg6fc8jM%2FcJW6L8KICPBwLeY%2BS6r8IHCSoAW4wTHGo%2FpDSEGjFjuQDdv4wqMz2SQGuwmmApSabWf%2FtFG019ufgKhjPo1GrCR45tHanFai462kpCSfdcN9r2KPTs7Jd0UsqmR1o1Mm55V3UzJI9zWRpdZnOD%2F3A%2Fucj2WSkKHnwvITgaR%2BDLEp7cfr5xeNjrfLVRY6AJsCjmGt5Y4%2FpLM8xWH8dbvnKGWtoRYvwQShDXI5%2FcxJSuhQ%2BxZn9%2BCEIB2JmPT1CaQ8XDsPHKCSq11avN5Es7s6N99U2zW7b89sny%2BlEG8%2Bq8emmRvD7ub%2FRKTESl%2B1EDdr2nl%2FldxKPUwlmUla5SfJQ2OjnT1k6RE3S09qB0xJVWZsKCmN%2FXSztNd%2BRtAjdfXfGVAcvsA55NmLf74vWXk%2BLBNtdtwpAvmhNnvxU%2FgazRDMiwXD4n7iAb0zFbCI7de%2FiKKHy6uAs3g9uHIEpnwfJ8qDNMb6gQ%2BtM3JZo%2FhDSzDxcaFvYa0iRspwrEExh%2F%2BoymYhxjhADCUkq594wlA8VfjKZnqEyuJo46kYzpIlmBPj7Xr90ObqN7sQ2qFJ%2BRYTcT2JcDJ80Of7vJ1WksNG0E2JiY4%2Fkv6eCxX7oVPClyHlc3WRB5YARSGsi5o7S9i9S%2BmzbILg7NFR2TNk%3D&__VIEWSTATEGENERATOR=63972CAF&nav=False&ctl00%24ContentPlaceHolder1%24hdnAttendeeId=&ctl00%24ContentPlaceHolder1%24hdnIsFavorite=&ctl00%24ContentPlaceHolder1%24hdnAttendeeId2=&ctl00%24ContentPlaceHolder1%24hdnIsFavorite2=&ctl00%24ContentPlaceHolder1%24hdnINProfile=&ctl00%24ContentPlaceHolder1%24hdnINConnections=&ctl00%24ContentPlaceHolder1%24hdnClick=&ctl00%24ContentPlaceHolder1%24hdnMode=&ctl00%24ContentPlaceHolder1%24hdnSortMode=ASC&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnAttendeeId=&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnIsFavorite=&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnAttendeeId2=&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnIsFavorite2=&=&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnMode=search&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnSortMode=ASC&ctl00%24ContentPlaceHolder1%24ctrlAttendeeList%24hdnCustomFieldIDs=&ctl00%24ContentPlaceHolder1%24nnSendMail%24txtMessage=&ctl00%24ContentPlaceHolder1%24nnSendMail%24hdnTask=AtoA&ctl00%24ContentPlaceHolder1%24nnSendMail%24hdnCoId=&ctl00%24ContentPlaceHolder1%24nnSendMail%24hdnBoothId=&ctl00%24ContentPlaceHolder1%24nnSendMail%24hdnContactID=477950&ctl00%24ContentPlaceHolder1%24nnSendMail%24hdnAgentId=605264&__CALLBACKID=ctl00%24ContentPlaceHolder1%24ctrlAttendeeList&__CALLBACKPARAM="+str(i*50)+"\r\n"
    resp = requests.post('http://irce.a2zinc.net/IRCE2017/Public/PeerConnect.aspx?nav=False',data=payload,headers=headers)
    print i
    #print resp.text
    
    pq_attendees = PyQuery(resp.text)
    
    for attendee in pq_attendees('tbody tr'):
        details = ''
        details+= str(attendee.attrib['data-id']) + '\t'
        details+= str(pq_attendees(attendee)('td:eq(3)').text()) + '\t'
        details+= str(pq_attendees(attendee)('td:eq(4)').text()) + '\t'
        details+= str(pq_attendees(attendee)('td:eq(5)').text()) + '\t'
        details+= str(pq_attendees(attendee)('td:eq(6)').text())+'\n'
        
        
        file_attendees_details.write(details) 
        file_attendees_details.flush()
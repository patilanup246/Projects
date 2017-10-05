'''
Created on May 14, 2017

@author: Mukadam
'''
import requests
import urllib,re
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'cookie': "bcookie=\"v=2&be18ad6e-971b-4edc-8e90-8e914bd9c526\"; bscookie=\"v=1&201705131511551ed148b2-48f3-45c6-856d-1c12599e47bbAQG3JyC_xiCuSHRDHAa3a0FdeFcKlu5w\"; visit=\"v=1&M\"; _ga=GA1.2.1591115923.1494688980; sl=\"v=1&yDlCG\"; lang=\"v=2&lang=en-us\"; li_at=AQEDAQdhrlYEvCzvAAABXAUm1tAAAAFcBt5K0FEAYkMzPsAlfQKuhU6sfFYs6SILxNQzMrP-IfhFsNOKnFdy8k1CiVfsBDqXQP4p2_vbEn53VX1ZEsI1qODVS-rEipd3vG2d89kd2e-lzSeb9Ua9ZK-f; liap=true; JSESSIONID=\"ajax:9207225280046802473\"; RT=s=1494735051092&r=https%3A%2F%2Fwww.linkedin.com%2Fuas%2Flogin%3Fsession_redirect%3D%252Fcompany-beta%252F6388780%252F; _lipt=CwEAAAFcBSbqG__nacqT5aj1Ttzb49z_EuqrWSDl6Wx7ufBzJ0bys0ZiGwpDidV9-BGAwZ3sPBBO-yU1PkBiSkqgUW-01SeSynsUk82-IvyMEAUWNO_Gf7lDHzaHstW9OFL9bdxs4WpSzrR3s6SIJmADpmK-giNwM7IBAYG-Cll9PUAGYYz4RmDyRBj1wOU3nAKXoDeHmISWkJAVhW1nuY-5m17VIGkKPdshOdDxlawUFQqkScPDgln7VWgvJ_tB6reVDF19oBS6jyPdRlntvv9Lhp59KQzNisHalnrrWAYoevk9SlwLgkjwCJ8NTrRD7twsZoAkUs6JKbKlo95erJPlwpvUjs8TnKTQFugvnlXCovjW4CCiuXF_D7_LNVajNiY08tOGhJ0DS_3Eonb-lOOrCc4PDFQz0Oa6uA1tGrMGcOhFs_fqOZajIpahzzgb10h_q_GcFzw; lidc=\"b=SB34:g=8:u=102:i=1494735086:t=1494821450:s=AQEcPyeTnVz4IhEdKJBVYIgfKYfIvSYV\"",
    'referer': "https://www.linkedin.com/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded"
    }
file_company_input = open('company_code.txt','r').read().split('\n')
file_company_output = open('company_codes_output.txt','a')


for company in file_company_input:
    response = requests.request("GET", "https://www.linkedin.com/company-beta/"+str(company), headers=headers,verify=False)
    companysite = ''
    #print file_company_input.index(company)
    try:
        companysite = re.findall('companyPageUrl&quot;:&quot;(.*?)&quot;', response.text)[0]
    except Exception,e:
        pass
    
    #file_company_output.write(company+'\t\t'+companysite+'\n')
    file_company_output.flush()

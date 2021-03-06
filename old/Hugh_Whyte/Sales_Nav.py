'''
Created on May 2, 2017

@author: Mukadam
'''
import requests

url = "https://www.linkedin.com/sales/search/results"
file_linkedin =  open('file_linkedin.txt','w')
for i in range(1,690):
    print str(i)
    #querystring = {"EL":"true","facet":"G","facet.G":"gd:0","count":"25","start":str(i*25),"updateHistory":"true","searchHistoryId":"1291824145","trackingInfoJson.contextId":"E2C02E9FB6D3BA1400D4A9C57D2B0000","trackingInfoJson.requestId":"cf45f321-339a-45ef-90b5-c8762d28109f","_":"1493740068517"}
    querystring = {"keywords":"title:(CEO OR Director OR Chairman)","facet":["G","CS"],"facet.G":"au:4910","facet.CS":["C","D","E"],"count":"25","start":str(i*25),"updateHistory":"true","searchHistoryId":"1292578925","trackingInfoJson.contextId":"EA8B14CBA11CBB1480564D0E0B2B0000","trackingInfoJson.requestId":"9367f164-8976-4862-be5f-0cf83263954d","_":"1493819181397"}
    headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "bcookie=\"v=2&3305621b-454a-4b33-87fa-9e84211d0a91\"; bscookie=\"v=1&201702191051039e5509a6-2e5c-4ec5-8393-5355b3b38ebfAQHSoBj6f11H5LmW_aL9-ow_qnlRt2gQ\"; visit=\"v=1&M\"; VID=V_2017_03_27_09_199; SID=1ac57e7a-78aa-4654-965f-49447cd2021e; _cb_ls=1; _chartbeat2=D0udO2DKiV87CoIgID.1493737937723.1493737992090.1; PLAY_SESSION=f56c1ada965178c1f4f6241752329bc80d5badd8-chsInfo=4d1be178-c61d-4a9c-a7b2-0a956559034d+premium_nav_upsell_text; __ssid=d4a461f5-b5af-4bb4-961f-9c4a316bee76; onboarding_session=22dc1865-043f-476a-861d-aef5e46dca17; pushPermState=default; lidc=\"b=OB34:g=218:u=99:i=1493801246:t=1493887645:s=AQEFlTOrApRCWFEXsH-kG26Gv0z1vMCn\"; li_at=AQEDAQdhrlYBPDMhAAABW8m_K6oAAAFbz9OMDVEAa3RVAWqfLyY1jGSXpGwS7xU4rWrAL7AUOhSDTpwUIxoDLd7ONiY7fSqbKfquPTeLQKK8gzSxTtIgKxcwIIkvUl1z-d0E7nWo3chIOgTQ9lS55787; liap=true; sl=\"v=1&8x0cN\"; JSESSIONID=\"ajax:4848616662945522541\"; _ga=GA1.2.501110755.1487515805; _gat=1; _lipt=CwEAAAFbzosZaRNiAOH6_w3MwHcKqguF5knQpekNsJHDnVRTPdcyb3Pf4B9tIg7z2OR_I_FkLJpzYNDaoqyL2PsCSal-idLQuC-PpoJexSUAiD-gRl-UP62EvIQH15jlmY92QpZdIxuhiFwoohbuCPzaRQavqrgnhXJnYB-jkZxtZt_4Dqm2-aUFDK9LvFBrQKgL53pT_ewWuquUAdDXyoHwpFSNEQP-xO3lwIZ9mmZdr79KrYGaJr3BWHBhIksmtpBwFOhIZLyjH2oR9C7WmqThCLj9lBFqsrwv_5sND5yzzA0_rA1MAXHXeicXwZnvlPQFsUwqmz0La66xJe2PCzfMdP-v9T4U86zW-zSMdQuKACE5HigLNgi3ImOXzkm2dQVXolGtu6DOh6m2iq-_78Njzdev0Cqvkg; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4MDQ5MDgwOSUzQSUzQTgzMjQ4MzA5OSa8_E4qbD1xc4QW8_HClBTGzmo; RT=s=1493819181266&r=https%3A%2F%2Fwww.linkedin.com%2Fsales%3Ftrk%3Dd_flagship3_nav; lang=\"v=2&lang=en-us\"; sdsc=22%3A1%2C1493819180088%7ECAOR%2C0pv64%2Fhfi7U61AP39coVUQhj1sEY%3D",
    'referer': "https://www.linkedin.com/sales/search?keywords=title%3A(CEO%20OR%20Director%20OR%20Chairman)&facet=G&facet=CS&facet.G=au%3A4910&facet.CS=C&facet.CS=D&facet.CS=E&count=25&start=25&updateHistory=true&searchHistoryId=1292578925&trackingInfoJson.contextId=EA8B14CBA11CBB1480564D0E0B2B0000",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #print(response.json())

    for item in response.json()['searchResults']:
        memberId = ''
        formattedName = ''
        title = ''
        companyId = ''
        companyName = ''
        try:
            memberId = str(item['member']['memberId'])
        except Exception,e:
            print e
            
        try:
            formattedName = str(item['member']['formattedName'].encode('ascii','ignore'))
        except Exception,e:
            print e
            
        try:
            title = str(item['member']['title'].encode('ascii','ignore'))
        except Exception,e:
            print e
            
        try:
            companyId = str(item['company']['companyId'])
        except Exception,e:
            print e
            
        try:
            companyName = str(item['company']['companyName'].encode('ascii','ignore'))
        except Exception,e:
            print e
            
        file_linkedin.write(memberId +'\t'+ formattedName +'\t'+ title +'\t'+ companyId +'\t'+ companyName+'\n')
    file_linkedin.flush()
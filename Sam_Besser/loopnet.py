import requests
from pyquery import PyQuery

headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    #'Connection': "keep-alive",
    'Host': "www.loopnet.com",
    'Pragma': "no-cache",
    'Referer': "http://www.loopnet.com/zip/10001-commercial-real-estate/2",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
f_o = open('f_o.txt','w')
f_r = open('l.1.txt').read().split('\n')

for i in f_r:
    print (i)
    m = 1
    while True:
        if m==1:
            x = str('http://www.loopnet.com/zip/'+str(i)+'-commercial-real-estate')
            ri = requests.get(x,headers=headers).text
        else:
            x = str('http://www.loopnet.com/zip/'+str(i)+'-commercial-real-estate'+'/'+str(m)+'/')
            ri = requests.get(x,headers=headers).text
        pi = PyQuery(ri)
        
        print (x)
       
        
        for p in pi('[class="listingDescription"] a'):
            #print (p.attrib['href'])
            f_o.write(i+'--'+p.attrib['href']+'\n')
            f_o.flush()
            
        if len(pi('[class="listingDescription"] a')) < 25:
            break
        
        m+=1
        
        
        
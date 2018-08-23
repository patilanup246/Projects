'''
Created on 20-Dec-2017

@author: Administrator
'''


import requests
from pyquery import PyQuery

course_url = ['https://www.lynda.com/Java-tutorials/Java-8-Essential-Training-2015/377484-2.html']
output_file = open('java_essential_training.txt','w')
for course in course_url:
    
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': 'bcookie=2589afd718db4e62b8853e35ef7dfb0cb793f0ae8bcc4e05bb287e5f0ce226af; throttle-d3ebbd09ec7ecff8c4948ff79599614d=1; throttle-ad15fee1459e8f3e1ae3d8d711f77883=1; throttle-20fc2dfb0a81016faeebb960e94da216=1; _ga=GA1.2.672596481.1519637527; throttle-2caceb48e6d82cc19e5e874884531c1a=1; throttle-183f723d6b3764cfa0c5047aa03d3e13=1; throttle-f5a490e5b1060189d91af607a6222fb8=1; throttle-47481a8f590db61e7b4703e070ade640=1; throttle-54c678a5add39d58a7d7411cae569603=1; show-member-tour-cta=true; throttle-a64030d4f0078f1211744e69b24c818f=1; throttle-6d224299407bfb31a5838d5586143992=1; throttle-a08346b1d77e5ed99edf7159d1d154d9=1; __utma=203495949.672596481.1519637527.1519649441.1519701623.2; __utmz=203495949.1519701623.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); SSOLogin=OrgUrl=https%3A%2F%2Fshib.lynda.com%2FShibboleth.sso%2FInCommon%3FproviderId%3Dhttps%3A%2F%2Fidentity.sas.com%2Fadfs%2Fservices%2Ftrust%26target%3Dhttps%3A%2F%2Fshib.lynda.com%2FInCommon&OrgName=SAS%20Institute; throttle-2b03d60a3a4380742663b5f4066e4d2a=1; throttle-81caf7c4bbc10c18b29b105cfcbcdbee=1; throttle-b8b1cb3ef236f57532c515db9614be44=1; tcookie=e81994a5-da1f-4111-b471-5639bbd23db4; __utmv=203495949.|1=Persona=Enterprise-User-Status-Active-Type-Regular=1^3=Product=lyndaEnterprise=1; throttle-9ecc4e578ac856334c0a44bd43f10619=1; throttle-85975e5888b0a2a3d27c273fd5637879=1; throttle-fcc41b5952df7ea0746eff3c71b72bc7=1; throttle-bf01e020137cb85eaa7a5e6a2f331834=1; throttle-cc6e24142c9b2f691b86349a86409bdb=1; throttle-7566ffb605d4cb8c15225d8859a6efd3=1; throttle-7c763a81963c33faaf1d7f75336c624b=0; throttle-04a9b84ec6efb7db03729148c22d02e5=0; throttle-cccbee7c260435d4b14cadf05af4bcf1=0; player_settings_0_2=player_type=2&video_format=1&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=0&reset_on_plugins=True; litrk-srcveh=srcValue=direct/none&vehValue=direct/none&prevSrc=&prevVeh=; throttle-9620ede73ab0b3b8d0fe1e62763ad939=1; player_settings_2972742_2=player_type=2&video_format=1&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=540; throttle-3c6decaab331b0e589231f32fc4b9a84=1; throttle-a5ca6acbd2f547f2914c0b113231bee3=1; throttle-cb8048294d8a62ec98a5d38754e4a964=1; ncp=1; player=%7B%22volume%22%3A1%2C%22muted%22%3Afalse%2C%22theaterMode%22%3Atrue%7D; NSC_tw5_xxx-iuuq_wt=ffffffff096e9e2f45525d5f4f58455e445a4a423660; NSC_tw5_xxx-iuuqt_wt=ffffffff096e9e2745525d5f4f58455e445a4a423661; _gid=GA1.2.904517675.1528327569; token=21f5a5ff-c63a-4c8d-a78d-c3b6e35b02f3,76f54c5d03affebb08cfaf9af686389f,oVcUx2NIIA4NeSrFkJf/6UeBr/iJ7YMGi3IAdaPvaze5BoWkgK0sG74fYw+nlVUHZ7b90Jc8LXRcaQ09WamZKEAeYuBpLAh0b/ByaQpt0P1/jK0tQ4uqCIJ6sXCZ3UklaJ7z4a8eMz7fdO4fyf/DYg==; LyndaAccess=LyndaAccess=6/6/2018 4:27:07 PM&p=0&data=9,7/26/2020,1,94434; LyndaLoginStatus=Member-Logged-In; recentSearches=%5B%7B%22Name%22%3A%22%5Cn%5Ct%5Ct%5Ct%5Ct%5Cn%5Ct%5Ct%5Ct%5Ctlearning%20java%5Cn%5Ct%5Ct%5Ct%22%7D%2C%7B%22Name%22%3A%22revit%202017%22%7D%2C%7B%22Name%22%3A%22%5Cn%5Ct%5Ct%5Ct%5Ct%5Cn%5Ct%5Ct%5Ct%5Ctrevit%202018%3A%20essential%20training%20for%20structure%5Cn%5Ct%5Ct%5Ct%22%7D%5D; utag_main=v_id:0161d1747629009b2db81698ecc004073001c06b00b08$_sn:9$_ss:0$_st:1528329550601$_pn:4%3Bexp-session$ses_id:1528327569015%3Bexp-session; _gat=1',
        'Host': "www.lynda.com",
        'Pragma': "no-cache",
        'Referer': "https://www.lynda.com/Java-tutorials/Welcome/669544/715909-4.html",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.24 Safari/537.36"
        }
    
    resp = requests.get(course, headers=headers)
    pq = PyQuery(resp.text)
    for a in pq('.item-name'):
        try:
            print (a.attrib['href']+'---'+a.text.strip())
        
            r = requests.get(a.attrib['href'], headers=headers).text
        
            pqv = PyQuery(r)
            print (pqv('[class="player"][data-quality]').attr('data-src'))
            output_file.write (course+'\t'+pqv('[class="player"][data-quality]').attr('data-src')+'\t'+a.text.strip()+'\n')
            output_file.flush()
        except Exception as e:
            print (e)
    #     rv = requests.get(pqv('[class="player"][data-quality]').attr('data-src'))
    #     with open(a.text.strip()+'.mp4', "wb") as code:
    #         code.write(rv.content)
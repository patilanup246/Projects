'''
Created on 20-Dec-2017

@author: Administrator
'''


import requests
from pyquery import PyQuery

course_url = ['https://www.lynda.com/SketchUp-tutorials/SketchUp-Rendering-Using-Twilight-2017/630602-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Tips-Tricks/580640-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Rendering-V-Ray-3/599605-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Set-Design/604228-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Revit-Workflow/590825-2.html',
              'https://www.lynda.com/CAD-tutorials/SketchUp-Bathroom-Remodel/599604-2.html',
              'https://www.lynda.com/SketchUp-tutorials/V-Ray-Control-Color-Bleed-SketchUp/490758-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Modeling-from-Photos/450189-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Ultimate-Man-Cave-She-Shed-Design/450188-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-2017-Essential-Training/494108-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Kitchen-Design/449642-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Architecture-Details/160268-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Rendering-Using-V-Ray-2/162706-2.html',
              'https://www.lynda.com/SketchUp-tutorials/Designing-Tiny-House-SketchUp/382571-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Architecture-LayOut/160269-2.html',
              'https://www.lynda.com/SketchUp-tutorials/3D-Modeling-Printing-Household-Parts/371693-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Architecture-Fundamentals/145425-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Interior-Design/166508-2.html',
              'https://www.lynda.com/SketchUp-tutorials/SketchUp-Pro-Tools-Techniques/151486-2.html',
              ]
output_file = open('output.txt','w')
for course in course_url:
    
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': "bcookie=bcdd83a32e0a4c489aad7e7d97d4c8a0917c9962cee84022b2d54fefbac5a636; player_settings_0_2=player_type=2&video_format=1&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=0&reset_on_plugins=True; litrk-srcveh=srcValue=direct/none&vehValue=direct/none&prevSrc=&prevVeh=; throttle-d3ebbd09ec7ecff8c4948ff79599614d=1; throttle-ad15fee1459e8f3e1ae3d8d711f77883=1; throttle-20fc2dfb0a81016faeebb960e94da216=1; _ga=GA1.2.894137091.1512099748; SSOLogin=OrgUrl=https%3A%2F%2Fshib.lynda.com%2FShibboleth.sso%2FInCommon%3FproviderId%3Dhttps%3A%2F%2Fidentity.sas.com%2Fadfs%2Fservices%2Ftrust%26target%3Dhttps%3A%2F%2Fshib.lynda.com%2FInCommon&OrgName=SAS%20Institute; throttle-2b03d60a3a4380742663b5f4066e4d2a=1; player_settings_2972742_2=player_type=2&video_format=1&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=540; throttle-81caf7c4bbc10c18b29b105cfcbcdbee=1; throttle-b8b1cb3ef236f57532c515db9614be44=1; tcookie=8270a5ee-ff9b-4dc3-8f91-009d8c4c910d; throttle-a5ca6acbd2f547f2914c0b113231bee3=1; throttle-47481a8f590db61e7b4703e070ade640=1; throttle-54c678a5add39d58a7d7411cae569603=1; throttle-9ecc4e578ac856334c0a44bd43f10619=1; throttle-85975e5888b0a2a3d27c273fd5637879=1; throttle-fcc41b5952df7ea0746eff3c71b72bc7=1; throttle-bf01e020137cb85eaa7a5e6a2f331834=1; throttle-cc6e24142c9b2f691b86349a86409bdb=1; throttle-e0cb8e4541d2401ae2437d4836b8d8cd=1; _gid=GA1.2.1511772677.1513770187; LyndaAccess=LyndaAccess=12/20/2017 3:43:26 AM&p=0&data=9,7/26/2020,1,94434; LyndaLoginStatus=Member-Logged-In; ncp=1; plugin_list=; __utma=203495949.894137091.1512099748.1513776486.1513776486.1; __utmz=203495949.1513776486.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=203495949; __utmv=203495949.|1=Persona=Enterprise-User-Status-Active-Type-Regular=1^3=Product=lyndaEnterprise=1; recentSearches=%5B%7B%22Name%22%3A%22sketchup%22%7D%2C%7B%22Name%22%3A%22%5Cn%5Ct%5Ct%5Ct%5Ct%5Cn%5Ct%5Ct%5Ct%5Ctinterior%20design%5Cn%5Ct%5Ct%5Ct%22%2C%22Type%22%3A4%7D%2C%7B%22Name%22%3A%223d%20animation%22%7D%5D; utag_main=v_id:0160102b133d0019fe15424114bd04071001606900b08$_sn:11$_ss:0$_st:1513778334300$_pn:8%3Bexp-session$ses_id:1513776477335%3Bexp-session; NSC_tw5_xxx-iuuqt_wt=ffffffff096e9e2345525d5f4f58455e445a4a423661; player=%7B%22volume%22%3A1%2C%22muted%22%3Afalse%2C%22quality%22%3A720%7D; token=af0f1af8-7eb6-4da0-b924-60fc75dc9d71,a4e7bb7bf58c8add8dbea34915afade4,oVcUx2NIIA4NeSrFkJf/6UeBr/iJ7YMGi3IAdaPvaze5BoWkgK0sG74fYw+nlVUHL7Z8r5kcVDbYNFf/Un/8p+neWlPWBOeB95sscLzNFqqTllB3NYC7QYUQlWoYGAPkghj7Y4pGRErneD6RvRftkA==; _gat=1",
        'Host': "www.lynda.com",
        'Pragma': "no-cache",
        'Referer': "https://www.lynda.com/SketchUp-training-tutorials/953-0.html",
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
            output_file.write (course+'\t'+pqv('[class="player"][data-quality]').attr('data-src')+'\t'+a.text.strip()+'\n')
            output_file.flush()
        except Exception as e:
            print (e)
    #     rv = requests.get(pqv('[class="player"][data-quality]').attr('data-src'))
    #     with open(a.text.strip()+'.mp4', "wb") as code:
    #         code.write(rv.content)
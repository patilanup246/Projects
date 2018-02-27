'''
Created on Feb 24, 2018

@author: talib
'''
# Import the required module for text 
# to speech conversion
# 
# import os
# mytext = 'You have received new invitations'
# language = 'en'
# myobj = gTTS(text=mytext, lang=language, slow=True)
# myobj.save("welcome.mp3")
# from gtts import gTTS
import requests
import playsound    
import time
url = "https://www.upwork.com/freelancers/api/v1/profile/me/fwh"

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'cookie': "device_view=full; _vhipo=0; visitor_id=103.207.10.146.151849481455908; optimizelyEndUserId=oeu1518543424626r0.7754595129734481; _ga=GA1.2.1012108701.1518543425; _pxvid=5c78e370-1073-11e8-bbff-a1d4849b058f; __troRUID=5c11816c-ab7d-42d4-976b-583da816c6d5; recognized=1; last_accessed_app=dash; _mkto_trk=id:518-RKL-392&token:_mch-upwork.com-1518548417350-46855; ki_r=; __ssid=606c17e2-a4a1-4ebf-8114-18e56ff876ba; dash_company_last_accessed=705290620522987521; _gid=GA1.2.415716950.1518969682; acced10826077=11127579; sp=b2ef19ad-5590-471a-8ccb-5043bf399348; __zlcmid=l5h8g5z5n0OrHz; acce4871455=20010885; ki_t=1518548421376%3B1519225250132%3B1519225250132%3B2%3B2; DA[rangwala_tasneem]=6a2bebac623755b42732793f1d449fdb%2C0%2Cv8%2C1527007960; mp_b36aa4f2a42867e23d8f9907ea741d91_mixpanel=%7B%22distinct_id%22%3A%20%22f7431cc9-b9f6-4dc6-91c9-1ada50dca983%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.in%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.in%22%7D; acced11070041=11377428; qt_visitor_id=49.202.56.431456989363959580; company_last_accessed=d10826077; current_organization_uid=705290620522987521; mp_mixpanel__c=55; __cfduid=d17742b92905b5047834ff4eb7924cd7d1519465964; _br_uid_2=uid%3D9457956618889%3Av%3D11.8%3Ats%3D1518543429639%3Ahc%3D18; __trossion=1518543430_1800_6_5c11816c-ab7d-42d4-976b-583da816c6d5%3A1519369081_5c11816c-ab7d-42d4-976b-583da816c6d5%3A1519465968_1519465968_1; __troSYNC=1; trctestcookie=ok; console_user=rangwala_tasneem; session_id=8eab8b2caa24079b042ceb0acb99d4c0; master_access_token=01471091.oauth2v1_d54cad78454a4faeafce646b1ce62d1d; oauth2_global_js_token=oauth2v1_169f7406fa91466b8061be341a0597f8; dash_access_token=oauth2v1_09faacd25d32efb8f8d1d4cfa5743c8c; XSRF-TOKEN=d16d74bf5efd4353ee16a0b4bdd3ac19; mp_fdf88b8da1749bafc5f24aee259f5aa4_mixpanel=%7B%22distinct_id%22%3A%20%22161905d906cb3b-06b4fc8ece89d5-d35346d-1d4c00-161905d906e2b4%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.in%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.in%22%7D; _px3=50c5c5dffb837e133c3feac5be9160207c6899b1f2bffb70a166acb458f1c7ed:nKXhuhwa+rCpQZFUpsKQ1SjQ6f7L1uzRFj3dKfpiPJZhw/UPxePHxVZaMbNabtd49xPT0oY4UTkpxw2rv/zorQ==:1000:cOurNjlvmtORdTUHCTLhOahaxVblG+sjP/XrQqnmu/5zxHOrlbygvu8aawvUf36xvqnazOhqvl3eT0e3OtOgLbp7DZ0zl/2nJPn/uQ6ef5jcUqa3lRUyT2SInh4/BPDMuIqUFCBVxnuiCXkfaNmvkgHcFJnzULEi+FiIXizMt98=",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }

while True:
    response = requests.request("GET", url,headers=headers)
    
    print(response.json()['interviews'])
    
    if response.json()['interviews']:
        playsound.playsound('welcome.mp3', True)
        time.sleep(3)
        playsound.playsound('welcome.mp3', True)
        time.sleep(3)
        playsound.playsound('welcome.mp3', True)
        
    time.sleep(60)

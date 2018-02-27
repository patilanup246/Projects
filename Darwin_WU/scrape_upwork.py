'''
Created on Feb 13, 2018

@author: talib
'''
import requests, csv
from pyquery import PyQuery
import time
output_f = open('upwork_output.csv','w',encoding='utf-8')

 
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'cookie': "device_view=full; _vhipo=0; visitor_id=103.207.10.146.151849481455908; __cfduid=d661f278212befe1f7766112ed9b15d9f1518494815; optimizelyEndUserId=oeu1518543424626r0.7754595129734481; _ga=GA1.2.1012108701.1518543425; _gid=GA1.2.1517393309.1518543425; _pxvid=5c78e370-1073-11e8-bbff-a1d4849b058f; __trossion=1518543430_1800_1__5c11816c-ab7d-42d4-976b-583da816c6d5%3A1518543430_1518543430_1; __troRUID=5c11816c-ab7d-42d4-976b-583da816c6d5; __troSYNC=1; recognized=1; console_user=rangwala_tasneem; qt_visitor_id=49.202.56.431456989363959580; company_last_accessed=d10826077; current_organization_uid=705290620522987521; last_accessed_app=dash; session_id=ae9bd50a855b788144f2d8e92f762978; XSRF-TOKEN=f52ea2372347fb8146f195099d567336; _gat_UA-62227314-1=1; _br_uid_2=uid%3D9457956618889%3Av%3D11.8%3Ats%3D1518543429639%3Ahc%3D2; mp_fdf88b8da1749bafc5f24aee259f5aa4_mixpanel=%7B%22distinct_id%22%3A%20%22161905d906cb3b-06b4fc8ece89d5-d35346d-1d4c00-161905d906e2b4%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.in%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.in%22%7D; _px3=8d3ddb67b0a657561aec9881aa108acd4852ec3fa0e0b5e1ac8e58b668bc9d01:yRnxeZD6gqQiT+fIMz3HEGlih6kjCjsCVtjJbjbEODHz8UxpzuAH+IoxwFdPO8+krWTfjOG0zMhImwNxQcUV9w==:1000:0hooRPsyEY/LkBEH+qk45Ux/M1nnJbW82cPvsvhwSngkwB7HI+EYrbv4SKNfjGlDZIDTEYleOo4FPMcnk81Z6E4UP3gHoPotNVxvJYPtbx/hmuGx8QBUxgQCRt1tDh6lcCeixE4H2ouaEeD9M1rOAXCU/B9MlOjfjpsX9VnhXG4=",
    'referer': "https://www.google.co.in/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }
for u in open('scrape_upwork_input.txt').read().split('\n'):
    try:
        u = u.split(' ',1)
    
        output_f.write (u[0]+'\t'+u[1]+'\n')
    except:
        output_f.write (''+'\n')
    
    
# -*- coding: utf-8 -*-
'''
Created on 21-Jan-2018

@author: Administrator
'''
import requests, csv, os
from pyquery import PyQuery
from selenium import webdriver
from glob import glob
o_f = open('filecams.txt','w')
import requests

url = "https://www.camsonline.com/DistributorServices/COL_DisQueryform.aspx"

payload = "__VIEWSTATE="+open('cams_req.txt').read()+("&__PREVIOUSPAGE=AjTYXXEVAM5zullcd9nGzCCDV2RSOFgp5EWASkk58mYcXwQUhJ-B5mHxvJyywqZzB1gKV8nj6JGphNrf8MHugMRTi3nTPPE6rtWQN3HikmWfCcn8LQb90jKV4CXdoYH-0"
"&qry=WBR2"
"&ctl00%24PageContent%24ddlformat=XLSWH"
"&ctl00%24PageContent%24ddldeliopt=DOWNLINK"
"&ctl00%24PageContent%24btnnext.x=39"
"&ctl00%24PageContent%24btnnext.y=14"
"&ctl00%24PageContent%24hOPF=XLSWH"
"&ctl00%24PageContent%24hemail=redmoneyindore%40gmail.com"
"&ctl00%24PageContent%24hamcs='B'%2C'H'%2C'P'%2C'L'%2C'BG'%2C'D'%2C'O'%2C'G'%2C'IF'%2C'K'%2C'F'%2C'MM'%2C'PP'%2C'RM'%2C'SH'%2C'T'%2C'UK'"
"&ctl00%24PageContent%24hbrktyp=brok"
"&ctl00%24PageContent%24hdeferred=N"
"&ctl00%24PageContent%24hdnQryVal=WBR2"
"&ctl00%24PageContent%24hbsize=Small"
#"&ctl00%24PageContent%24hadminParentPage=https%3A%2F%2Fwww.camsonline.com%2FDistributorServices%2FCOL_Mailbackservice.aspx"
"&ctl00%24PageContent%24hfTotalGSTAmount=0"
"&ctl00%24PageContent%24hRATE=0&ctl00%24PageContent%24hTAX_AMOUNT=0"
"&ctl00%24PageContent%24hDISTRIBUTOR_TAX_RATE=0"
"&ctl00%24PageContent%24hDISTRIBUTOR_TAX_AMOUNT=0")
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Content-Length': "15242",
    'Content-Type': "application/x-www-form-urlencoded",
    'Host': "www.camsonline.com",
    'Origin': "https://www.camsonline.com",
    'Pragma': "no-cache",
    'Referer': "https://www.camsonline.com/DistributorServices/COL_Repselect.aspx",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.100 Safari/537.36"
    }

response = requests.request("POST", url, data=payload, headers=headers)

pq = PyQuery(response.text)

o_f.write (pq('#__VIEWSTATE').attr('value'))
o_f.flush()

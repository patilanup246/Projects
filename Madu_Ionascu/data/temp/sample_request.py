#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 13, 2018

@author: talib
'''

import random
import requests

luminati_port = 24000
profile = 'https://sg.linkedin.com/in/frida-suryadjaya-25101b29'

http_proxy  = "http://127.0.0.1:{}".format(str(luminati_port))
https_proxy = "https://127.0.0.1:{}".format(str(luminati_port))
ftp_proxy   = "ftp://127.0.0.1:{}".format(str(luminati_port))


proxyDict = { 
          "http"  : http_proxy, 
          "https" : https_proxy, 
          "ftp"   : ftp_proxy
        }
headers = {
'x-lpm-session': ''.join(random.choice('ABC123') for i in range(6)),
'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
'accept-encoding': "gzip, deflate, br",
'accept-language': "en-US,en;q=0.9",
'upgrade-insecure-requests': "1",
'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}


response = requests.request("GET", profile , headers=headers, proxies=proxyDict)
print (response.text)

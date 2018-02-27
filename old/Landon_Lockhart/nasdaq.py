#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 05:46:55 2016

@author: landonlockhart
"""
from flask import Flask,render_template

import pandas as pd
import subprocess
from datetime import datetime, timedelta
import requests
from pyquery import PyQuery
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://stockData:xxxxxxxxxxxxx@stockData.c4xqz2oprsex.us-west-2.rds.amazonaws.com:3306/innodb', echo=False)
connection = engine.connect()
symbol_list = connection.execute("SELECT Symbol FROM Full_Stock_List where Symbol in ('AAPL', 'APOG', 'RHT','FDX','ADBE');").fetchall()




web_url = 'http://www.nasdaq.com/earnings/report/'
#columns = {'product': shoes, 'link': links}
#df = pd.DataFrame(columns)


#symbol_list = get_symbol_list()
df_result = pd.DataFrame()
length = len(symbol_list)
ct=1
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "max-age=0",
    'connection': "keep-alive",
    'host': "www.nasdaq.com",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.29 Safari/537.36"
    }
for stock_symbol in symbol_list:
    #print str(stock_symbol[0])+': '+str(ct)+' of '+str(length)
    ct=ct+1
    url = web_url + str(stock_symbol[0]).lower()
    #print url

    try:
        response = requests.request("GET", url, headers=headers).text
        #htmltext = urllib2.urlopen(url)
        pq = PyQuery(response)
        #next_date = soup.find_all('a',attrs={'class':'name-link'})
        
        date_text = pq('#two_column_main_content_reportdata').text().strip()
        beg = date_text.find('/') - 2
        end = beg+10
        anno_date = date_text[beg:end]
        new_anno_date = datetime.strptime(str(anno_date), '%m/%d/%Y')
        d = {'symbol': str(stock_symbol[0]),'nx_anno_date': new_anno_date}
        #print d
        df_result = df_result.append(d, ignore_index = True)
        print (str(stock_symbol[0])+': '+str(ct)+' of '+str(length)+' GOOD')
    except:
        print (str(stock_symbol[0])+': '+str(ct)+' of '+str(length)+' BAD')
        pass
    #print str(stock_symbol[0]) +' '+ anno_date

print (df_result)
df_result.to_sql(name='announcements', con=engine, if_exists = 'append', index=False, chunksize=10000)
connection.close()

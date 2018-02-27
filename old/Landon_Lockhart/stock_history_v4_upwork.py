#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:17:41 2016

@author: landonlockhart
"""
import requests
from pyquery import PyQuery
# main program
from flask import Flask,render_template
#from multi import Multi_Wrap
from yahoo_finance import Share
import numpy  
import pandas as pd  
import sys
from scrapers.options import OptionScraper
import Queue
import threading
import urllib2
import time
#import mechanize
import json
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs
import mechanize
import math
#import numpy as np
#import pandas as pd
#old# import pandas.io.data as web
import pandas_datareader.data as web
import threading
from google import getHistoricalData
module_import = 'import success'    
import os

try:
   # main program
   from flask import Flask,render_template
   #from multi import Multi_Wrap
   from yahoo_finance import Share
   import fix_yahoo_finance as yf
   import numpy  
   import pandas as pd  
   import sys
    
   #from scrapers.options import OptionScraper

   import Queue
   import threading
   import urllib2
   import time
   #import mechanize
   import json
   import time
   from datetime import datetime
   from bs4 import BeautifulSoup as bs
   import mechanize
   #import numpy as np
   #import pandas as pd
   #old# import pandas.io.data as web
   import pandas_datareader.data as web


except Exception,e: 
    module_import = 'import failed'

app = Flask(__name__)

from flaskext.mysql import MySQL
mysql = MySQL()



mysql.init_app(app)

resp_ssl = requests.get('https://www.sslproxies.org',verify=False).text
pq_ssl = PyQuery(resp_ssl)

proxy_list = []
for p in pq_ssl('table tr'):
    proxy_list.append(pq_ssl(p)('td:nth-child(1)').text()+':'+pq_ssl(p)('td:nth-child(2)').text())


proxy_count = 0
def get_new_proxy():
    global proxy_count
    proxy_count =proxy_count + 1
    get_proxy = proxy_list[proxy_count]
    #print get_proxy
    proxyDict = {
        "http": "http://" + get_proxy,
        "https": "https://" + get_proxy
    }
    proxy = get_proxy

    os.environ['http_proxy'] = proxy 
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    #return proxyDict

def stock_history(date):
    #mysql:  one thread per connection https://www.percona.com/blog/2010/10/27/mysql-limitations-part-4-one-thread-per-connection/
    #from flaskext.mysql import MySQL
    #connection = mysql.connect()            
    #cursor = connection.cursor()   
    an_error1=False
    an_error2=False
    start=time.time()        
    connection = mysql.connect()            
    cursor = connection.cursor()  
    from datetime import datetime, timedelta    

    #print today_date    
    c=0
    db_date= str(date)+' 16:05:00'
    cursor.execute("SELECT Symbol FROM Full_Stock_List ;")
    symbol_list = cursor.fetchall()
    symbol_list = [symbol[0] for symbol in symbol_list]
    
    
    symbol_num = 0
    
    for stock_symbol in symbol_list:
        if (symbol_num % 2000) == 0:
            get_new_proxy()
        symbol_num+=1
        c+=1 
        an_error1=False
        an_error2=False
        datetime_object = datetime.strptime(date, '%Y-%m-%d').date()
        date2 = datetime_object + timedelta(days = 1)
        try:
            #ticker_info = yf.download(str(stock_symbol), str(date), str(date2))
            ticker_info = getHistoricalData(stock_symbol, date, date)
            
        except Exception,e:
            print '! '+str(stock_symbol)+' stocks data retrieval problem1: '+str(e)
            an_error1=True
            pass
        
        
        if not an_error1:

            try: 
                #print ticker_info
                stock_open = float(ticker_info['Open'][0])
                stock_high = float(ticker_info['High'][0])
                stock_low = float(ticker_info['Low'][0])
                stock_close = float(ticker_info['Close'][0])
                stock_volume = float(ticker_info['Volume'][0])
                stock_adj_close = 0
                #stock_adj_close = float(ticker_info['Adj Close'][0])

            except Exception,e:
                print '! '+str(stock_symbol)+' stocks data insertion1: '+str(e)
                pass
            
            try:        
                query="INSERT INTO stocks (update_date,"\
                +"stock_symbol,"\
                +"open,"\
                +"high,"\
                +"low,"\
                +"close,"\
                +"volume,"\
                +"adj_close) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"            
                
                args=(db_date,\
                stock_symbol,\
                stock_open,\
                stock_high,\
                stock_low,\
                stock_close,\
                stock_volume,\
                stock_adj_close)   
                
                cursor.execute(query,args)            
                connection.commit() 
                
                print str(stock_symbol)+' stocks OK'
            
            except Exception,e:
                print '! '+str(stock_symbol)+' stocks data insertion2: '+str(e)
                pass
        
        else:

            try:
                query2="INSERT INTO stock_price (update_date,"\
                +"stock_symbol,"\
                +"price) VALUES (%s, %s, %s)"  
            
                args2=(db_date,\
                stock_symbol,\
                price)                                                     
            
                cursor.execute(query2,args2)
                connection.commit()
         
                print str(stock_symbol)+' prices OK'
            except Exception,e:
                print '! '+str(stock_symbol)+' stocks data insertion: '+str(e)
                pass
    return
    
def main(choice):
    #branch=[choice]
    #branch=['']
    #branch+=[choice]
    #symbol_list = ['GE']
    print 'getting stocks for : '+str(choice)        
    stock_history(str(choice))
    return

if __name__ == '__main__':            
    print(sys.argv, len(sys.argv))
    #(['dorun.py', 'a'], 2)

    if len(sys.argv)>1:
        choice=sys.argv[1]
    else:
        choice=""
    print "For choice: "+choice
    main(choice)
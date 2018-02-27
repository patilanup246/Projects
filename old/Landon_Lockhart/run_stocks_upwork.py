#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 08:40:55 2017

@author: landonlockhart
"""

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
from sqlalchemy import create_engine


def run_get_stocks():
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
    today_date = datetime.now().date()
    update_time_database = datetime.now()
    oneday = timedelta(days=1)
    today_date = today_date - oneday
    update_time_database = update_time_database - oneday
    update_time_database = update_time_database.replace(hour=16, minute=5, second=0, microsecond=0)
    symbol_list = get_symbol_list()
    
    #print today_date    
    c=0
    for stock_symbol in symbol_list:
        c+=1 
        an_error1=False  
                  
            daytime = 0
            if t0 > t6:
                update_time_database = t0.replace(hour=17, minute=05, second=0, microsecond=0)
                daytime = 0
            else:
                if t0 > t5:
                    update_time_database = t0.replace(hour=15, minute=45, second=0, microsecond=0)
                    print 'hi t5'
                else:
                    if t0 > t4:
                        update_time_database = t0.replace(hour=13, minute=30, second=0, microsecond=0)
                        print 'hi t4'
                    else:
                        if t0 > t3:
                            update_time_database = t0.replace(hour=11, minute=30, second=0, microsecond=0)
                            print 'hi t3'
                        else:
                            if t0 > t2:
                                update_time_database = t0.replace(hour=9, minute=15, second=0, microsecond=0)
                            else:
                                update_time_database = t0.replace(hour=7, minute=45, second=0, microsecond=0)
                                daytime = 0
                                
            daytime = 0            
            if daytime == 0:
                try:

                    ticker_info = yf.download(str(stock_symbol), str(today_date), str(today_date))
                  
                    stock_open = float(ticker_info['Open'][0])
                    stock_high = float(ticker_info['High'][0])
                    stock_low = float(ticker_info['Low'][0])
                    stock_close = float(ticker_info['Close'][0])
                    stock_volume = float(ticker_info['Volume'][0])
                    stock_adj_close = float(ticker_info['Adj Close'][0])

                except Exception,e:
                    print str(ticker_info)
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
                    
                    args=(update_time_database,\
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
                
                    args2=(update_time_database,\
                    stock_symbol,\
                    price)                                                     
                
                    cursor.execute(query2,args2)
                    connection.commit()
             
                    print str(stock_symbol)+' prices OK'
                except Exception,e:
                    print '! '+str(stock_symbol)+' stocks data insertion: '+str(e)
                    pass
                      
    return
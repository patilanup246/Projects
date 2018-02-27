# -*- coding: utf-8 -*-
'''
Created on 31-Jan-2018

@author: Administrator
'''
import requests, csv, os
from pyquery import PyQuery
from selenium import webdriver
from glob import glob

import sqlite3
 
# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.create_sheet()
#  
#  
# conn = sqlite3.connect('db.db')
# print ("Opened database successfully")
#  
# cursor = conn.execute("SELECT * from file_1 where LOWER(Title) LIKE '% parties %' OR LOWER(Article) LIKE '% parties %' OR LOWER(Title) LIKE '% fpi %' OR LOWER(Article) LIKE '% fpi %' OR LOWER(Title) LIKE '%hizbut tahrir indonesia%' OR LOWER(Article) LIKE '%hizbut tahrir indonesia%' OR LOWER(Title) LIKE '% hti %' OR LOWER(Article) LIKE '% hti %' OR LOWER(Title) LIKE '%islamic defender front%' OR LOWER(Article) LIKE '%islamic defender front%' OR LOWER(Title) LIKE '%nahdlatul ulama%' OR LOWER(Article) LIKE '%nahdlatul ulama%' OR LOWER(Title) LIKE '% nu %' OR LOWER(Article) LIKE '% nu %' OR LOWER(Title) LIKE '% party %' OR LOWER(Article) LIKE '% party %' OR LOWER(Title) LIKE '% political party %' OR LOWER(Article) LIKE '% political party %'")
# row_excel = 1
# for row in cursor:
#     print (row_excel)
#     ws.cell(row=row_excel,column = 1).value = row[0]
#     ws.cell(row=row_excel,column = 2).value = row[1]
#     ws.cell(row=row_excel,column = 3).value = row[2]
#     ws.cell(row=row_excel,column = 4).value = row[3]
#     ws.cell(row=row_excel,column = 5).value = row[4]
#     row_excel+=1
# wb.save('write_only_file.xlsx')
# print ("Operation done successfully")
# conn.close()
o = open('o.txt','w')
for d in open('dates.txt').read().split('\n'):
    o.write (d.split(' ')[-1]+'\n')
    o.flush()
# -*- coding: utf-8 -*-
'''
Created on 11-Jan-2018

@author: Administrator
'''
import requests, csv, os, time
from pyquery import PyQuery
from selenium import webdriver
from glob import glob
import re

#file_input = open('1_Branding Workshop_1_Module 1 What's My Brand.vtt').read()
#vtt_file = open('3_Conclusion_1_The Crucial Dos & Dont- A Roundup.txt','w')







# result = [y for x in os.walk('udemy') for y in glob(os.path.join(x[0], '*.vtt'))]
# for r in result:
#     try:
#         vtt_file = open(r.replace('.vtt','')+'.txt','w',encoding='utf-8')
#         for m in re.findall(r'(?P<text>.*?)\n\n', open(r,encoding='utf-8').read()+'\n\n'):
#             vtt_file.write(m+'\n\n')
# 
#          
#     except Exception as e:
#         print (e)
#         print (r)

    
result = [y for x in os.walk('new_udemy_from_gauthier') for y in glob(os.path.join(x[0], '*.txt'))]
count_fr = 0
count_txt = 0
filepath_count = 0

for r in result:
    if '_FR.txt' in r:
        count_fr+=1
    if 'filepath.txt' in r:
        filepath_count+=1
    if not '_FR.txt' in r and 'filepath.txt' in r:
        count_txt+=1
        
print (count_fr)
print (count_txt)
print (filepath_count)
    
# -*- coding: utf-8 -*-
'''
Created on 06-Jan-2018

@author: Administrator
'''
import requests, csv, os, time
from pyquery import PyQuery
from selenium import webdriver
from glob import glob

#driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')
#driver.get('https://translate.google.com/')


output_f = open('output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow([])
products_url = ''


result = [y for x in os.walk('udemy') for y in glob(os.path.join(x[0], '*.txt'))]
for r in result:
    print (r)
    input1 = open('\\?\'+r).read()
    #driver.find_element_by_id('#source').send_keys(input1)
    print (input1)
    time.sleep(5)
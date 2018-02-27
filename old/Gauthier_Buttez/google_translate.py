# -*- coding: utf-8 -*-
'''
Created on 06-Jan-2018

@author: Administrator
'''
import requests, csv, os, time
from pyquery import PyQuery
from selenium import webdriver
from glob import glob

driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')
driver.get('https://translate.google.com/')
time.sleep(5)

output_f = open('output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow([])
products_url = ''


result = [y for x in os.walk('udemy') for y in glob(os.path.join(x[0], '*.txt'))]
for r in result:
    if not 'filepath.txt' in r:
        if not '_FR.txt' in r:
            print (r)
            input1 = open(r,encoding="utf-8").read()
            time.sleep(1)
            final_string = ''
            #driver.execute_script("document.getElementById('source').value = '{}';".format(input1))
            #print (len(input1))
            for m in range(0,int(len(input1)/5000)+1):
                driver.find_element_by_id('source').clear()
                driver.find_element_by_id('source').send_keys(input1[m*5000:(m+1)*5000])
                driver.execute_script("document.getElementById('gt-submit').click()")
                time.sleep(5)
                final_string+=driver.find_element_by_id('result_box').get_attribute("innerText")
            #driver.find_element_by_id('gt-submit')
    
            
            oo = open(r.replace('.txt','_FR.txt'),'w',encoding='utf-8')
            oo.write(final_string)
            oo.close()
    #print (input1)
    
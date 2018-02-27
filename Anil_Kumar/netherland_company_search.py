# -*- coding: utf-8 -*-
'''
Created on 01-Feb-2018

@author: Administrator
'''
import requests, csv, os, time
from pyquery import PyQuery
from selenium import webdriver
from glob import glob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')

driver.get('https://www.kvk.nl/zoeken/')
#output_f = open('output.csv','w',encoding='utf-8', newline='')

for i in open('company_list.txt',encoding='utf-8').read().split('\n'):
    driver.find_element_by_css_selector('#powerSearchInput').clear()
    driver.find_element_by_css_selector('#powerSearchInput').send_keys(str(i))
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="hoofdvestigingTag"]:nth-of-type(1)')))
        print (str(i)+'\t'+ str(element.get_attribute('href')))
    except:
        print (str(i))
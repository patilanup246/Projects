# -*- coding: utf-8 -*-
'''
Created on 08-Jan-2018

@author: Administrator
'''
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()


output_f = open('output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['SKU','Name','Category','Fitment','Fitment HTMl','URL','Price','Features','Features HTML','Details','Details HTMl','Images'])
products_url = ''
with open('superatv_export.csv', encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if not row[20]:
            print(row[13] + row[20])
            try:
                driver.get(row[13])
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fotorama__thumb img")))
                time.sleep(1)
                print (len(driver.find_elements_by_css_selector('.fotorama__thumb img')))
                images_new = []
                for img in driver.find_elements_by_css_selector('.fotorama__thumb img'):
                    driver.find_element_by_css_selector('.fotorama__arr--next div').click()
                    time.sleep(1)  
                    for a in driver.find_elements_by_css_selector('.fotorama__stage__frame [class="fotorama__img"]'):
                        images_new.append (a.get_attribute("src"))
                #time.sleep(200000)
                row[20] = ', '.join(list(set(images_new)))
                
            except Exception as e:
                print (e)
        wr.writerow(row)
        
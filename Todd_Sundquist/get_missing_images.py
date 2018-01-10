# -*- coding: utf-8 -*-
'''
Created on 08-Jan-2018

@author: Administrator
'''
import csv

from selenium import webdriver


driver = webdriver.Chrome()


output_f = open('output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['SKU','Name','Category','Fitment','Fitment HTMl','URL','Price','Features','Features HTML','Details','Details HTMl','Images'])
products_url = ''
with open('superatv_export(1).csv', encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if not row[11]:
            print(row[5] + row[11])
            try:
                driver.get(row[5])
                
                print (len(driver.find_elements_by_css_selector('.fotorama__thumb img')))
#                 for img in driver.find_elements_by_css_selector('.fotorama__thumb img'):
#                     driver.find_element_by_css_selector('.fotorama__arr--next div').click()
#                     time.sleep(2)
                images_new = []
                for a in driver.find_elements_by_css_selector('.fotorama__stage__frame [class="fotorama__img"]'):
                    images_new.append (a.get_attribute("src"))
                #time.sleep(200000)
                row[11] = ', '.join(images_new)
                
            except Exception as e:
                print (e)
        wr.writerow(row)
        
# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2018

@author: talib
'''
from selenium import webdriver
import time
import csv

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})

driver = webdriver.Chrome(chrome_options=chrome_options, service_args=["--verbose","--log-path=flipkart_scraper.log"])
output_f = open('flipkart_scrape.csv','w',encoding='utf8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Title',    'MRP',    'Selling Price',    'Ratings',    'Reviews',    'URL'])
INPUT_URLS = open('input_urls.txt',encoding='utf8').read().split('\n')
try:
    for url in INPUT_URLS:
    
            driver.get(url)
            
            while True:
                all_products = driver.find_elements_by_css_selector('.MP_3W3')
                product_count = len(all_products)
            
                print (product_count)
                
                for product in all_products:
                    details = []
                    title = ''
                    mrp = ''
                    selling_price = ''
                    ratings = ''
                    reviews = ''
                    url = ''
                    
                    try:
                        title =  product.find_element_by_css_selector('._2cLu-l').get_attribute('title')
                    except:
                        pass
                    
                    try:
                        url =  product.find_element_by_css_selector('._2cLu-l').get_attribute('href').split('?')[0]
                    except:
                        pass
                    try:
                        mrp = product.find_element_by_css_selector('._3auQ3N').text
                    except:
                        pass          
                    try:
                        selling_price = product.find_element_by_css_selector('._1vC4OE').text
                    except:
                        pass            
                    try:
                        ratings = product.find_element_by_css_selector('.hGSR34').text
                    except:
                        pass            
                    try:
                        reviews = product.find_element_by_css_selector('._38sUEc').text
                    except:
                        pass
                    details.append(title)
                    details.append(mrp)
                    details.append(selling_price)
                    details.append(ratings)
                    details.append(reviews)
                    details.append(url)
                    
                    wr.writerow (details)
                try:  
                    next1 = driver.find_element_by_xpath("//span[contains(text(),'Next')]/..").get_attribute('href')
                    driver.get(next1)
                    time.sleep(2)
                except:
                    break
except Exception as e:
    print ('Critical Error - '+ str(e))

driver.quit()

        
        
        
    
    
# -*- coding: utf-8 -*-
'''
Created on Aug 11, 2018

@author: tasshu
'''
from selenium import webdriver
import csv
import time

output_f = open('google_scraper_output.csv','w', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Search query',    'Title Link',  'GMB',  'Website Link',    'Closed',    'Not Claimed'])



search_queries = open('input_urls.txt').read().split('\n')

driver = webdriver.Chrome()

for query in search_queries:
    
    try:
        print ('Extracting : '+query)
        link_text = ""
        is_gmb_exists = ""
        is_permanent_closed_exists = ''
        is_own_this_buisness_exist = ''
        website = 'N/A'
        
        '''
        1) Get first link
        2) Check if GMB page exists
        3) Check if permanently closed exists
        4) check if Own this business? exists
        '''
        
    
        
        driver.get("https://www.google.de/search?q=" + query )
        
        time.sleep(5)
        
        #find element and get its attribute (link) i.e getting first link from google search
        link_text = driver.find_element_by_css_selector('[class="rc"] h3 a').get_attribute('href')
        
        
        #Check if GMB exists
        try:
            driver.find_element_by_css_selector('[id="rhs_block"] .g')
            is_gmb_exists = 'Yes'
        except Exception as e:
            is_gmb_exists = 'No'
        
        
        try:
            driver.find_element_by_css_selector('[id="rhs_block"] .g [data-attrid="kc:/local:permanently closed"]')
            is_permanent_closed_exists = 'Yes'
        except Exception as e:
            is_permanent_closed_exists = 'No'
        
        
        
        try:
            driver.find_element_by_css_selector('[ping^="/url?sa=t&source=web&rct=j&url=https://www.google.com/local/add/choice"]')
            is_own_this_buisness_exist = 'Yes'
        except Exception as e:
            is_own_this_buisness_exist = 'No'
        
        
        try:
            website = driver.find_element_by_css_selector('[id="rhs_block"] .g [class="ab_button"][ping^="/url?sa=t&source=web&rct=j&url="] ').get_attribute('href')
        except Exception as e:
            pass
        
        wr.writerow([query, link_text, is_gmb_exists, website, is_permanent_closed_exists, is_own_this_buisness_exist])
        
    except Exception as e:
        print ('Something went wrong with : ' + query)

driver.quit()
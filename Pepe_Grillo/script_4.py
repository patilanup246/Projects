# -*- coding: utf-8 -*-
'''
Created on Jun 14, 2018

@author: tasneem
'''


import linkedin_properties
import start_webdriver
import login_linkedin
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import csv

def message_profiles(driver):
    print ("Loading Profles")
    readCSV1 = csv.reader(open('linkedin_messages.csv',encoding='utf-8'), delimiter=',')
    cc = []
    for row in readCSV1:
        if row[5]:
            if not 'to_send' == row[5]:
                cc.append (row)
                print (row)
    for row in cc:
        
        try:
            driver.get(row[4])
            
            try:
                time.sleep(5)
                message_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pv-s-profile-actions--message')))
                
                #message_button.click()
                time.sleep(5)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                time.sleep(5)
                time.sleep(5)
                print ('Click the message button')
                driver.execute_script("$('.pv-s-profile-actions--message')[0].click();")
                print ('Message button clicked')
                time.sleep(5)
                print ("Will get message box")
                message_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea')))
                print ("Got message box")
                time.sleep(5)
                message_box.send_keys(row[5].replace('{first_name}',row[1]))
                print ("Message written in message box")
                time.sleep(5)
                driver.find_element_by_css_selector('[type="submit"]').click()
                
            except Exception as e:
                print("An Error Occured");
                print (e)
                
       
                
            
            time.sleep(30)

        except Exception as e:
            print("An Error Occured");
            print (e)




is_session_valid = login_linkedin.login_to_linkedin()

if is_session_valid:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        message_profiles(DRIVER)
    finally:
        DRIVER.quit()
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

def add_recent_connections(profiles):
    
    readCSV1 = csv.reader(open('linkedin_messages.csv',encoding='utf-8'), delimiter=',')
    cc = []
    for row in readCSV1:
        cc.append (row)
    for profile in profiles:
        is_new = 1
        for p in cc:
            if p[4] == profile[2]:
                is_new = 0
                break
            
        if is_new:
            cc.append([profile[0],profile[1],'','',profile[2]])
            
    output_f = open('linkedin_messages.csv','w',encoding='utf-8', newline='')
    wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
    #wr.writerow(['name', 'first_name', 'job_alert_url', 'message_thread_no', 'profile_url', 'to_send', '1', '2', '3', '4', '5'])
    for c in cc:
        wr.writerow(c)

def get_recent_connections(driver):
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
    
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="body"]')))
    profiles = []
    time.sleep(5)
    for i in range(10):
        #element.send_keys(Keys.END)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        
        
    for p in driver.find_elements_by_css_selector('[class="mn-connection-card__details"]')[:100]:
        profile = []
        
        profile.append(p.find_element_by_css_selector('.mn-connection-card__name ').text)
        profile.append(p.find_element_by_css_selector('.mn-connection-card__name ').text.split(' ')[0])
        profile.append(p.find_element_by_css_selector('[data-control-name="connection_profile"]').get_attribute('href'))
        
        profiles.append(profile)
    
        print (profile)
        
    return profiles



is_session_valid = login_linkedin.login_to_linkedin()

if is_session_valid:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        add_recent_connections(get_recent_connections(DRIVER))
    finally:
        DRIVER.quit()
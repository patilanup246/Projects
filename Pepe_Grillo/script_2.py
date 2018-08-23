# -*- coding: utf-8 -*-
'''
Created on May 19, 2018

@author: tasneem
'''
import linkedin_properties
import start_webdriver
import login_linkedin
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import sys
import csv


MAX_PAGE        =   linkedin_properties.MAX_PAGE
SEARCH_STRING   =   linkedin_properties.SEARCH_STRING





        
def get_new_profiles(driver):
    
    
    new_profile_file    = open('new_profile_file.txt','w')
    driver.get('https://www.linkedin.com/messaging')
    time.sleep(5)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-conversations-container__conversations-list')))
    counter = 1
    while True:
        if counter%100 == 0:
            thread_elements = driver.find_elements_by_css_selector('[data-control-name="view_message"]')
            if len(thread_elements) >= 100:
                for thel in thread_elements[:100]:
                    try:
                        #thel.find_element_by_css_selector('.msg-conversation-card__unread-count')
                        new_profile_file.write(thel.get_attribute('href')+'\n')
                        new_profile_file.flush()
                    except Exception as e:
                        #print (e)
                        pass
             
            
                break
        element.send_keys(Keys.ARROW_DOWN)
        counter+=1
    
    
        




        
        
def append_messages(driver):
    readCSV1 = csv.reader(open('linkedin_messages.csv',encoding='utf-8'), delimiter=',')
    cc1 = []
    for row in readCSV1:
        cc1.append (row)
    for tu in open('new_profile_file.txt','r').read().split('\n'):
        try:
            is_new = 1
            temp_row = []
            for row in cc1:
                if "'"+tu.replace('https://www.linkedin.com/messaging/thread/','').replace('/','')+"'" == row[3]:
                    is_new = 0
                    temp_row = row
                    cc1.remove(row)
                    break
                    
            driver.get(tu)
            details = []
            
            
            
            
            
            
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-s-event-listitem__body')))
            time.sleep(5)
            
            
            
            if is_new:
                name = driver.find_element_by_css_selector('h2.msg-entity-lockup__entity-title').text
                details.append(name)
                firstname = name.split(' ')[0]
                details.append(firstname)
                details.append('')
                message_thread_no = str(tu.replace('https://www.linkedin.com/messaging/thread/','').replace('/',''))
                details.append(message_thread_no)
                profile_link = driver.find_element_by_css_selector('[class="msg-thread__topcard-btn ember-view"]').get_attribute('href')
                details.append(profile_link)
                details.append('')
                all_messages = driver.find_elements_by_css_selector('.msg-s-event-listitem')
            
                for message in all_messages:
                    try:
                        
                        m = message.find_element_by_css_selector('.msg-s-message-group__name').text+' '+message.find_element_by_css_selector('.msg-s-message-group__timestamp').text+'\n'
                        
                        
                        
                        details.append(m+message.find_element_by_css_selector('.msg-s-event-listitem__body').text)
                    except Exception as e:
                        print (e)
            
                cc1.append(details)
                print ('New')
                print (details)
            else:
                all_messages = driver.find_elements_by_css_selector('.msg-s-event-listitem')
                
                for message in all_messages:
                    try:
                        
                        m = message.find_element_by_css_selector('.msg-s-message-group__name').text+' '+message.find_element_by_css_selector('.msg-s-message-group__timestamp').text+'\n'
                        full_message = m+message.find_element_by_css_selector('.msg-s-event-listitem__body').text
                        if not full_message in temp_row:
                            temp_row.append(full_message)
                    except Exception as e:
                        pass


                #print (details)
                cc1.append(temp_row)
                print (temp_row)
            time.sleep(5)
            
        except Exception as e:
            print (e)
        
    output_f = open('linkedin_messages.csv','w',encoding='utf-8', newline='')
    wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
    for row in cc1:
        wr.writerow(row)

is_session_valid = login_linkedin.login_to_linkedin()

if is_session_valid:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        get_new_profiles(DRIVER)
        append_messages(DRIVER)
    finally:
        DRIVER.quit()
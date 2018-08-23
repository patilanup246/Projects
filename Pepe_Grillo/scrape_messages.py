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





        
def get_all_profiles(driver):
    
    profile_file        = open('profile_file.txt','w')
    #new_profile_file    = open('new_profile_file.txt','w')
    driver.get('https://www.linkedin.com/messaging')
    time.sleep(5)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-conversations-container__conversations-list')))
    counter = 1
    last_count = 0
    while True:
        if counter%180 == 0:
            break
            thread_elements = driver.find_elements_by_css_selector('[data-control-name="view_message"]')
            current_size = len(thread_elements)
            if current_size > last_count:
                last_count = current_size
                print (current_size)
            else:
                for thel in thread_elements:
#                     try:
#                         thel.find_element_by_css_selector('.msg-conversation-card__unread-count')
#                         new_profile_file.write(thel.get_attribute('href')+'\n')
#                         new_profile_file.flush()
#                     except Exception as e:
#                         print (e)
                
                
                    profile_file.write(thel.get_attribute('href')+'\n')
                    profile_file.flush()
                break
        
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        counter+=1
        

def read_all_messages(driver):

    output_f = open('linkedin_messages.csv','w',encoding='utf-8', newline='')
    wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
    wr.writerow(['name', 'first_name', 'job_alert_url', 'message_thread_no', 'profile_url', 'to_send', '1', '2', '3', '4', '5'])

    #for tu in open('profile_file.txt','r').read().split('\n'):
    for tu in driver.find_elements_by_css_selector('[data-control-name="view_message"]'):
        try:
            
            driver.execute_script("arguments[0].click();", tu)
            details = []
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-s-event-listitem__body')))
            time.sleep(10)
            
            name = driver.find_element_by_css_selector('h2.msg-entity-lockup__entity-title').text
            details.append(name)
            firstname = name.split(' ')[0]
            details.append(firstname)
            details.append('')
            message_thread_no = "'"+str(tu.get_attribute('href').replace('https://www.linkedin.com/messaging/thread/','').replace('/',''))+"'"
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
                    pass


            print (details)
            wr.writerow(details)
            
            time.sleep(10)
            
        except Exception as e:
            print (e)


        

is_session_valid = login_linkedin.login_to_linkedin()

if is_session_valid:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        get_all_profiles(DRIVER)
        read_all_messages(DRIVER)
    finally:
        DRIVER.quit()
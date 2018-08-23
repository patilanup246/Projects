'''
Created on May 21, 2018

@author: tasneem
'''
import linkedin_properties
import start_webdriver
import login_linkedin
import database_connect
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time



def invite_profiles(driver):
    profiles = database_connect.get_connect_profiles()
    for profile in profiles:
        try:
            driver.get(profile)
            try:
                connect_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pv-s-profile-actions--connect')))
                connect_button.click()
                driver.execute_script("$('[class=\"button-primary-large ml1\"]').click()")
            except Exception as e:
                #print (e)
                driver.execute_script("$('[type=\"connect-icon\"]').click()")
                driver.execute_script("$('[class=\"button-primary-large ml1\"]').click()")
                
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type="success-pebble-icon"]')))
                database_connect.update_connect_profile(profile,True)
            except Exception as e:
                #print (e)
                database_connect.update_connect_profile(profile,False)
            #[type="success-pebble-icon"]
            
            time.sleep(linkedin_properties.DELAY_INBETWEEN_INVITES)
        except Exception as e:
            print (e)
                



is_session_valid = login_linkedin.login_to_linkedin()
if is_session_valid:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        
        
        invite_profiles(DRIVER)
        
        
    finally:
        DRIVER.quit()
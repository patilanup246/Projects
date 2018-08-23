'''
Created on May 19, 2018

@author: tasneem
'''
import linkedin_properties
from start_webdriver import create_driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys
import pickle
import time
import os


LINKEDIN_LOGIN_URL  =   linkedin_properties.LINKEDIN_LOGIN_URL
LINKEDIN_USERNAME   =   linkedin_properties.LINKEDIN_USERNAME
LINKEDIN_PASSWORD   =   linkedin_properties.LINKEDIN_PASSWORD






def load_cookies(driver):
    #deleting existing cookies
    driver.get('https://www.linkedin.com/lite/contentsecurity')
    driver.delete_all_cookies()
    
    #loading cookies
    cookies = pickle.load(open("linkedin_cookies.pkl", "rb")) 
        
    for cookie in cookies:
        try:
            driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path')})
        except Exception as e:
            pass
    


def is_loggedin(driver):
    try:
        
        load_cookies(driver)
        
        driver.get('https://www.linkedin.com/feed/')
        
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="main"]')))
        
        print ('Logged In')
        
        return True
        
        
    except Exception as e:
        print ('Exception raised in check_login\n' +str(e))

    return False


def login(driver, username, password):
    try:
        
        print ('Logging in')
        
        driver.get(LINKEDIN_LOGIN_URL)
        
        #fill_username
        driver.find_element_by_css_selector('.form-email input').send_keys(username)
        
        #fill password
        driver.find_element_by_css_selector('.form-password input').send_keys(password)
        
        #click button
        driver.find_element_by_css_selector('.form-buttons input').click()
    
        time.sleep(5)
        
        driver.get('https://www.linkedin.com/feed/')
        
        try:
            os.remove("linkedin_cookies.pkl")
        except Exception as e:
            pass
        
        pickle.dump(driver.get_cookies() , open("linkedin_cookies.pkl","wb"))
        
        
    except Exception as e:
        print ('Linkedin login failed. \n')
        print (e)
        sys.exit()
        
    

def login_to_linkedin():
    is_instantiated = 0
    try:
        DRIVER = create_driver()
        is_instantiated = 1
    except Exception as e:
        print ('Could not start selenium. Exiting ...')
        print (e)
        return False
        sys.exit()
    if not is_loggedin(DRIVER):
        login(DRIVER, LINKEDIN_USERNAME, LINKEDIN_PASSWORD)
    if is_instantiated:
        DRIVER.quit()
    return True
'''
Created on May 19, 2018

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
from selenium.webdriver.common.keys import Keys
import time

MAX_PAGE        =   linkedin_properties.MAX_PAGE
SEARCH_STRING   =   linkedin_properties.SEARCH_STRING

def scrape_results(driver, search_url):
    
    driver.get(search_url)
    page_num = 1
    
    profiles = []
    
    while True:
        if page_num <= MAX_PAGE:
            
            time.sleep(5)
            driver.find_element_by_css_selector('html').send_keys(Keys.END)
            
            for profile in driver.find_elements_by_css_selector('.search-result__info'):
                try:
                    name = profile.find_element_by_css_selector('.name').text
                    designation = profile.find_element_by_css_selector('.subline-level-1').text
                    location = profile.find_element_by_css_selector('.subline-level-2').text
                    linkedin_url = profile.find_element_by_css_selector('.search-result__result-link').get_attribute('href')
                    
                    profile = {}
                    profile['name'] = name
                    profile['designation'] = designation
                    profile['location'] =  location
                    profile['linkedin_url'] =  linkedin_url
                    profiles.append(profile)
                except Exception as e:
                    pass
                
            try:
                
                
                
                time.sleep(5)
                driver.find_element_by_css_selector('[class="next-text"]').click()
            except Exception as e:
                print (e)
                print ('Page limit reached by number of pages')
                break
            
            page_num+=1
            
            
        else:
            print ('Page limit reached by MAX_PAGE')
            break
    return profiles

is_session_valid = login_linkedin.login_to_linkedin()
if is_session_valid:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        results = scrape_results(DRIVER, SEARCH_STRING)
        database_connect.insert_profile(results)
    finally:
        DRIVER.quit()
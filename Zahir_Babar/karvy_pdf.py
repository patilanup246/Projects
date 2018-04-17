'''
Created on Mar 19, 2018

@author: talib
'''
from selenium import webdriver
import pickle
import time
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def start_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})
    return webdriver.Chrome(chrome_options=chrome_options)


def login(driver):
    driver.get('https://www.karvymfs.com/karvy/Distributor/Distributor_Login.aspx')
    driver.find_element_by_css_selector('[name="txtUserId"]').send_keys('redltd891')
    driver.find_element_by_css_selector('[name="txtPassword"]').send_keys('karvy123')
    driver.find_element_by_css_selector('[name="btnSubmit"]').click()

    


def get_report(driver, folio_num, tried,pdf):
    login(driver)
    driver.get('https://www.karvymfs.com/karvy/Distributor/Query/QueryNew.aspx')
    if 'Query New' in driver.title: 
        select = Select(driver.find_element_by_css_selector('[name="ctl00$MiddleContent$ddlfunds"]'))
        select.select_by_value(sys.argv[2])
        
        driver.find_element_by_css_selector('[name="ctl00$MiddleContent$txtAcNo"]').send_keys(folio_num)
        driver.find_element_by_css_selector('[name="ctl00$MiddleContent$btnQuery"]').click()
        
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="ctl00_MiddleContent_dgQueryDets"] tbody tr:nth-of-type(2) td:nth-of-type(4) a[href]')))
        element.click()
        
        driver.find_element_by_css_selector('[id="rdDetailed"]').click()
        time.sleep(0.3)
        driver.find_element_by_css_selector('[id="chkAllItems"]').click()
        driver.find_element_by_css_selector('[name="btnViewAndPrint"]').click()
        
        element_frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="hidName"][value]')))
        pdf = str(element_frame.get_attribute('value'))
        return pdf
            

is_instantiated = 0
try:
    DRIVER = start_webdriver()
    is_instantiated = 1
    pdf_file = ''
    print (get_report(DRIVER, str(sys.argv[1]), 1,pdf_file)) 
except Exception as e:
    print (e)
finally:
    if is_instantiated == 1:
        DRIVER.quit()
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


# account_num = sys.argv[1]
# account_type = sys.argv[2]

account_num = '0459910043792'
account_type = ''


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
#chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})
DRIVER = webdriver.Chrome(chrome_options=chrome_options)

def login(driver):
    driver.get('https://www.franklintempletonindia.com/')
    driver.find_element_by_css_selector('.dropdown.btn-group .fti-loginBtn').click()
    driver.find_element_by_css_selector('[name="loginName"]').send_keys('FINEDGE2017')
    driver.find_element_by_css_selector('[name="loginPwd"]').send_keys('Finedge@9414')
    driver.find_element_by_css_selector('[for*="rememberMe"] span').click()
    driver.find_element_by_css_selector('.login-submit-btn').click()
    time.sleep(3)

    


def get_report(driver, folio_num, tried,acco_type):

    login(driver)
        
    driver.get('https://accounts.franklintempletonindia.com/advisor/#/myinvestors')

    driver.find_element_by_css_selector('[id="simple-btn-keyboard-nav"]').click()

    for i in driver.find_elements_by_css_selector('[class="dropdown-menu"] [role="menuitem"] a'):
        if i.text == 'Account No.':
            i.click()
            break
        
    driver.find_element_by_css_selector('[placeholder="search..."]').send_keys('0359910184970')
    
    driver.find_element_by_css_selector('[ng-hide="hideSearch"].icon-fti_search').click()
    
    
    
    driver.find_element_by_css_selector('[name="ctl00$MiddleContent$txtAcNo"]').send_keys(folio_num)
    driver.find_element_by_css_selector('[name="ctl00$MiddleContent$btnQuery"]').click()
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="ctl00_MiddleContent_dgQueryDets"] tbody tr:nth-of-type(2) td:nth-of-type(4) a[href]')))
    element.click()
    
    driver.find_element_by_css_selector('[id="rdDetailed"]').click()
    time.sleep(0.3)
    driver.find_element_by_css_selector('[id="chkAllItems"]').click()
    driver.find_element_by_css_selector('[name="btnViewAndPrint"]').click()

    element_frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src*=AccountStmts]')))
    
    return (element_frame.get_attribute('src'))


#login(DRIVER)
try:
    print (get_report(DRIVER, str(account_num), 1,account_type)) 
except Exception as e:
    print (e)
finally:
    pass
    #DRIVER.quit()
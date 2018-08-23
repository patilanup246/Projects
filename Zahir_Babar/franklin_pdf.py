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
    driver.find_element_by_css_selector('.login-submit-btn').click()
    time.sleep(3)

    


def get_report(driver, folio_num, tried,acco_type):
    
    login(driver)
    is_account_active = 0
    try:    
        driver.get('https://accounts.franklintempletonindia.com/advisor/#/myinvestors')
        element_1 = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="simple-btn-keyboard-nav"]')))
        element_1.click()
        is_account_active = 1
        time.sleep(1)
        for i in driver.find_elements_by_css_selector('[class="dropdown-menu"] [role="menuitem"] a'):
            if i.text == 'Account No.':
                i.click()
                break
        #time.sleep(3)
        element_2 = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="search..."]')))
        element_2.send_keys('2199911341009')
        
        driver.find_element_by_css_selector('[ng-click="investorSearch()"]').click()
        

        
        time.sleep(5)
        driver.find_element_by_css_selector('[class="ui-grid-cell-contents ftic-uhName ng-binding ng-scope"]').click()
        time.sleep(5)
        driver.find_element_by_css_selector('[uib-btn-radio="\'accountview\'"]').click()
        
        time.sleep(5)
        element_4 = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-options="option.label | translate for option in filterOptions"]')))
        select = Select(element_4)
        select.select_by_visible_text('Since inception')
        
        time.sleep(5)
        
        driver.find_element_by_css_selector('[class="panel-orange-btn btn m0 pull-left"]').click()
        
        time.sleep(5)
        driver.find_element_by_css_selector('[class="icon-fti_download bold"]').click()
        time.sleep(5)
        driver.find_element_by_css_selector('[ng-click="download(\'pdf\')"]').click()
        #
        

    except Exception as e:
        print(e)
    
    if is_account_active:
        pass
        element_3 = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="icon icon-fti-Logout"]')))
        element_3.click()
         
        time.sleep(2)
        driver.execute_script('''$('[ng-if*="btnNo1!=="]')[0].click()''')

        


#login(DRIVER)
try:
    print (get_report(DRIVER, str(account_num), 1,account_type)) 
except Exception as e:
    print (e)
finally:
    pass
    DRIVER.quit()
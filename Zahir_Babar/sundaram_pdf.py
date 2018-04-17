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

folio_num = 'SBBNAB695734'


site_name = str(folio_num)

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
prefs = {
    "download.default_directory" : os.getcwd()+'\\SUNDARAM\\'+site_name
    }
chrome_options.add_experimental_option("prefs",prefs)
DRIVER = webdriver.Chrome(chrome_options=chrome_options)

def login(driver):
    driver.get('https://www.sundarambnpparibasfs.in/distributorservices/?amcid=bnpss')
    driver.find_element_by_css_selector('[class="iceInpTxt"]').send_keys('ARN-69442')
    driver.find_element_by_css_selector('[class="iceInpSecrt"]').send_keys('redmoney@12')
    driver.find_element_by_css_selector('[class="iceCmdBtn button"]').click()

    


def get_report(driver, folio_num, tried):

    login(driver)
       
    element_0 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[src="images/report.jpg"]')))
    element_0.click()
    
    element_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:investorsoafolio2:_2"]')))
    element_1.click()
    
    element_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="searchBrokF:textfolio"]')))
    element_2.send_keys(folio_num)
    time.sleep(0.5)
    element_3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name*="searchBrokF:j_idt"]')))
    element_3.click()
    time.sleep(0.5)
    element_3.click()
    time.sleep(0.5)
    element_4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:SlctSoaBrokerM:_4"]')))
    element_4.click()
    time.sleep(0.5)
    element_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:SlctFileModeBrokerM:_2"]')))
    element_5.click()
    time.sleep(0.5)
    element_6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:j_idt232"]')))
    element_6.click()


#login(DRIVER)
try:
    print  (get_report(DRIVER, folio_num, 1))
except Exception as e:
    print (e)
finally:
    time.sleep(3)
    DRIVER.quit()
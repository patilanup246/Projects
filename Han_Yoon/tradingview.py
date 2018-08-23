'''
Created on Jul 11, 2018

@author: tasneem
'''

import trading_view_config as config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from pyquery import PyQuery

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("no-sandbox")

#driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
is_started = 0
try:
    driver = webdriver.Chrome(chrome_options=chrome_options)
    is_started = 1
    driver.get(config.SCRAP_URL)
    
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tv-dialog__modal-wrap')))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tv-dialog__overlay')))
    driver.execute_script("$('.tv-dialog__modal-wrap').remove();")
    driver.execute_script("$('.tv-dialog__overlay').remove();")
    
    
    
    
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.backtesting-tab')))
    element.click()
    
    
    driver.find_element_by_css_selector('.report-tabs li:nth-of-type(3)').click()
    
    driver.execute_script("$('.bottom-widgetbar-content.backtesting').height(10000000);")
    
    driver.find_element_by_css_selector('.report-tabs li:nth-of-type(2)').click()
    
    driver.find_element_by_css_selector('.report-tabs li:nth-of-type(3)').click()
    
    time.sleep(5)
    
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    
    pq = PyQuery(html)
    
    for a in pq('.table-wrap tbody'):
        
        tr1 = pq(a)('tr:nth-of-type(1)')
        tr2 = pq(a)('tr:nth-of-type(2)')
        
        tradeID = pq(tr1)('.trade-num').text()
        numContracts = pq(tr1)('.trade-contracts').text()
        
        entryText  = pq(tr1)('.trade-e-comment').text()
        entryTime  = pq(tr1)('.trade-e-date').text()
        entryPrice = pq(tr1)('.trade-e-price').text()
        exitText   = pq(tr2)('.trade-x-comment').text()
        exitTime   = pq(tr2)('.trade-x-date').text()
        exitPrice  = pq(tr2)('.trade-x-price').text()
        
        print (tradeID, numContracts, entryText, entryTime, entryPrice, exitText, exitTime, exitPrice)
    
finally:
    if is_started:
        driver.quit()